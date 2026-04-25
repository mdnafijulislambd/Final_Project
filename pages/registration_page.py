from pages.base_page import BasePage


class RegistrationPage(BasePage):

    # Select candidate registration option from UI
    # Ensures element is visible before performing click action
    def select_candidate(self):
        self.page.wait_for_selector(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Candidate']]"
        )
        self.page.click(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Candidate']]"
        )

    # Select recruiter registration option from UI
    # Uses stable locator with visibility check before interaction
    def select_recruiter(self):
        self.page.wait_for_selector(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Recruiter']]"
        )
        self.page.click(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Recruiter']]"
        )

    # Fill recruiter registration form with provided test data
    def enter_recruiter_details(self, company, email, phone, password):
        self.page.wait_for_selector("//input[@id='_recruiter-company-name']")

        self.page.fill("//input[@id='_recruiter-company-name']", company)
        self.page.fill("//input[@id='_recruiter-email']", email)
        self.page.fill("//input[contains(@class,'phone-class')]", phone)
        self.page.fill("//input[@id='password']", password)
        self.page.fill("//input[@id='confirm-password']", password)

    # Fill candidate registration form with provided test data
    def enter_candidate_details(self, username, email, password):
        # Ensure form is fully loaded before interacting with fields
        self.page.wait_for_selector("//input[@id='username']")

        self.page.fill("//input[@id='username']", username)
        self.page.fill("//input[@id='email']", email)
        self.page.fill("//input[@id='password']", password)
        self.page.fill("//input[@id='conf-pass']", password)

    # Submit registration form for both candidate and recruiter flows
    def submit(self):
        self.page.click("//button[contains(@class,'submit')]")