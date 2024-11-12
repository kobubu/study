'''
Найти ранги матриц

'''
import numpy as np
A = np.array([[1,0,3,5],[0,4,5,5],[0,0,0,0],[0,0,0,0]])
B = np.array([[1,0,3,5],[0,4,5,5],[0,0,0,4  ],[0,0,0,0]])

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(B))
# 3
