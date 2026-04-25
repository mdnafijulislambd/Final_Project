from pages.base_page import BasePage


class ProfilePage(BasePage):

    # Navigate to user profile page from application UI
    # Locator should match current navigation structure of the application
    def go_to_profile(self):
        self.click("//a[contains(text(),'Profile')]")

    # Perform password change operation for logged-in user
    # Ensures both password fields are filled with identical value for validation success
    def change_password(self, new_password):
        # Open change password form/modal
        self.click("//span[text()='Change Password']")

        # Enter new password value
        self.fill("//input[@id='new_password']", new_password)

        # Confirm new password value
        self.fill("//input[@id='confirm_password']", new_password)

        # Submit password change request
        self.click("//button[@type='submit']")