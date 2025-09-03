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
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )

    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    print("Логин и пароль введены")

    login_button.click()
    print("Кнопка Login нажата")

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )

    message_text = success_message.text.strip()
    if "×" in message_text:
        message_text = message_text.split("×")[-1].strip()  # Убираем крестик

    print("Текст с зелёной плашки:")
    print(f'"{message_text}"')

    input("\nНажмите Enter, чтобы закрыть браузер")

finally:
    driver.quit()
    print("Браузер закрыт")
