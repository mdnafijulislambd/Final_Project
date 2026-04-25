from utils.allure_utils import attach_screenshot


class BasePage:

    # Initialize BasePage with Playwright page instance
    # Acts as the core parent class for all Page Objects
    def __init__(self, page):
        self.page = page

    # Generic click action wrapper for UI interaction
    def click(self, locator):
        self.page.click(locator)

    # Generic input handler for form fields
    def fill(self, locator, value):
        self.page.fill(locator, value)

    # Capture full page text in lowercase format
    # Useful for global validation and assertion logic
    def get_text(self):
        return self.page.locator("body").inner_text().lower()

    # Take screenshot manually when needed (useful for debugging or failure handling)
    def take_screenshot(self, name="screenshot"):
        attach_screenshot(self.page, name)