'''

Дан список num_list, состоящий из целых чисел (int). Например:

num_list = list(range(0, 100, 3))
С помощью цикла for посчитайте количество чётных элементов в списке.
Результат запишите в переменную count_even.
'''

num_list = list(range(0, 100, 3))

count_even = sum(1 for x in num_list if x % 2 ==0)
