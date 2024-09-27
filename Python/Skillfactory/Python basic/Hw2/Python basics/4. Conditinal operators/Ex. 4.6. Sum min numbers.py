'''
Усложним предыдущую задачу.
Напишите функцию sum_min_numbers(), которая также принимает на вход три числа (a, b, c) и возвращает сумму двух наименьших.
Можно использовать функцию find_min_number() из предыдущего задания для поиска минимального числа.
Примеры работы программы:
print(sum_min_numbers(1, 2, 3))
# 3
print(sum_min_numbers(1, 2, -10))
# -9
'''


def sum_min_numbers(a, b, c):
    numbers = a,b,c
    return  sum(numbers)-max(numbers)




