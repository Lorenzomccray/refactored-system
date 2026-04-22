from app.orchestrator.source_router import SourceRouter
from app.orchestrator.task_classifier import TaskClassifier
from app.schemas.source_resolution import ConflictState, SourceTier
from app.schemas.task import RequestedActionClass, TaskKind


def test_architecture_query_routes_to_canonical():
    task = TaskClassifier().classify("task-1", "What is the intended architecture for this system?")
    resolution = SourceRouter().resolve(task)

    assert task.task_kind == TaskKind.ARCHITECTURE
    assert task.requested_action_class == RequestedActionClass.READ_ONLY
    assert resolution.preferred_tier == SourceTier.CANONICAL
    assert resolution.selected_sources[0].path == "docs/MASTER_AI_SYSTEM_V2.md"


def test_runtime_query_routes_to_runtime_artifacts():
    task = TaskClassifier().classify("task-2", "Why did the task fail and what do the logs show?")
    resolution = SourceRouter().resolve(task)

    assert task.task_kind == TaskKind.RUNTIME
    assert resolution.preferred_tier == SourceTier.RUNTIME
    assert any(source.path == "main.py" for source in resolution.selected_sources)


def test_build_query_routes_to_build_docs():
    task = TaskClassifier().classify("task-3", "What build doc defines the current implementation target?")
    resolution = SourceRouter().resolve(task)

    assert task.task_kind == TaskKind.BUILD
    assert resolution.preferred_tier == SourceTier.BUILD
    assert resolution.selected_sources[0].path == "docs/build/PHASE_1_SOVEREIGN_RUNTIME_SPINE.md"


def test_donor_adoption_query_consults_canonical_and_reference():
    task = TaskClassifier().classify("task-4", "Should we adopt the Gobii pattern for this project?")
    resolution = SourceRouter().resolve(task)

    assert task.task_kind == TaskKind.REFERENCE
    assert resolution.preferred_tier == SourceTier.CANONICAL
    assert resolution.consulted_tiers == [SourceTier.CANONICAL, SourceTier.REFERENCE]
    assert resolution.selected_sources[1].path == "docs/reference/DONOR_ADOPTION_MATRIX.md"


def test_conflict_is_represented_without_flattening():
    task = TaskClassifier().classify(
        "task-5",
        "Should the architecture change because the current runtime failed with errors and logs?",
    )
    resolution = SourceRouter().resolve(task)

    assert resolution.conflict_state == ConflictState.CANONICAL_RUNTIME_MISMATCH
    assert resolution.escalation_required is True
