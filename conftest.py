import pytest
import allure
from utils.allure_utils import attach_screenshot


@pytest.fixture(scope="function")
def page():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page", None)

        if page:
            attach_screenshot(page, "Failure Screenshot")

            allure.attach(
                page.url,
                name="Failed URL",
                attachment_type=allure.attachment_type.TEXT
            )