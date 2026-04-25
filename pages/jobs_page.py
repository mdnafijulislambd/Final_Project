from pages.base_page import BasePage


class JobsPage(BasePage):

    # Navigate to Jobs section from main navigation menu
    # Ensures correct page transition before applying filters or actions
    def go_to_jobs(self):
        self.click("//span[text()='Jobs']")

    # Apply country filter for job search results
    # Selects "Bangladesh" as filtering criteria from dropdown list
    def filter_country(self):
        self.page.select_option("//select[@name='vacancy-country']", label="Bangladesh")

    # Trigger job search based on selected filters
    # Executes search action to refresh job listings
    def search(self):
        self.click("//button[text()='Search']")

    # Save first available job from search results
    # Uses first match to ensure deterministic selection in test execution
    def save_job(self):
        self.page.locator("//span[contains(text(),'Save')]").first.click()