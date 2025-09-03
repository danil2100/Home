import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import allure


@pytest.fixture
def driver():
    service = Service("msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
