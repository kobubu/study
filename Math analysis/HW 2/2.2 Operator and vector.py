'''
Результат действия оператора на вектор  называют образом вектора.
a) Найдите образ вектора v [1, 2, 3] при действии оператора F [1, 0, 0], [0, 0, 1], [0, -1, 0], если

v =
'''

import numpy as np

# Define the vector v as a column vector
v = np.array([[1],
              [2],
              [3]])

# Define the operator F as a 2D array
F = np.array([[1, 0, 0],
              [0, 0, 1],
              [0, -1, 0]])

# Compute the image of v under F
image_v = F @ v

# Print the result
print("The image of v under F is:")
print(image_v)
