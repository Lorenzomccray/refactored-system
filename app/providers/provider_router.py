from dataclasses import dataclass


@dataclass(slots=True)
class ProviderRouteDecision:
    provider_name: str
    model_name: str
    route_reason: str
    privacy_class: str = "standard"


class ProviderRouter:
    """Minimal provider router scaffold aligned to the doctrine-first core."""

    def select(
        self,
        *,
        agent_role: str = "builder",
        requires_local_only: bool = False,
        requires_structured_output: bool = False,
    ) -> ProviderRouteDecision:
        if requires_local_only:
            return ProviderRouteDecision(
                provider_name="local",
                model_name="local-default",
                route_reason="Local-only path requested by policy.",
                privacy_class="local-only",
            )

        if agent_role == "verifier" and requires_structured_output:
            return ProviderRouteDecision(
                provider_name="openai",
                model_name="gpt-4o",
                route_reason="Structured verification path for the minimal scaffold.",
            )

        if agent_role == "planner":
            return ProviderRouteDecision(
                provider_name="openai",
                model_name="gpt-4o",
                route_reason="Default reasoning route for planner scaffolding.",
            )

        return ProviderRouteDecision(
            provider_name="openai",
            model_name="gpt-4o-mini",
            route_reason="Default execution route for minimal scaffolding.",
        )

    def route(self, task: str) -> str:
        """Backward-compatible route method used by current prototype code."""
        decision = self.select(agent_role="builder")
        return decision.provider_name
