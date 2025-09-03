import allure
import pytest
from selenium.webdriver.common.by import By
from pages.slow_calculator_page import SlowCalculatorPage


@pytest.fixture
def page(driver):
    page = SlowCalculatorPage(driver)
    page.open()
    return page


@allure.feature("Calculator Testing")
@allure.story("Slow Calculator Addition")
@allure.title("Проверка сложения 7 + 8 с задержкой")
@allure.description(
    "Тест устанавливает задержку 4 секунды, выполняет операцию 7 + 8 = "
    "и проверяет, что результат появляется через указанное время."
)
@allure.severity(allure.severity_level.NORMAL)
def test_addition(page):
    with allure.step("Установка задержки в 4 секунды"):
        page.set_delay(4)

    with allure.step("Выполнение: 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Ожидание появления результата '15'"):
        page.wait_for_result("15")

    with allure.step("Проверка, что результат равен '15'"):
        result = page.driver.find_element(By.CLASS_NAME, "screen").text.strip()
        assert result == "15", f"Ожидалось '15', получено '{result}'"

    with allure.step("Прикрепление финального скриншота"):
        allure.attach(
            page.driver.get_screenshot_as_png(),
            name="final_result_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
