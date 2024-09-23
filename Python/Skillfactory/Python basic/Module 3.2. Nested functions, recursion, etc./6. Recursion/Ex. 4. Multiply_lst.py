'''
Напишите рекурсивную функцию multiply_lst(lst), которая перемножает элементы заданного списка lst между собой.
Если в функцию передаётся пустой список, она должна возвращать 1.
Примеры вызова функции:
print(multiply_lst([1, 5, 2, 1.5]))
## 15
print(multiply_lst([]))
## 1
'''

def multiply_lst(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * multiply_lst(lst[1:])

print(multiply_lst([1, 5, 2, 1.5]))



