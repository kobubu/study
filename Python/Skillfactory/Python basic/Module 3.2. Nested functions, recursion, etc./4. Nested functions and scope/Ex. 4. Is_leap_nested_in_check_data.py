'''
Сделайте функцию is_leap() из предыдущего задания внутренней функцией функции check_date().
Модифицируйте код функции check_date() так, чтобы она корректно обрабатывала високосные года.
Пример работы функции:

print(check_date(18, 9, 1999))
# True
print(check_date(29, 2, 2000))
# True
print(check_date(29, 2, 2021))
# False
print(check_date(13, 13, 2021))
# False
print(check_date(13.5, 12, 2021))
# False
'''


# Функция для проверки корректности даты
def check_date(day, month, year):
    def is_leap(year):
        # Год является високосным, если он делится на 4, но не делится на 100,
        # либо делится на 400
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Проверяем день, месяц и год на целочисленность
    if not (isinstance(day, int) and isinstance(month, int) and isinstance(year, int)):
        return False

    # Проверяем год на заданный диапазон
    if year < 1900 or year > 2022:
        return False

    # Проверяем месяц на заданный диапазон
    if month < 1 or month > 12:
        return False

    # Проверяем день на заданный диапазон
    if day < 1 or day > 31:
        return False

    # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
    if month in [4, 6, 9, 11] and day > 30:
        return False

    # Проверяем количество дней в феврале
    if month == 2:
        if is_leap(year) and day > 29:
            return False
        elif not is_leap(year) and day > 28:
            return False

    return True


# Вызываем is_leap через check_date
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(year=2000))  # True
