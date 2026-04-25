from pages.base_page import BasePage


class LoginPage(BasePage):

    # Navigate to login page from authentication entry point
    # Ensures correct page transition before performing login actions
    def go_to_login(self):
        self.page.click("//span[contains(@class,'jet-auth-links__item-text')]")
        self.page.wait_for_url("**login**")

    # Navigate to registration page from login screen
    # Verifies URL change to confirm successful navigation
    def go_to_registration(self):
        self.page.click("//span[normalize-space()='Register Now']")
        self.page.wait_for_url("**registration**")

    # Perform login action using provided credentials
    # Includes form field validation before submission
    def login(self, email, password):
        # Ensure login form is fully loaded before interaction
        self.page.wait_for_selector("//input[@id='email']")

        # Enter user email
        self.page.fill("//input[@id='email']", email)

        # Enter user password
        self.page.fill("//input[@id='password']", password)

        # Optional UI interaction (remember me checkbox)
        self.page.click("text=Remember me")

        # Submit login form
        self.page.click("//button[contains(@class,'submit')]")

    # Validate successful login by confirming navigation to authenticated area
    def wait_for_login_success(self):
        self.page.wait_for_url("**account**")