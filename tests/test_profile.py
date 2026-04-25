from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.test_data import TestData


def test_change_password(page):
    login = LoginPage(page)
    profile = ProfilePage(page)

    # Navigate to application base URL
    page.goto(TestData.BASE_URL)

    # Perform login using existing valid credentials
    login.go_to_login()
    login.login(TestData.EXISTING_EMAIL_1, TestData.PASSWORD_1)

    # Navigate to user profile section
    profile.go_to_profile()

    # Update user password with a new value
    profile.change_password("000000000000")

    # Verify password change success message is displayed
    success_msg = page.locator(".jet-form-builder-message--success:visible").first
    assert success_msg.is_visible()
    assert "successfully changed your password" in success_msg.inner_text().lower()

    # Allow backend processing time before performing reset operation
    page.wait_for_timeout(2000)

    # Re-open profile page before resetting password (required for some UI flows)
    profile.go_to_profile()

    # Reset password back to original value for test consistency
    profile.change_password(TestData.PASSWORD_1)