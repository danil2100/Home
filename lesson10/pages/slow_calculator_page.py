from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой.
    URL: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку в поле #delay."""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text: str) -> None:
        """Нажимает кнопку по тексту (например, '7', '+', '=')"""
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()

    def wait_for_result(self, expected: str) -> None:
        """Ждёт, пока результат в поле .screen не станет равным ожидаемому значению."""
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected
            )
        )
