from dataclasses import dataclass
from typing import Dict


@dataclass
class BrowserContext:
    url: str = ""
    title: str = ""
    selected_text: str = ""


class BrowserContextService:
    def __init__(self):
        self._context = BrowserContext()

    def update(self, data: Dict[str, str]):
        self._context.url = data.get("url", self._context.url)
        self._context.title = data.get("title", self._context.title)
        self._context.selected_text = data.get("selected_text", self._context.selected_text)

    def get(self) -> BrowserContext:
        return self._context
