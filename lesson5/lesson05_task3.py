from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    input_field.send_keys("Sky")
    print("Ввели: Sky")

    input_field.clear()
    print("Поле очищено")

    input_field.send_keys("Pro")
    print("Ввели: Pro")

    input("Нажмите Enter, чтобы закрыть браузер")

finally:
    driver.quit()
    print("Браузер закрыт")
