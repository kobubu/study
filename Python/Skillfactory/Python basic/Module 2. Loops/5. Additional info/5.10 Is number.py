'''
Дан словарь mixture_dict. Значения в нём могут быть трёх типов: строки (str) или числа (int и float).

Посчитайте, сколько значений в словаре mixture_dict являются числами. Результат занесите в переменную count_numbers. Используйте в своём коде оператор continue.
'''

mixture_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
count_numbers = 0

for key, value in mixture_dict.items():
    if isinstance(value, (int, float)):
        count_numbers += 1
    else:
        continue

print(count_numbers)
