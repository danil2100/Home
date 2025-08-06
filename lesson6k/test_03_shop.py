from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


def test_saucedemo_total_price():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/../../..//button").click()
        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/../../..//button").click()
        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']/../../..//button").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])

        assert total_value == 58.29, f"Ожидалось $58.29, получено ${total_value}"

    finally:
        driver.quit()