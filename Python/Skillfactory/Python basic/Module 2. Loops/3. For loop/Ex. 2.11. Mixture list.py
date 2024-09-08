'''

Дан список mixture_list, элементами которого могут являться любые типы данных Python. Например:


mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
С помощью цикла for посчитайте количество элементов типа str в списке. Результат запишите в переменную count_str.
'''

mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
count_str = sum(1 for x in mixture_list if isinstance(x, str))

print(count_str)
