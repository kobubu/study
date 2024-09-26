'''
Напишите функцию check_duplicates(), которая проверит, есть ли дубликаты в списке lst, переданном ей в качестве аргумента.
Результатом работы функции должно стать булево число (True или False).
Примеры работы программы:

lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
print(check_duplicates(lst))
# True

lst = list(range(0, 15))
print(check_duplicates(lst))
# False
'''




check_duplicates=  lambda x: len(lst) != len(set(lst))

lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
print(check_duplicates(lst))
