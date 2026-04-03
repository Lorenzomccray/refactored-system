try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None

class PlaywrightController:
    def __init__(self):
        self._playwright_context = None
        self._browser = None
        self._page = None

    def _ensure_browser(self):
        if sync_playwright is None:
            raise ImportError("Playwright is not installed. Please run 'pip install playwright' and 'playwright install'.")
        
        if self._browser is None:
            self._playwright_context = sync_playwright().start()
            self._browser = self._playwright_context.chromium.launch(headless=True)
            self._page = self._browser.new_page()

    def open(self, url: str):
        self._ensure_browser()
        self._page.goto(url)
        return f"Opened {url}"

    def click(self, selector: str):
        self._ensure_browser()
        self._page.click(selector)
        return f"Clicked {selector}"

    def fill(self, selector: str, value: str):
        self._ensure_browser()
        self._page.fill(selector, value)
        return f"Filled {selector} with {value}"

    def text(self, selector: str):
        self._ensure_browser()
        return self._page.inner_text(selector)

    def close(self):
        if self._browser:
            self._browser.close()
            self._playwright_context.stop()
            self._browser = None
            self._playwright_context = None
            self._page = None
        return "Browser closed"
