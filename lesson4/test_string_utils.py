import pytest
from string_utils import StringUtils

utils = StringUtils()


# Позитивные тесты для метода capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),              # базовый случай
    ("Skypro", "Skypro"),              # уже заглавная
    ("привет", "Привет"),              # кириллица
    ("a", "A"),                        # один символ
    ("word with spaces", "Word with spaces")  # несколько слов
], ids=["basic", "already_capitalized", "unicode", "single_char", "multi_word"])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected

# Негативные тесты для метода capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                          # пустая строка
    (" ", " "),                        # пробел
    ("123", "123"),                   # только цифры
    ("$test", "$test"),               # спецсимволы
    ("1test1test", "1test1test")       # строка с цифрами
], ids=["empty", "space", "numbers", "special_chars", "numbered_string"])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


# Позитивные тесты для метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),           # пробелы в начале
    ("skypro   ", "skypro"),           # пробелы в конце
    ("   a   ", "a"),                 # пробелы с двух сторон
    ("a", "a"),                       # один символ
    (" word with spaces ", "word with spaces")  # пробелы до и после
], ids=["leading", "trailing", "both_sides", "single_char", "with_spaces"])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected

# Негативные тесты для метода trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                          # пустая строка
    (" ", ""),                         # только пробел
    ("$test", "$test"),               # спецсимволы
    ("123", "123"),                   # только цифры
    ("   ", "")                        # строка из пробелов
], ids=["empty", "single_space", "special_chars", "numbers", "spaces_only"])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


# Позитивные тесты для метода contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "S"),
    ("Hello", "e"),
    ("Привет", "р"),
    ("123", "2"),
    ("$test$", "$")
], ids=["basic", "middle", "unicode", "number", "special_char"])
def test_contains_positive(input_str, symbol):
    assert utils.contains(input_str, symbol) is True

# Негативные тесты для метода contains

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "U"),
    ("Hello", "z"),
    ("", "a"),
    ("123", "a"),
    ("$test$", "q")
], ids=["missing_char", "not_in_string", "empty", "char_not_in_numbers", "char_not_in_specials"])
def test_contains_negative(input_str, symbol):
    assert utils.contains(input_str, symbol) is False


# Позитивные тесты для метода delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),         # удаление буквы
    ("Hello", "e", "Hllo"),           # удаление внутри строки
    ("Привет", "р", "Пивет"),         # удаление кириллической буквы
    ("123", "2", "13"),              # удаление цифры
    ("$test$", "$", "test")           # удаление спецсимвола
], ids=["delete_letter", "delete_middle", "delete_unicode", "delete_number", "delete_special"])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected

# Негативные тесты для метода delete_symbol

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),        # несуществующий символ
    ("Hello", "Z", "Hello"),          # символа нет в строке
    ("", "a", ""),                    # пустая строка
    ("123", "a", "123"),            # символ не входит в строку
    ("$test$", "q", "$test$")        # символ отсутствует
], ids=["no_match", "not_found", "empty", "no_char_in_numbers", "no_char_in_specials"])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected