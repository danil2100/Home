from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/ajax")

    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    blue_button.click()
    print("Кнопка нажата. Ожидаем загрузку данных")

    green_box = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content p.bg-success"))
    )

    text = green_box.text.strip()

    print("Текст из зелёной плашки:")
    print(f'"{text}"')

    expected_text = "Data loaded with AJAX get request."
    if text == expected_text:
        print("Текст совпадает с ожидаемым.")
    else:
        print("Текст не совпадает!")
        print(f"Ожидалось: '{expected_text}'")
        print(f"Получено:  '{text}'")

finally:
    driver.quit()
    print("Браузер закрыт")