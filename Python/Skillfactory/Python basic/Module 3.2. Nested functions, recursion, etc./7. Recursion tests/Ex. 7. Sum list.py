'''
Другая важная операция в нейронных сетях — это суммирование элементов исходной матрицы.
Напишите функцию sum_list(). Она принимает на вход вложенный список, элементами которого являются числа, и возвращает сумму всех элементов.
Примеры вызова функции:
matrix = [
    [1, 1, 0],
    [4, 2, 1],
    [0, 2, 1]
]
print(sum_list(matrix))
## 12
matrix = [
    [1, 1, [1, 2, 3], 0],
    [4, 2, 1, [10, 52, 2]],
    [0, 2, 1]
]
print(sum_list(matrix))
## 82
'''
def sum_list(matrix):
    result = 0
    for elem in matrix:
        if type(elem) == list:
            result += sum_list(elem)
        else:
            result += elem
    return  result
matrix = [
    [1, 1, [1, 2, 3], 0],
    [4, 2, 1, [10, 52, 2]],
    [0, 2, 1]
]
print(sum_list(matrix))
#82

