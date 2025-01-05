'''
Напишите функцию get_unique_loto(num). Она так же, как и функция в задании 10.10,
генерирует num полей для игры в лото, однако теперь на каждом поле 5х5 числа не могут повторяться.
Функция также должна возвращать массив формы num x 5 x 5.
'''

# Введите свое решение ниже
import numpy as np


def get_unique_loto(num):
    # Создаем пустой массив для хранения полей
    loto_array = np.zeros((num, 5, 5), dtype=int)

    # Генерируем каждое поле
    for i in range(num):
        # Генерируем 25 уникальных чисел от 1 до 100
        numbers = np.random.choice(np.arange(1, 101), size=25, replace=False)
        # Заполняем поле 5x5
        loto_array[i] = numbers.reshape(5, 5)

    return loto_array

