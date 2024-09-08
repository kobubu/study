'''
Напишите программу, которая находит произведение элементов списка num_list.
В качестве начального значения произведения задайте 1.
Далее в цикле перебирайте элементы списка num_list и умножайте значение произведения на элемент списка.

Результирующее произведение занесите в переменную p.
'''
from functools import  reduce

num_list = [1,2,3,4,5]
p = reduce(lambda  x, y: x * y, num_list, 1)
print(p)

//alternative

import math

num_list = [1, 2, 3, 4, 5]

# Используем функцию math.prod для нахождения произведения элементов списка
product_result = math.prod(num_list)

print(product_result)  # Вывод: 120


