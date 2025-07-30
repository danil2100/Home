from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/textinput")
    print("Страница загружена")

    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

    input_field.send_keys("SkyPro")
    print("Введён текст: SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

    button.click()
    print("Кнопка нажата")

    button_text = button.text.strip()

    print("Текст на кнопке:")
    print(f'"{button_text}"')

    expected = "SkyPro"
    if button_text == expected:
        print("Текст совпадает с ожидаемым.")
    else:
        print("Текст не совпадает!")
        print(f"Ожидалось: '{expected}'")
        print(f"Получено:  '{button_text}'")

finally:
    driver.quit()
    print("Браузер закрыт")