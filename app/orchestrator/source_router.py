from __future__ import annotations

from typing import List

from app.schemas.source_resolution import (
    ConflictState,
    SourceReference,
    SourceResolution,
    SourceTier,
)
from app.schemas.task import Task, TaskKind


class SourceRouter:
    def resolve(self, task: Task) -> SourceResolution:
        if task.task_kind == TaskKind.ARCHITECTURE:
            return self._resolve_architecture(task)
        if task.task_kind == TaskKind.RUNTIME:
            return self._resolve_runtime(task)
        if task.task_kind == TaskKind.BUILD:
            return self._resolve_build(task)
        if task.task_kind == TaskKind.REFERENCE:
            return self._resolve_reference(task)
        return self._resolve_external(task)

    def _resolve_architecture(self, task: Task) -> SourceResolution:
        sources = [
            SourceReference(
                tier=SourceTier.CANONICAL,
                path="docs/MASTER_AI_SYSTEM_V2.md",
                rationale="Primary backend-brain architecture blueprint.",
                authoritative=True,
            ),
            SourceReference(
                tier=SourceTier.CANONICAL,
                path="docs/SOURCE_SYSTEM_BLUEPRINT.md",
                rationale="Defines source priority and doc authority.",
                authoritative=True,
            ),
        ]
        conflict_state, escalation_required, fail_closed, rationale = self._detect_conflict(task)
        rationale.insert(0, "Architecture work must consult canonical docs first.")
        return SourceResolution(
            task_id=task.task_id,
            preferred_tier=SourceTier.CANONICAL,
            consulted_tiers=[SourceTier.CANONICAL],
            selected_sources=sources,
            conflict_state=conflict_state,
            escalation_required=escalation_required,
            fail_closed=fail_closed,
            confidence=0.95,
            rationale=rationale,
        )

    def _resolve_runtime(self, task: Task) -> SourceResolution:
        sources = [
            SourceReference(
                tier=SourceTier.RUNTIME,
                path="main.py",
                rationale="Observed entry point for the current runtime path.",
            ),
            SourceReference(
                tier=SourceTier.RUNTIME,
                path="app/orchestrator/loop_manager.py",
                rationale="Observed execution loop for current runtime behavior.",
            ),
        ]
        conflict_state, escalation_required, fail_closed, rationale = self._detect_conflict(task)
        rationale.insert(0, "Runtime diagnostics should start from observed runtime artifacts.")
        return SourceResolution(
            task_id=task.task_id,
            preferred_tier=SourceTier.RUNTIME,
            consulted_tiers=[SourceTier.RUNTIME],
            selected_sources=sources,
            conflict_state=conflict_state,
            escalation_required=escalation_required,
            fail_closed=fail_closed,
            confidence=0.8,
            rationale=rationale,
        )

    def _resolve_build(self, task: Task) -> SourceResolution:
        sources = [
            SourceReference(
                tier=SourceTier.BUILD,
                path="docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md",
                rationale="Active Phase 1 runtime-spine build target.",
                authoritative=True,
            ),
            SourceReference(
                tier=SourceTier.BUILD,
                path="docs/build/PHASE_1_ACCEPTANCE_CRITERIA.md",
                rationale="Acceptance gate for the current build slice.",
                authoritative=True,
            ),
        ]
        conflict_state, escalation_required, fail_closed, rationale = self._detect_conflict(task)
        rationale.insert(0, "Build work should follow active build docs before reference notes.")
        return SourceResolution(
            task_id=task.task_id,
            preferred_tier=SourceTier.BUILD,
            consulted_tiers=[SourceTier.BUILD],
            selected_sources=sources,
            conflict_state=conflict_state,
            escalation_required=escalation_required,
            fail_closed=fail_closed,
            confidence=0.9,
            rationale=rationale,
        )

    def _resolve_reference(self, task: Task) -> SourceResolution:
        lowered = task.raw_input.lower()
        consulted: List[SourceTier] = [SourceTier.REFERENCE]
        sources = [
            SourceReference(
                tier=SourceTier.REFERENCE,
                path="docs/reference/DONOR_ADOPTION_MATRIX.md",
                rationale="Primary donor-boundary and adoption classification doc.",
            )
        ]
        preferred_tier = SourceTier.REFERENCE
        rationale = ["Reference work starts with donor and lesson docs."]
        if any(keyword in lowered for keyword in ("should", "adopt", "merge", "integrate", "use")):
            preferred_tier = SourceTier.CANONICAL
            consulted = [SourceTier.CANONICAL, SourceTier.REFERENCE]
            sources.insert(
                0,
                SourceReference(
                    tier=SourceTier.CANONICAL,
                    path="docs/MASTER_AI_SYSTEM_V2.md",
                    rationale="Canonical architecture must authorize donor adaptation.",
                    authoritative=True,
                ),
            )
            rationale.append("Adoption language detected; canonical authority outranks reference lessons.")
        conflict_state, escalation_required, fail_closed, conflict_rationale = self._detect_conflict(task)
        rationale.extend(conflict_rationale)
        confidence = 0.75 if preferred_tier == SourceTier.CANONICAL else 0.7
        return SourceResolution(
            task_id=task.task_id,
            preferred_tier=preferred_tier,
            consulted_tiers=consulted,
            selected_sources=sources,
            conflict_state=conflict_state,
            escalation_required=escalation_required,
            fail_closed=fail_closed,
            confidence=confidence,
            rationale=rationale,
        )

    def _resolve_external(self, task: Task) -> SourceResolution:
        conflict_state, escalation_required, fail_closed, rationale = self._detect_conflict(task)
        rationale.insert(0, "External lookups should be treated as lowest-authority sources.")
        return SourceResolution(
            task_id=task.task_id,
            preferred_tier=SourceTier.EXTERNAL,
            consulted_tiers=[SourceTier.EXTERNAL],
            selected_sources=[],
            conflict_state=conflict_state,
            escalation_required=escalation_required,
            fail_closed=fail_closed,
            confidence=0.5,
            rationale=rationale,
        )

    @staticmethod
    def _detect_conflict(task: Task) -> tuple[ConflictState, bool, bool, List[str]]:
        lowered = task.raw_input.lower()
        has_canonical_signal = any(keyword in lowered for keyword in ("should", "intended", "architecture"))
        has_runtime_signal = any(keyword in lowered for keyword in ("failed", "error", "status", "logs"))
        if has_canonical_signal and has_runtime_signal:
            rationale = [
                "Task mixes intended design and current observed state; escalation is required.",
            ]
            return (
                ConflictState.CANONICAL_RUNTIME_MISMATCH,
                True,
                task.high_impact,
                rationale,
            )
        return ConflictState.NONE, False, False, []
