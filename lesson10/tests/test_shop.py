import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("E-commerce Testing")
@allure.story("Checkout Process")
@allure.title("Проверка итоговой суммы при оформлении заказа")
@allure.description(
    "Тест добавляет 3 товара, заполняет данные и проверяет финальную сумму."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_total_price(driver):
    with allure.step("Открытие страницы"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизация"):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    with allure.step("Добавление товаров в корзину"):
        driver.find_element(
            By.XPATH, "//div[text()='Sauce Labs Backpack']/../../..//button"
        ).click()
        driver.find_element(
            By.XPATH,
            "//div[text()='Sauce Labs Bolt T-Shirt']/../../..//button",
        ).click()
        driver.find_element(
            By.XPATH, "//div[text()='Sauce Labs Onesie']/../../..//button"
        ).click()

    with allure.step("Переход в корзину и оформление заказа"):
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

    with allure.step("Заполнение данных покупателя"):
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

    with allure.step("Проверка итоговой суммы"):
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])
        assert (
            total_value == 58.29
        ), f"Ожидалось $58.29, получено ${total_value}"

    with allure.step("Прикрепление финального скриншота"):
        allure.attach(
            driver.get_screenshot_as_png(),
            name="final_order_summary",
            attachment_type=allure.attachment_type.PNG,
        )
