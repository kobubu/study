
# Define matrix A
A = np.array([[5, 1], [1, 5]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sorting eigenvalues and eigenvectors by the magnitude of eigenvalues
sorted_indices = np.argsort(-np.abs(eigenvalues))
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices]

eigenvalues_sorted, eigenvectors_sorted
