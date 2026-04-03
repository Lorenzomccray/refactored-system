import os
from typing import Any, Dict

from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    name = "openai"

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        # Stub: replace with real OpenAI client call
        return {
            "provider": self.name,
            "output": f"[OPENAI STUB] {prompt}",
        }
