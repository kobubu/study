'''
Двумерные таблицы (матрицы) — основной формат данных, с которым мы будем работать.
Давайте рассмотрим операцию сложения двух матриц.
Напишите функцию matrix_sum(), которая получает на вход две матрицы (matrix1, matrix2) и возвращает их сумму.
Примечание. Чтобы сложить две матрицы, нужно просуммировать их соответствующие элементы.

1 2 3   2 3 4   1+2 2+3 3+4   3 5 7
2 3 4 + 4 5 6 = 2+4 3+5 4+6 = 6 8 10
5 6 7   4 3 2   5+4 6+3 7+2   9 9 9

Важно отметить, что суммировать можно только матрицы одинаковой размерности.
Поэтому сначала необходимо проверить, что размеры матриц совпадают,
то есть матрицы должны иметь равное количество строк, а в каждой строке должно быть равное количество элементов (столбцов).
Если размеры матриц не совпадают, необходимо вывести на экран сообщение "Error! Matrices dimensions are different!"
с помощью функции print(), а затем вернуть значение None из функции matrix_sum().
Гарантируется, что на вход подаются только прямоугольные матрицы (матрицы, в которых количество элементов в каждой из строк одинаково).
Примеры работы программы:
matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]
print(matrix_sum(matrix1=matrix_example, matrix2=matrix_example))
# [[2, 10, 8], [8, 4, -4], [14, 130, 176]]
matrix1_example = [
          [1, 5, 4],
          [4, 2, -2]
]
matrix2_example = [
          [10, 15, 43],
          [41, 2, -2],
          [7, 5, 7]
]
print(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# Error! Matrices dimensions are different!
# None
matrix1_example = [
          [1, 5, 4, 5],
          [4, 2, -2, -5],
          [4, 2, -2, -5]
]
matrix2_example = [
          [10, 15, 43],
          [41, 2, -2],
          [7, 5, 7]
]
print(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# Error! Matrices dimensions are different!
# None
'''

def matrix_sum(matrix1, matrix2):
    if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
        print("Error! Matrices dimensions are different!")
        return None
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [x + y for x, y in zip(row1, row2)]
        result.append(result_row)

    return result
