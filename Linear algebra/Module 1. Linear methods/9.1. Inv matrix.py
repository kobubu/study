'''
Дана матрица :

A = np.array([[8, 6, 11], [7, 5, 9],[6, 10, 6]])
Найдите матрицу, обратную матрице .

В качестве ответа запишите элемент из первого столбца второй строки, округлив его до трёх знаков после точки-разделителя.

'''
import numpy as np


A = np.array([[8, 6, 11], [7, 5, 9],[6, 10, 6]])

print(np.linalg.inv(A))
print(round(np.linalg.inv(A)[1,0],3))
# 3