'''
Даны 2 матрицы
A = np.array([[1,9,8,5], [3,6,3,2], [3,3,3,3], [0,2,5,9], [4,4,1,2]])
B = np.array([[1,-1,0,1,1], [-2,0,2,-1,1]])
Найдите произведение матриц A и B в том порядке, в котором их можно умножить.

В качестве ответа через запятую, без пробелов запишите элемент чётвертого столбца первой строки.
'''
import numpy as np
A = np.array([[1,9,8,5], [3,6,3,2], [3,3,3,3], [0,2,5,9], [4,4,1,2]])
B = np.array([[1,-1,0,1,1], [-2,0,2,-1,1]])
print(np.dot(B,A))
#Out: [[  2   9  11  14] [  8 -10 -14 -11]]