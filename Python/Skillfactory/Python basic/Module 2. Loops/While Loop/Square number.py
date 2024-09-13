'''
Напишите цикл while, который находит минимальное натуральное число number, квадрат которого больше некоторого заданного value.

Результирующий ответ запишите в переменную number.
'''

## Введите свое решение ниже

import random

number = 0
value = random.randint(1, 36)

while number**2 <= value:
    number += 1

#alternative

number = math.ceil(math.sqrt(value))
