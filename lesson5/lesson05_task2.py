from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Button with Dynamic ID']")
        )
    )

    button.click()

    print("Кнопка успешно нажата!")

    input("Нажмите Enter, чтобы закрыть браузер")

finally:
    driver.quit()
