'''
вычислите собственные числа и векторы матрицы
'''
import numpy as np

# Define matrix A
A = np.array([[1, 3, 5],
              [4, -4, 9],
              [13, 7, 12]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sorting eigenvalues and eigenvectors by the magnitude of eigenvalues
sorted_indices = np.argsort(-np.abs(eigenvalues))
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices]

# Compute determinant of the eigenvector matrix
det_eigenvectors = np.linalg.det(eigenvectors)

# Check symmetry of matrix A
is_symmetric = np.allclose(A, A.T)

# Verify the eigenvalue-eigenvector relationship
verification_results = []
for i in range(len(eigenvalues_sorted)):
    v = eigenvectors_sorted[:, i]
    lambda_val = eigenvalues_sorted[i]
    Av = np.dot(A, v)
    lambda_v = lambda_val * v
    diff = np.linalg.norm(Av - lambda_v)
    verification_results.append((lambda_val, Av, lambda_v, diff))

# Prepare results
result = {
    "Eigenvalues": eigenvalues,
    "Sorted Eigenvalues": eigenvalues_sorted,
    "Determinant of Eigenvector Matrix": det_eigenvectors,
    "Is Symmetric": is_symmetric,
    "Verification Results": verification_results
}
print(result)
