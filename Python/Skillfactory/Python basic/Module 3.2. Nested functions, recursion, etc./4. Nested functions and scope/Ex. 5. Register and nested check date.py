'''

Нам остался финальный штрих — добавить проверку даты на корректность в функцию для регистрации!
Модифицируйте функцию register() так, чтобы она выбрасывала исключение ValueError("Invalid Date!"), если введённая пользователем дата является некорректной. Для этого вам пригодится функция check_date() из предыдущего задания — вы можете добавить её в функцию register() или сделать независимой, на ваш вкус.

Главное — не забудьте добавить её объявление при отправке кода на проверку.

Пример вызова функции:


reg = register('Petrova', 'Maria', '13.03.2003', 'Ivanovna')
reg = register('Ivanov', 'Sergej', '24.09.1995', registry=reg)
reg = register('Smith', 'John', '13.02.2003', registry=reg)
print(reg)
## [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]

reg = register('Ivanov', 'Sergej', '24.13.1995')
## ValueError: Invalid Date!
'''

# Функция для регистрации пользователей
def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):
        # Разделяем строку по символу точки
        day, month, year = date.split('.')
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        return day, month, year
    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)
    if check_date(day, month, year) == False:
        raise ValueError("Invalid Date!")
    # Добавляем данные в список
    registry.append((surname, name, middle_name, day, month, year))
    return registry

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

