from dataclasses import dataclass
from typing import Iterable


RISKY_KEYWORDS = {
    "delete",
    "rm ",
    "drop database",
    "truncate",
    "force push",
    "reboot",
    "shutdown",
    "restart service",
}


@dataclass
class ApprovalResult:
    approved: bool
    reason: str
    requires_confirmation: bool = False


class ApprovalEngine:
    def __init__(self, risky_keywords: Iterable[str] | None = None):
        self.risky_keywords = set(risky_keywords or RISKY_KEYWORDS)

    def evaluate(self, action_text: str, confirmed: bool = False) -> ApprovalResult:
        lowered = action_text.lower()
        risky = any(keyword in lowered for keyword in self.risky_keywords)
        if not risky:
            return ApprovalResult(True, "Action allowed", False)
        if confirmed:
            return ApprovalResult(True, "Risky action confirmed by user", True)
        return ApprovalResult(False, "Risky action requires explicit confirmation", True)
