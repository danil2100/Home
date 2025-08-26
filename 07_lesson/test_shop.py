import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()


def test_checkout_total_price(driver):
    # Экземпляры Page Object
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Шаг 1: Открыть сайт и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавить товары в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # Шаг 3: Перейти в корзину
    inventory_page.go_to_cart()

    # Шаг 4: Нажать Checkout
    cart_page.click_checkout()

    # Шаг 5: Заполнить форму
    checkout_page.enter_first_name("Даниил")
    checkout_page.enter_last_name("Чекмарев")
    checkout_page.enter_postal_code("490000")
    checkout_page.continue_checkout()

    # Шаг 6: Получить итоговую стоимость
    total_text = checkout_page.get_total_price()

    # Извлекаем сумму
    total_amount = float(total_text.split("$")[1])

    # Проверка
    assert (
        total_amount == 58.29
    ), f"Ожидалось $58.29, но получено ${total_amount}"
