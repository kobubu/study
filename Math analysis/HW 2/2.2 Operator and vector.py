'''
Результат действия оператора на вектор  называют образом вектора.
a) Найдите образ вектора v [1, 2, 3] при действии оператора F [1, 0, 0], [0, 0, 1], [0, -1, 0], если

v =
'''


import numpy as np

v = np.array([1, 2, 3])
F = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])

print(v@F)