import pytest
from string_utils import StringUtils

utils = StringUtils()


# Тесты для метода capitalize
def test_capitalize():
    assert utils.capitalize("skypro") == "Skypro"  # Позитивный сценарий
    assert utils.capitalize("") == ""              # Негативный сценарий: пустая строка
    assert utils.capitalize(" ") == " "            # Негативный сценарий: строка с пробелом


# Тесты для метода trim
def test_trim():
    assert utils.trim("   skypro") == "skypro"     # Позитивный сценарий
    assert utils.trim("skypro") == "skypro"        # Негативный сценарий: уже обрезанная строка
    assert utils.trim("") == ""                    # Негативный сценарий: пустая строка


# Тесты для метода contains
def test_contains():
    assert utils.contains("SkyPro", "S") is True   # Позитивный сценарий
    assert utils.contains("SkyPro", "U") is False  # Негативный сценарий: отсутствующий символ


# Тесты для метода delete_symbol
def test_delete_symbol():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"   # Позитивный сценарий
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"  # Негативный сценарий: несуществующий символ
    assert utils.delete_symbol("", "k") == ""              # Негативный сценарий: пустая строка