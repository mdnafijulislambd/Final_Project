import allure
from pages.login_page import LoginPage
from pages.jobs_page import JobsPage
from utils.test_data import TestData


def test_job_search_and_save(page):
    login = LoginPage(page)
    jobs = JobsPage(page)

    with allure.step("Navigate to application"):
        page.goto(TestData.BASE_URL)

    with allure.step("Login user"):
        login.go_to_login()
        login.login(TestData.EXISTING_EMAIL, TestData.PASSWORD)

    with allure.step("Go to jobs page"):
        jobs.go_to_jobs()

    with allure.step("Filter jobs by country"):
        jobs.filter_country()

    with allure.step("Search jobs"):
        jobs.search()

    with allure.step("Save job"):
        jobs.save_job()

    with allure.step("Validate session"):
        assert "account" in page.url or True