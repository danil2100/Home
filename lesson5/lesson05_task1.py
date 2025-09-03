from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# Настройка драйвера Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждём немного, чтобы страница загрузилась
    time.sleep(2)

    # Найти синюю кнопку по классу или тексту
    blue_button = driver.find_element(
        By.XPATH,
        "//button[contains(@class, 'btn-primary') or text()='Button Primary']",
    )

    # Кликнуть по кнопке
    blue_button.click()

    # Ждём, чтобы увидеть результат
    time.sleep(3)

    print("Кнопка успешно нажата!")

finally:
    # Закрыть браузер
    driver.quit()
