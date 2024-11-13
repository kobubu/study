import numpy as np


v1 = np.array([9, 10, 7, 7, 9])
v2 = np.array([2, 0, 5, 1, 4])
v3 = np.array([4, 0, 0, 4, 1])
v4 = np.array([3, -4, 3, -1, -4])
A = np.vstack([v1,v2,v3,v4]).T

# Найдите определитель матрицы Грама  системы Ответ округлите до целого числа.
print(np.linalg.det((A.T@A)))
