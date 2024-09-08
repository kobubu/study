'''
Вам задан список num_list, состоящий из чисел (int и float) например:
num_list = [1, 10, 3, -5].
Отсортируйте его с помощью метода sort() для списков,
а затем последовательно выведите на экран элементы этого списка с помощью цикла for в следующем формате:
"element {i}: {elem}", где i - индекс элемента в списке, elem - элемент.
'''

num_list = [1, 10, 3, -5]

[print(f"element {i}: {elem}") for i, elem in enumerate(sorted(num_list))]


//alternative

num_list.sort() or [print(f"element {i}: {elem}") for i, elem in enumerate(num_list)]
