from __future__ import annotations

from typing import Any, Dict

from app.schemas.source_resolution import SourceResolution
from app.schemas.task import Task


class ContextLoader:
    def load(self, task: Task, resolution: SourceResolution) -> Dict[str, Any]:
        return {
            "task": task.to_dict(),
            "source_resolution": resolution.to_dict(),
            "source_attribution": resolution.receipt_inputs(),
            "policy_context": {
                "requested_action_class": task.requested_action_class.value,
                "high_impact": task.high_impact,
            },
            "working_context": {
                "selected_paths": [source.path for source in resolution.selected_sources],
                "consulted_tiers": [tier.value for tier in resolution.consulted_tiers],
                "rationale": list(resolution.rationale),
            },
        }
