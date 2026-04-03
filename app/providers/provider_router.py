class ProviderRouter:
    def route(self, task: str) -> str:
        """
        Determines the appropriate provider based on the task.
        Currently returns "openai" by default.
        """
        # Return "openai" by default for now
        # Keep it simple, but make it ready for future providers
        return "openai"
