import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.test_data import TestData


def test_case_4(page):

    login = LoginPage(page)
    reg = RegistrationPage(page)

    data = TestData.generate_recruiter()

    with allure.step("Open application"):
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")

    with allure.step("Go to registration"):
        login.go_to_login()
        login.go_to_registration()

    with allure.step("Select recruiter"):
        reg.select_recruiter()

    with allure.step("Fill recruiter form"):
        reg.enter_recruiter_details(
            company=data["company"],
            email=data["email"],
            phone=data["phone"],
            password=data["password"]
        )

    with allure.step("Submit registration"):
        reg.submit()

    with allure.step("Verify success"):
        page.wait_for_url("**status=success**")
        assert "status=success" in page.url

    with allure.step("Login with new account"):
        login.go_to_login()
        login.login(data["email"], data["password"])