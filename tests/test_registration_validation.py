import allure
import time
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.test_data import TestData

@allure.title("Registration with invalid email")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Registration Validation")
def test_invalid_email_registration(page):

    login = LoginPage(page)
    reg = RegistrationPage(page)

    page.goto(TestData.BASE_URL)
    page.wait_for_load_state("networkidle")

    login.go_to_login()
    login.go_to_registration()

    reg.select_candidate()

    data = TestData.generate_invalid_user()

    reg.enter_candidate_details(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )

    reg.submit()
    page.wait_for_timeout(2000)

    error_locator = page.locator("text=/email|invalid|valid email|format/i")

    error_text = ""
    if error_locator.count() > 0:
        error_text = error_locator.first.inner_text().lower()

    if error_text == "":
        error_text = page.evaluate("""
            () => {
                const el = document.querySelector("input[type='email']");
                return el ? el.validationMessage : "";
            }
        """).lower()

    assert (
        "email" in error_text or
        "invalid" in error_text or
        "valid email" in error_text or
        "format" in error_text
    )

    assert "status=success" not in page.url






@allure.title("Registration with invalid email")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Registration Validation")
def test_invalid_email_registration(page):
 
    login = LoginPage(page)
    reg = RegistrationPage(page)
 
    page.goto(TestData.BASE_URL)
    page.wait_for_load_state("networkidle")
 
    login.go_to_login()
    login.go_to_registration()
 
    reg.select_candidate()
 
    data = TestData.generate_invalid_user()
 
    reg.enter_candidate_details(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
 
    reg.submit()
    page.wait_for_timeout(2000)
 
    error_locator = page.locator("text=/email|invalid|valid email|format/i")
 
    error_text = ""
    if error_locator.count() > 0:
        error_text = error_locator.first.inner_text().lower()
 
    if error_text == "":
        error_text = page.evaluate("""
            () => {
                const el = document.querySelector("input[type='email']");
                return el ? el.validationMessage : "";
            }
        """).lower()
 
    assert (
        "email" in error_text or
        "invalid" in error_text or
        "valid email" in error_text or
        "format" in error_text
    )
 
    assert "status=success" not in page.url
 
 
@allure.title("Registration - Blank fields submit")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Registration Validation")
def test_registration_blank_fields(page):
 
    login = LoginPage(page)
    reg = RegistrationPage(page)
 
    with allure.step("Navigate to application"):
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
 
    with allure.step("Go to registration page"):
        login.go_to_login()
        login.go_to_registration()
 
    with allure.step("Select candidate type"):
        reg.select_candidate()
 
    with allure.step("Wait for form to load"):
        page.wait_for_selector("//input[@id='username']")
 
    with allure.step("Submit form without filling any field"):
        reg.submit()
 
    with allure.step("Verify form did not proceed to success"):
        page.wait_for_timeout(2000)
        assert "status=success" not in page.url, (
            "Form should not submit successfully with blank fields"
        )
 
    with allure.step("Verify validation error is present"):
        body_text = page.locator("body").inner_text().lower()
        has_error = (
            "required" in body_text or
            "field"    in body_text or
            "empty"    in body_text or
            "fill"     in body_text
        )
 
        assert has_error, (
            "Expected validation error for blank fields, but none found"
        )
 
 
@allure.title("Registration - Password mismatch")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Registration Validation")
def test_registration_password_mismatch(page):
 
    login = LoginPage(page)
 
    with allure.step("Navigate to application"):
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
 
    with allure.step("Go to registration page"):
        login.go_to_login()
        login.go_to_registration()
 
    with allure.step("Select candidate type"):
        page.wait_for_selector(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Candidate']]"
        )
        page.click(
            "//div[contains(@class,'jet-button__state') and .//span[normalize-space()='Candidate']]"
        )
 
    with allure.step("Fill form with mismatched passwords"):
        ts = int(time.time())
        page.wait_for_selector("//input[@id='username']")
 
        page.fill("//input[@id='username']", f"user_{ts}")
        page.fill("//input[@id='email']",    f"user_{ts}@gmail.com")
 
        page.fill("//input[@id='password']",  "Password123")
        page.fill("//input[@id='conf-pass']", "DifferentPass456")
 
    with allure.step("Submit the form"):
        page.click("//button[contains(@class,'submit')]")
 
    with allure.step("Verify password mismatch error"):
        page.wait_for_timeout(2000)
 
        assert "status=success" not in page.url, (
            "Registration should not succeed with mismatched passwords"
        )
 
        body_text = page.locator("body").inner_text().lower()
        has_error = (
            "match"    in body_text or
            "mismatch" in body_text or
            "password" in body_text or
            "same"     in body_text or
            "confirm"  in body_text
        )
 
        assert has_error, f"Expected password mismatch error, but got: {body_text[:200]}"
 
 
@allure.title("Registration - Too short password")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Registration Validation")
def test_registration_short_password(page):
 
    login = LoginPage(page)
    reg = RegistrationPage(page)
 
    with allure.step("Navigate to application"):
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
 
    with allure.step("Go to registration page"):
        login.go_to_login()
        login.go_to_registration()
 
    with allure.step("Select candidate type"):
        reg.select_candidate()
 
    with allure.step("Fill form with too short password (3 chars)"):
        ts = int(time.time())
        page.wait_for_selector("//input[@id='username']")
 
        page.fill("//input[@id='username']", f"user_{ts}")
        page.fill("//input[@id='email']",    f"user_{ts}@gmail.com")
 
        page.fill("//input[@id='password']",  "123")
        page.fill("//input[@id='conf-pass']", "123")
 
    with allure.step("Submit the form"):
        reg.submit()
 
    with allure.step("Verify short password error"):
        page.wait_for_timeout(2000)
 
        assert "status=success" not in page.url, (
            "Registration should not succeed with too short password"
        )
 
        body_text = page.locator("body").inner_text().lower()
        has_error = (
            "short"     in body_text or
            "minimum"   in body_text or
            "least"     in body_text or
            "character" in body_text or
            "length"    in body_text
        )
 
        assert has_error, (
            "Expected short password validation error, but none found"
        )
 
 
@allure.title("Recruiter Registration - Invalid phone number")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authentication")
@allure.story("Recruiter Registration Validation")
def test_recruiter_invalid_phone(page):
 
    login = LoginPage(page)
    reg = RegistrationPage(page)
 
    with allure.step("Navigate to application"):
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
 
    with allure.step("Go to registration page"):
        login.go_to_login()
        login.go_to_registration()
 
    with allure.step("Select recruiter type"):
        reg.select_recruiter()
 
    with allure.step("Fill recruiter form with invalid phone"):
        ts = int(time.time())
        page.wait_for_selector("//input[@id='_recruiter-company-name']")
 
        page.fill("//input[@id='_recruiter-company-name']", f"Company_{ts}")
        page.fill("//input[@id='_recruiter-email']",        f"recruiter_{ts}@gmail.com")
 
        page.fill("//input[contains(@class,'phone-class')]", "abcde")
 
        page.fill("//input[@id='password']",         "12345678")
        page.fill("//input[@id='confirm-password']", "12345678")
 
    with allure.step("Submit the form"):
        reg.submit()
 
    with allure.step("Verify phone validation error"):
        page.wait_for_timeout(2000)
 
        assert "status=success" not in page.url, (
            "Registration should not succeed with invalid phone number"
        )
 
        body_text = page.locator("body").inner_text().lower()
        has_error = (
            "phone"   in body_text or
            "number"  in body_text or
            "invalid" in body_text or
            "valid"   in body_text or
            "format"  in body_text
        )
 
        assert has_error, f"Expected phone validation error, but got: {body_text[:200]}"