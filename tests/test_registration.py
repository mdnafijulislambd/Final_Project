import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.helpers import generate_user
from utils.test_data import TestData


@allure.title("User Registration - Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authentication")
@allure.story("Candidate Registration")
def test_registration_positive(page):

    login = LoginPage(page)
    reg = RegistrationPage(page)

    username, email = generate_user()

    page.goto(TestData.BASE_URL)
    page.wait_for_load_state("domcontentloaded")

    login.go_to_login()
    login.go_to_registration()

    reg.select_candidate()
    reg.enter_candidate_details(username, email, TestData.PASSWORD)
    reg.submit()

    page.wait_for_url("**status=success**")
    assert "status=success" in page.url


@allure.title("Registration with existing email")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Duplicate Email Validation")
def test_registration_existing_email(page):

    login = LoginPage(page)
    reg = RegistrationPage(page)

    page.goto(TestData.BASE_URL)
    page.wait_for_load_state("domcontentloaded")

    login.go_to_login()
    login.go_to_registration()

    reg.select_candidate()
    reg.enter_candidate_details(
        "testuser",
        TestData.EXISTING_EMAIL,
        TestData.PASSWORD
    )

    reg.submit()

    error = page.locator("body").inner_text().lower()
    assert "already" in error or "exist" in error