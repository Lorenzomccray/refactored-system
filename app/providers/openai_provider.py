import os
from typing import Any, Dict
from openai import OpenAI
from app.providers.base_provider import BaseProvider

class OpenAIProvider(BaseProvider):
    name = "openai"

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        if not self.api_key or not self.client:
            return {
                "provider": self.name,
                "model": kwargs.get("model", "gpt-4o"),
                "output": "",
                "ok": False,
                "error": "OPENAI_API_KEY is missing from environment"
            }
        
        try:
            model = kwargs.get("model", "gpt-4o")
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **{k: v for k, v in kwargs.items() if k != "model"}
            )
            
            return {
                "provider": self.name,
                "model": model,
                "output": response.choices[0].message.content,
                "ok": True,
                "error": None
            }
        except Exception as e:
            return {
                "provider": self.name,
                "model": kwargs.get("model", "gpt-4o"),
                "output": "",
                "ok": False,
                "error": str(e)
            }
