from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    print("Страница загружается")

    WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "img[src]")) == 4
    )

    images = driver.find_elements(By.CSS_SELECTOR, "img[src]")

    third_image_src = images[2].get_attribute("src")

    print("Загрузка завершена. Значение атрибута src у 3-й картинки:")
    print(f'"{third_image_src}"')

finally:
    driver.quit()
    print("Браузер закрыт")