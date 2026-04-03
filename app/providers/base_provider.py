from typing import Any, Dict


class BaseProvider:
    name: str = "base"

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError
