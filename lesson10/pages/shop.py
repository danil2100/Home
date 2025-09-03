from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SaucedemoPage:
    """
    Page Object для https://www.saucedemo.com/
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """Открывает страницу."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Логин + ожидание загрузки каталога."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        # Ждём появления хотя бы одного товара
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

    def add_item_to_cart(self, item_name: str) -> None:
        """Добавляет товар в корзину по имени."""
        add_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='inventory_item_name'][text()='{item_name}']"
                    f"/ancestor::div[@class='inventory_item']"
                    f"//button[text()='Add to cart']",
                )
            )
        )
        add_button.click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()

    def get_total_price(self) -> str:
        """Возвращает итоговую сумму из корзины."""
        total = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text.strip()
