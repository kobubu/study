'''
Напишите функцию get_less(list_in, num), которая принимает на вход список list_in, состоящий из чисел, и ещё одно число num.

Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. Если такого числа нет, необходимо вернуть None.
'''

# Введите свое решение ниже
list_in = [4,3, 3,4, 5, 6, 2,5]
num = 3

def get_less(list_in, num):
    for x in list_in:
        if x < num:
            return x

def get_less(list_in, num):
    return  [x for x in list_in if x < num]
