'''
Напишите функцию even_numbers_in_matrix(), которая получает на вход матрицу (список из списков) matrix и возвращает количество чётных чисел в ней.
Гарантируется, что все элементы в матрице matrix являются числами.
Пример работы программы:
matrix_example = [
    [1, 5, 4],
    [4, 2, -2],
    [7, 65, 88]
]
print(even_numbers_in_matrix(matrix=matrix_example))
# 5
'''

def even_numbers_in_matrix(matrix):
    # Преобразуем список списков в один список
    flat_list = [number for row in matrix for number in row]
    even_numbers = [number for number in flat_list if number % 2 == 0]
    return len(even_numbers)




