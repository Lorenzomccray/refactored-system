from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(slots=True)
class ToolContract:
    tool_name: str
    tool_version: str
    description: str
    input_schema: str
    output_schema: str
    risk_class: str
    approval_required: bool
    timeout_seconds: int = 30
    verification_method: str = "syntactic"
    artifact_outputs: List[str] = field(default_factory=list)
    secret_requirements: List[str] = field(default_factory=list)
    sandbox_required: bool = False
    metadata: Dict[str, str] = field(default_factory=dict)

    def validate(self) -> None:
        required = {
            "tool_name": self.tool_name,
            "tool_version": self.tool_version,
            "input_schema": self.input_schema,
            "output_schema": self.output_schema,
            "risk_class": self.risk_class,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise ValueError(f"Tool contract missing required fields: {', '.join(missing)}")


class MockToolRegistry:
    """Minimal registry for the first code milestone."""

    def __init__(self) -> None:
        self._contracts: Dict[str, ToolContract] = {}

    def register(self, contract: ToolContract) -> None:
        contract.validate()
        self._contracts[contract.tool_name] = contract

    def get(self, tool_name: str) -> Optional[ToolContract]:
        return self._contracts.get(tool_name)
