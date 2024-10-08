'''
Напишите код, который определяет, является ли вложенный список test_matrix квадратной матрицей (то есть матрицей, у которой количество строк равно количеству столбцов).

Примеры квадратной и неквадратной (прямоугольной) матрицы: слева — квадратная, справа — неквадратная.
'''


matrix = [[1, 2, 3], [2, 3, 4], [4, 4, 5]]

is_square = True

for row in test_matrix:
    if len(row) != len(test_matrix):
        is_square = False
        break

is_square = all(len(row) == len(test_matrix) for row in test_matrix)
