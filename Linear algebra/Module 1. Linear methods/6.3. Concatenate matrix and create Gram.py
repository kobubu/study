'''
Дана система векторов:
x = np.array([1,2,1,0,4])
y = np.array([2,1,-1,1,0])
z = np.array([-1,1,-1,0,0])

Составьте матрицу A, расположив векторы x, y, z в строках.
Найдите матрицу Грама B (матрицу скалярных произведений столбцов матрицы ) системы векторов.

Чему равна полученная матрица Грама ?
'''
import numpy as np
x = np.array([1,2,1,0,4])
y = np.array([2,1,-1,1,0])
z = np.array([-1,1,-1,0,0])
A = np.vstack((x, y, z))
print(A)
B = np.transpose(A)
print(B)
print(B@A)
