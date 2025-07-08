def month_to_season(month):
    """Возвращает название сезона по номеру месяца."""
    if not isinstance(month, int) or month < 1 or month > 12:
        return 'Неверный номер месяца'

    if 1 <= month <= 2 or month == 12:
        return 'зима'
    elif 3 <= month <= 5:
        return 'весна'
    elif 6 <= month <= 8:
        return 'лето'
    elif 9 <= month <= 11:
        return 'осень'


print(month_to_season(2))  # Должно вернуть "зима"
