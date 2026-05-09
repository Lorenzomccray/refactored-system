"""Pydantic contracts for the Sovereign Upgrade Plane.

These schemas define the governed intake, adapter registry, and upgrade receipt
objects used by the FastAPI brain, Temporal workflows, MCP Gateway, and Cortex
receipt layer.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class RiskClass(str, Enum):
    READ_ONLY = "READ_ONLY"
    LOCAL_WRITE = "LOCAL_WRITE"
    LOCAL_EXECUTION = "LOCAL_EXECUTION"
    EXTERNAL_API_CALL = "EXTERNAL_API_CALL"
    DATABASE_MUTATION = "DATABASE_MUTATION"
    BROWSER_AUTOMATION = "BROWSER_AUTOMATION"
    CREDENTIAL_USE = "CREDENTIAL_USE"
    IRREVERSIBLE = "IRREVERSIBLE"


class AdapterType(str, Enum):
    TOOL = "TOOL"
    PROVIDER = "PROVIDER"
    SANDBOX = "SANDBOX"
    NOTIFICATION = "NOTIFICATION"
    PERSISTENCE = "PERSISTENCE"
    DOMAIN = "DOMAIN"
    WORKFLOW = "WORKFLOW"
    MEMORY = "MEMORY"
    BROWSER = "BROWSER"


class LicenseStatus(str, Enum):
    VERIFIED_ALLOWED = "VERIFIED_ALLOWED"
    VERIFIED_RESTRICTED = "VERIFIED_RESTRICTED"
    AGPL_RESTRICTED = "AGPL_RESTRICTED"
    COMMERCIAL_RESTRICTED = "COMMERCIAL_RESTRICTED"
    UNKNOWN = "UNKNOWN"
    CONCEPT_ONLY = "CONCEPT_ONLY"


class AdapterRegistryStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    SANDBOX_PASSED = "SANDBOX_PASSED"
    REGISTERED_DISABLED = "REGISTERED_DISABLED"
    MONITOR_MODE = "MONITOR_MODE"
    ACTIVE_GOVERNED = "ACTIVE_GOVERNED"
    SUSPENDED = "SUSPENDED"
    DEPRECATED = "DEPRECATED"


class DependencySpec(BaseModel):
    name: str
    version: Optional[str] = None
    source: Optional[str] = None
    required: bool = True
    risk_note: Optional[str] = None


class VerificationTestSpec(BaseModel):
    name: str
    command: Optional[str] = None
    test_type: str = Field(description="unit | integration | sandbox | health | policy")
    expected_result: str
    timeout_seconds: int = 300
    requires_network: bool = False
    requires_credentials: bool = False


class HealthCheckSpec(BaseModel):
    command: Optional[str] = None
    endpoint: Optional[str] = None
    expected_output: str
    timeout_seconds: int = 60


class RollbackSpec(BaseModel):
    rollback_command: Optional[str] = None
    rollback_strategy: str = Field(description="disable | restore_previous_registry | uninstall | revert_config | manual")
    expected_result: str
    destructive: bool = False


class CapabilityIntakeSubmission(BaseModel):
    name: str = Field(min_length=2)
    display_name: str
    description: str
    domain: str = Field(description="legal | ecommerce | social_media | coding | browser | provider | memory | ops | etc.")
    risk_class: RiskClass
    adapter_type: AdapterType
    source_repo_or_url: Optional[str] = None
    source_commit: Optional[str] = None
    source_branch: Optional[str] = None
    source_local_path: Optional[str] = None

    owner: str = Field(description="human or system owner accountable for this capability")
    requested_by: str = "user"
    approval_required: bool = True

    license_check: LicenseStatus
    license_name: Optional[str] = None
    license_file_path: Optional[str] = None
    license_notes: Optional[str] = None

    dependencies: List[DependencySpec] = []
    verification_test: VerificationTestSpec
    health_check_command: Optional[str] = None
    health_check: Optional[HealthCheckSpec] = None
    rollback_command: Optional[str] = None
    rollback: RollbackSpec

    allowed_operations: List[str] = []
    blocked_operations: List[str] = []
    credential_requirements: List[str] = []
    credential_boundary: str = "none"
    network_boundary: str = "none"
    filesystem_boundary: str = "none"

    sandbox_required: bool = True
    sandbox_type: str = Field(default="mock", description="mock | e2b | docker | temporal_namespace | local_readonly")
    temporal_namespace: Optional[str] = None

    registry_tags: List[str] = []
    metadata: Dict[str, Any] = {}

    class Config:
        extra = "forbid"


class UpgradeApprovalRecord(BaseModel):
    approved: bool
    approved_by: str
    approved_at: str
    justification: str
    approved_scope: str
    approved_operations: List[str]


class UpgradeTestResult(BaseModel):
    name: str
    status: str
    expected_result: str
    actual_result: str
    evidence_refs: List[str] = []


class UpgradeReceipt(BaseModel):
    id: str
    receipt_type: str = "UPGRADE_RECEIPT"

    capability_name: str
    capability_domain: str
    adapter_type: AdapterType
    adapter_id: str
    version: str

    workflow_id: str
    temporal_run_id: Optional[str] = None
    initiated_by: str
    approved_by: Optional[str] = None

    status: str = Field(description="tested | promoted | rejected | blocked | rolled_back | deprecated")

    created_at: str
    completed_at: Optional[str] = None

    source_repo_or_url: Optional[str] = None
    source_commit: Optional[str] = None

    license_status: LicenseStatus
    license_name: Optional[str] = None
    license_notes: Optional[str] = None

    risk_class: RiskClass
    allowed_operations: List[str]
    blocked_operations: List[str]

    tests_passed: bool
    test_results: List[UpgradeTestResult]

    approvals: List[UpgradeApprovalRecord]

    rollback_strategy: str
    rollback_command: Optional[str] = None
    rollback_verified: bool

    previous_system_state_hash: str
    new_system_state_hash: Optional[str] = None

    registry_entry_before: Optional[Dict[str, Any]] = None
    registry_entry_after: Optional[Dict[str, Any]] = None

    health_check_result: Optional[Dict[str, Any]] = None
    policy_check_result: Optional[Dict[str, Any]] = None

    evidence_refs: List[str] = []
    final_summary: str

    canonical_payload_hash: str
    previous_receipt_hash: Optional[str] = None
    receipt_hash: str


class AdapterRegistryEntry(BaseModel):
    adapter_id: str
    capability_name: str
    adapter_type: AdapterType
    domain: str
    version: str
    source_repo_or_url: Optional[str] = None
    source_commit: Optional[str] = None

    owner: str
    status: AdapterRegistryStatus
    risk_class: RiskClass

    allowed_operations: List[str]
    blocked_operations: List[str]

    license_status: LicenseStatus
    license_notes: Optional[str] = None

    health_check: HealthCheckSpec
    rollback: RollbackSpec

    requires_approval: bool
    requires_credentials: bool
    credential_boundary: str

    sandbox_receipt_id: Optional[str] = None
    promotion_receipt_id: Optional[str] = None
    rollback_receipt_ids: List[str] = []

    previous_state_hash: Optional[str] = None
    registry_entry_hash: str
    created_at: str
    updated_at: str
