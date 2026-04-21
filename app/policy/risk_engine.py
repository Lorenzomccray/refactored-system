from dataclasses import dataclass
from enum import Enum
from typing import Optional


class RiskClass(str, Enum):
    READ_ONLY = "READ_ONLY"
    LOCAL_WRITE = "LOCAL_WRITE"
    LOCAL_EXECUTION = "LOCAL_EXECUTION"
    EXTERNAL_API_CALL = "EXTERNAL_API_CALL"
    DATABASE_MUTATION = "DATABASE_MUTATION"
    BROWSER_AUTOMATION = "BROWSER_AUTOMATION"
    CREDENTIAL_USE = "CREDENTIAL_USE"
    IRREVERSIBLE = "IRREVERSIBLE"


@dataclass(slots=True)
class ClassifiedAction:
    action_type: str
    risk_class: RiskClass
    reason: str
    tool_name: Optional[str] = None


class RiskEngine:
    """Minimal fail-closed classifier for the first code milestone."""

    def classify(self, action_type: str, tool_name: Optional[str] = None) -> ClassifiedAction:
        action = (action_type or "").strip().lower()
        tool = (tool_name or "").strip().lower()

        if action in {"read", "inspect", "describe", "list", "plan"}:
            return ClassifiedAction(action_type=action_type, risk_class=RiskClass.READ_ONLY, reason="Read-only or inspection style action", tool_name=tool_name)
        if tool in {"shell", "shell_tool"} or action in {"run", "execute"}:
            return ClassifiedAction(action_type=action_type, risk_class=RiskClass.LOCAL_EXECUTION, reason="Local command or execution request", tool_name=tool_name)
        if tool in {"browser", "browser_tool", "playwright"} or action in {"browse", "navigate", "click", "fill"}:
            return ClassifiedAction(action_type=action_type, risk_class=RiskClass.BROWSER_AUTOMATION, reason="Browser interaction requested", tool_name=tool_name)
        if action in {"write", "patch", "edit", "save"}:
            return ClassifiedAction(action_type=action_type, risk_class=RiskClass.LOCAL_WRITE, reason="Local write-style action", tool_name=tool_name)
        if action in {"delete", "destroy", "drop"}:
            return ClassifiedAction(action_type=action_type, risk_class=RiskClass.IRREVERSIBLE, reason="Irreversible action requested", tool_name=tool_name)

        return ClassifiedAction(action_type=action_type, risk_class=RiskClass.READ_ONLY, reason="Unknown actions default to lowest-capability mock path for scaffolding", tool_name=tool_name)
