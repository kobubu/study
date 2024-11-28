#ваш код
def inverse_matrix(A):
  return None if abs(np.linalg.det(A)) < 0.001 else np.linalg.inv(A)

A = np.array([[1, 2], [2, 1]])

print(inverse_matrix(A))
#Пример результата: array([[-0.33333333, 0.66666667],[ 0.66666667, -0.33333333]])
