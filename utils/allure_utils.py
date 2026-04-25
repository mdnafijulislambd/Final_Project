import allure

def attach_screenshot(page, name="Screenshot"):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

def attach_text(text, name="Log"):
    allure.attach(
        text,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )