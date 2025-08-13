import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Page_Object_cal import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open_page()

    # Установить задержку 45 секунд
    calc_page.set_delay("45")

    # Нажать кнопки: 7 + 8 =
    calc_page.press_7()
    calc_page.press_add()
    calc_page.press_8()
    calc_page.press_equals()

    # Явное ожидание
    wait = WebDriverWait(driver, 60)
    wait.until(
        lambda d: d.find_element(By.CSS_SELECTOR, ".screen")
        .get_attribute("textContent")
        .strip()
        == "15"
    )

    # Проверка
    result = (
        driver.find_element(By.CSS_SELECTOR, ".screen")
        .get_attribute("textContent")
        .strip()
    )
    assert result == "15", f"Ожидалось '15', но получено: '{result}'"
