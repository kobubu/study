import re

def find_min_max(input_string):
    # Преобразуем строку в список, разделяя по пробелам
    elements = input_string.split()

    # Заменяем запятые на точки для корректного преобразования в числа
    elements = [el.replace(',', '.') for el in elements]

    # Фильтруем только числа, используя регулярное выражение
    numbers = []
    for el in elements:
        if re.match(r'^-?\d+(\.\d+)?$', el):
            try:
                numbers.append(float(el))
            except ValueError:
                continue

    # Если нет чисел, возвращаем сообщение об ошибке
    if not numbers:
        return "Некорректный ввод"

    # Находим минимум и максимум
    min_num = min(numbers)
    max_num = max(numbers)

    return f"Minimum: {min_num}\nMaximum: {max_num}"


# Ввод данных от пользователя
input_string = input('Введите последовательность чисел: ')

# Вызов функции и вывод результата
result = find_min_max(input_string)
print(result)
