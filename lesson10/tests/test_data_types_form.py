import allure
import pytest
from pages.data_types_page import DataTypesPage


@allure.feature("Form Testing")
@allure.story("Data Types Form Validation")
@pytest.fixture
def page(driver):
    page = DataTypesPage(driver)
    page.open()
    return page


@allure.title("Проверка подсветки полей формы")
@allure.description("Тест заполняет форму и проверяет цвет подсветки полей.")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_field_highlights(page):
    with allure.step("Заполнение всех полей формы (кроме zip-code)"):
        page.fill_first_name("Иван")
        page.fill_last_name("Петров")
        page.fill_address("Ленина, 55-3")
        page.fill_city("Москва")
        page.fill_country("Россия")
        page.fill_email("test@skypro.com")
        page.fill_phone("+7985899998787")
        page.fill_job_position("QA")
        page.fill_company("SkyPro")

    with allure.step("Отправка формы"):
        page.submit_form()

    with allure.step("Проверка подсветки"):
        assert "alert-danger" in page.get_field_class(
            "zip-code"
        ), "Zip code должен быть красным"
        assert (
            len(page.get_highlighted_fields()) == 9
        ), "Ожидалось 9 зелёных полей"
