from __future__ import annotations

from typing import List

from app.schemas.task import RequestedActionClass, Task, TaskKind


class TaskClassifier:
    _ARCHITECTURE_KEYWORDS = (
        "architecture",
        "design",
        "schema",
        "policy",
        "blueprint",
        "intended",
        "adr",
    )
    _RUNTIME_KEYWORDS = (
        "error",
        "failed",
        "failure",
        "traceback",
        "status",
        "running",
        "logs",
        "crash",
    )
    _BUILD_KEYWORDS = (
        "build",
        "requirements",
        "dependency",
        "install",
        "workflow",
        "ci",
        "python version",
        "package",
    )
    _REFERENCE_KEYWORDS = (
        "donor",
        "gobii",
        "openclaw",
        "manus",
        "tasklet",
        "pattern",
        "lesson",
        "reference",
    )
    _EXTERNAL_KEYWORDS = (
        "http://",
        "https://",
        "model card",
        "api limit",
        "vendor",
        "external",
    )
    _WRITE_KEYWORDS = ("write", "create", "update", "edit", "patch")
    _EXECUTION_KEYWORDS = (
        "run:",
        "execute",
        "restart",
        "delete",
        "remove",
        "drop",
        "shutdown",
    )
    _HIGH_IMPACT_KEYWORDS = (
        "delete",
        "drop",
        "destroy",
        "shutdown",
        "credential",
        "secret",
        "token",
    )

    def classify(self, task_id: str, raw_input: str) -> Task:
        text = raw_input.strip()
        lowered = text.lower()
        rationale: List[str] = []
        tags = self._extract_tags(lowered)
        task_kind = self._classify_kind(lowered, rationale)
        action_class = self._classify_action(lowered, rationale)
        high_impact = any(keyword in lowered for keyword in self._HIGH_IMPACT_KEYWORDS)
        normalized_goal = self._normalize_goal(text)
        return Task(
            task_id=task_id,
            raw_input=text,
            normalized_goal=normalized_goal,
            task_kind=task_kind,
            requested_action_class=action_class,
            rationale=rationale,
            tags=tags,
            high_impact=high_impact,
        )

    def _classify_kind(self, lowered: str, rationale: List[str]) -> TaskKind:
        if self._contains_any(lowered, self._RUNTIME_KEYWORDS):
            rationale.append("Runtime keywords detected; selecting runtime classification.")
            return TaskKind.RUNTIME
        if self._contains_any(lowered, self._BUILD_KEYWORDS):
            rationale.append("Build/config keywords detected; selecting build classification.")
            return TaskKind.BUILD
        if self._contains_any(lowered, self._ARCHITECTURE_KEYWORDS):
            rationale.append("Architecture keywords detected; selecting architecture classification.")
            return TaskKind.ARCHITECTURE
        if self._contains_any(lowered, self._REFERENCE_KEYWORDS):
            rationale.append("Donor/reference keywords detected; selecting reference classification.")
            return TaskKind.REFERENCE
        if self._contains_any(lowered, self._EXTERNAL_KEYWORDS):
            rationale.append("External lookup keywords detected; selecting external classification.")
            return TaskKind.EXTERNAL
        rationale.append("No strong signal detected; defaulting to architecture classification.")
        return TaskKind.ARCHITECTURE

    def _classify_action(
        self,
        lowered: str,
        rationale: List[str],
    ) -> RequestedActionClass:
        if self._contains_any(lowered, self._EXECUTION_KEYWORDS):
            rationale.append("Execution verb detected; classifying as LOCAL_EXECUTION.")
            return RequestedActionClass.LOCAL_EXECUTION
        if self._contains_any(lowered, self._WRITE_KEYWORDS):
            rationale.append("Write verb detected; classifying as LOCAL_WRITE.")
            return RequestedActionClass.LOCAL_WRITE
        if self._contains_any(lowered, self._EXTERNAL_KEYWORDS):
            rationale.append("External lookup signal detected; classifying as EXTERNAL_API_CALL.")
            return RequestedActionClass.EXTERNAL_API_CALL
        rationale.append("No state-changing action detected; classifying as READ_ONLY.")
        return RequestedActionClass.READ_ONLY

    @staticmethod
    def _normalize_goal(text: str) -> str:
        if text.lower().startswith("run:"):
            return text[4:].strip()
        return text

    @staticmethod
    def _contains_any(lowered: str, keywords: tuple[str, ...]) -> bool:
        return any(keyword in lowered for keyword in keywords)

    @staticmethod
    def _extract_tags(lowered: str) -> List[str]:
        tags = []
        for candidate in ("manus", "tasklet", "gobii", "openclaw", "mcp"):
            if candidate in lowered:
                tags.append(candidate)
        return tags
