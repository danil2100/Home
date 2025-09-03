# Автотесты с Selenium и Allure

Этот проект содержит автоматизированные тесты для трёх веб-страниц:

1. **Форма данных** — [https://bonigarcia.dev/selenium-webdriver-java/data-types.html](https://bonigarcia.dev/selenium-webdriver-java/data-types.html)
2. **Медленный калькулятор** — [https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
3. **Интернет-магазин saucedemo** — [https://www.saucedemo.com/](https://www.saucedemo.com/)

Тесты написаны с использованием:
- **Selenium WebDriver** — для взаимодействия с браузером
- **pytest** — как фреймворк
- **Allure** — для генерации отчёта
- **Page Object Model (POM)** — для чистоты и поддержки кода

## Установка зависимостей

Убедитесь, что у вас установлен Python (версия 3.8+), затем выполните:

```bash
pip install selenium pytest allure-pytest webdriver-manager



---

### Что сделано:

| Задача | Готово |
| Все тесты работают | Да |
| Используется Allure | Да |
| Разметка шагов и проверок | Да |
| Декораторы: `@allure.title`, `feature`, `severity` | Да |
| Page Object для всех страниц | Да |
| Инструкция по запуску и просмотру отчёта | Да |
| `.gitignore` и что не пушить | Да |