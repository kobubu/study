'''
Пользователь с клавиатуры (через функцию input()) вводит через запятую и пробел
 две последовательности чисел (некоторые идентификаторы товаров/услуг, просмотренных клиентом 'A' и клиентом 'B' на платформе «Авито»).
Необходимо конвертировать каждый ввод пользователя в отдельный список, состоящий из целых чисел, а также составить новый список, состоящий из элементов пересечения двух исходных. Дубликаты необходимо удалить, а результирующий список — вывести на экран.
Важно! Если пересечение пустое, то на экран должен выводиться пустой список.
Если ввод пользователя невозможно конвертировать в список из целых чисел, возникает ошибка. Необходимо отлавливать эту ошибку и выводить на экран фразу Некорректный ввод.
Для поиска пересечений в списках напишите функцию pure_intersection(), которая будет возвращать список с уникальными элементами пересечения.

Ввод:
108, 138, 42, 52, 14
109, 13, 52, 32, 42, 14, 109
Вывод:
[42, 52, 14]
Пример №2:
Ввод:
108, 138, 42, 52, 14
189, 202, 249, 24, 15, 3
Вывод:
[]
Пример №3:

Ввод:
108, 138, 42, 52, четырнадцать
189, 202, 249, 24, 15, 3

Вывод:
Некорректный ввод'''

'''
Пользователь с клавиатуры (через функцию input()) вводит через запятую и пробел
 две последовательности чисел (некоторые идентификаторы товаров/услуг, просмотренных клиентом 'A' и клиентом 'B' на платформе «Авито»).
Необходимо конвертировать каждый ввод пользователя в отдельный список, состоящий из целых чисел, а также составить новый список, состоящий из элементов пересечения двух исходных. Дубликаты необходимо удалить, а результирующий список — вывести на экран.
Важно! Если пересечение пустое, то на экран должен выводиться пустой список.
Если ввод пользователя невозможно конвертировать в список из целых чисел, возникает ошибка. Необходимо отлавливать эту ошибку и выводить на экран фразу Некорректный ввод.
Для поиска пересечений в списках напишите функцию pure_intersection(), которая будет возвращать список с уникальными элементами пересечения.

Ввод:
108, 138, 42, 52, 14
109, 13, 52, 32, 42, 14, 109
Вывод:
[42, 52, 14]
Пример №2:
Ввод:
108, 138, 42, 52, 14
189, 202, 249, 24, 15, 3
Вывод:
[]
Пример №3:

Ввод:
108, 138, 42, 52, четырнадцать
189, 202, 249, 24, 15, 3

Вывод:
Некорректный ввод'''

input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')
# ваш код здесь
input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')

# ваш код здесь
# Определяем функцию для нахождения пересечения двух списков
def pure_intersection(lst1, lst2):
    # Преобразуем строки в списки целых чисел
    lst1 = list(map(int, lst1.split(', ')))
    lst2 = list(map(int, lst2.split(', ')))

    # Находим пересечение двух множеств, созданных из списков
    intersection = set(lst1) & set(lst2)

    # Возвращаем список уникальных элементов пересечения
    return list(intersection)


# Пытаемся выполнить код, обрабатывая возможные ошибки
try:
    # Вызываем функцию pure_intersection с введенными пользователем данными
    result = pure_intersection(input_string1, input_string2)

    # Выводим результат
    print(result)

# Если возникает ошибка преобразования строки в целое число (некорректный ввод)
except ValueError:
    # Выводим сообщение об ошибке
    print('Некорректный ввод')
