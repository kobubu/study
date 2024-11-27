import numpy as np

# Define the matrix A and eigenvectors v1 and v2
A = np.array([[-7, 6], [-12, 11]])
v1 = np.array([1, 2])
v2 = np.array([1, 1])

# Eigenvalues
lambda1 = -1
lambda2 = 5

# Compute A * v1 and A * v2
Av1 = A @ v1
Av2 = A @ v2

# Check if A * v1 = lambda1 * v1 and A * v2 = lambda2 * v2
lambda1_v1 = lambda1 * v1
lambda2_v2 = lambda2 * v2

Av1, lambda1_v1, Av2, lambda2_v2
