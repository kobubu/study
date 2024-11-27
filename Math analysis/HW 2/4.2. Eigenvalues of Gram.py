'''
Найдите собственные числа матрицы Грама от A, если:
A = np.array([[1, 9, 4],
              [9, 4, 7],
              [4, 7, 12]])
Каждое из собственных чисел округлите до целого.'''
import numpy as np

# Define matrix A
A = np.array([[1, 9, 4],
              [9, 4, 7],
              [4, 7, 12]])

gram_matrix = A.T@A

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(gram_matrix)

print(eigenvalues)
