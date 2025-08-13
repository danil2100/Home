from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, 50
        )  # Увеличено для ожидания результата

    # Локаторы
    def get_delay_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#delay")

    def get_button_7(self):
        return self.driver.find_element(By.XPATH, "//span[text()='7']")

    def get_button_8(self):
        return self.driver.find_element(By.XPATH, "//span[text()='8']")

    def get_button_add(self):
        return self.driver.find_element(By.XPATH, "//span[text()='+']")

    def get_button_equals(self):
        return self.driver.find_element(By.XPATH, "//span[text()='=']")

    def get_display(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen")

    # Методы
    def open_page(
        self,
        url="https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html",
    ):
        self.driver.get(url)

    def set_delay(self, seconds):
        delay_input = self.get_delay_input()
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_7(self):
        self.get_button_7().click()

    def press_8(self):
        self.get_button_8().click()

    def press_add(self):
        self.get_button_add().click()

    def press_equals(self):
        self.get_button_equals().click()

    def get_result(self):
        # Ожидаем, пока в дисплее появится "15"
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.get_display().get_attribute("textContent").strip()
