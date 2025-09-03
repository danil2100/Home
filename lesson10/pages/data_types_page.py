from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List


class DataTypesPage:
    """
    Page Object для страницы https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"  # ⚠️ Убраны пробелы

    def open(self) -> None:
        """Открывает страницу."""
        self.driver.get(self.url)

    def fill_first_name(self, value: str) -> None:
        """Заполняет поле First name."""
        self.driver.find_element(By.NAME, "first-name").send_keys(value)

    def fill_last_name(self, value: str) -> None:
        """Заполняет поле Last name."""
        self.driver.find_element(By.NAME, "last-name").send_keys(value)

    def fill_address(self, value: str) -> None:
        """Заполняет поле Address."""
        self.driver.find_element(By.NAME, "address").send_keys(value)

    def fill_city(self, value: str) -> None:
        """Заполняет поле City."""
        self.driver.find_element(By.NAME, "city").send_keys(value)

    def fill_country(self, value: str) -> None:
        """Заполняет поле Country."""
        self.driver.find_element(By.NAME, "country").send_keys(value)

    def fill_email(self, value: str) -> None:
        """Заполняет поле E-mail."""
        self.driver.find_element(By.NAME, "e-mail").send_keys(value)

    def fill_phone(self, value: str) -> None:
        """Заполняет поле Phone number."""
        self.driver.find_element(By.NAME, "phone").send_keys(value)

    def fill_job_position(self, value: str) -> None:
        """Заполняет поле Job position."""
        self.driver.find_element(By.NAME, "job-position").send_keys(value)

    def fill_company(self, value: str) -> None:
        """Заполняет поле Company."""
        self.driver.find_element(By.NAME, "company").send_keys(value)

    def submit_form(self) -> None:
        """Нажимает кнопку Submit через JavaScript."""
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", submit_button
        )
        self.driver.execute_script("arguments[0].click();", submit_button)

    def get_field_class(self, field_id: str) -> str:
        """Возвращает значение атрибута class у поля по ID."""
        return self.driver.find_element(By.ID, field_id).get_attribute("class")

    def get_highlighted_fields(self) -> List[str]:
        """Возвращает список ID полей с зелёной подсветкой (alert-success)."""
        success_class = "alert-success"
        fields = [
            "first-name",
            "last-name",
            "address",
            "city",
            "country",
            "e-mail",
            "phone",
            "job-position",
            "company",
        ]
        return [
            field_id
            for field_id in fields
            if success_class in self.get_field_class(field_id)
        ]
