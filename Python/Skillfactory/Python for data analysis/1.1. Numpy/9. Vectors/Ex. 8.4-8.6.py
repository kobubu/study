from hidden import *
import numpy as np
# Вычисление длины суммы векторов
sum_vector = a + c
length_of_sum = np.linalg.norm(sum_vector)

# Вычисление суммы длин векторов
length_a = np.linalg.norm(a)
length_b = np.linalg.norm(b)
length_c = np.linalg.norm(c)
sum_of_lengths = length_a + length_c

# Сравнение
if length_of_sum == sum_of_lengths:
    print("Длина суммы векторов равна сумме длин векторов.")
elif length_of_sum < sum_of_lengths:
    print("Длина суммы векторов меньше суммы длин векторов.")
else:
    print("Длина суммы векторов больше суммы длин векторов.")

# найдем, какое расстояние между векторами больше 100
distance_a_b = np.linalg.norm(a - b)
distance_a_c = np.linalg.norm(a - c)
distance_b_c = np.linalg.norm(b - c)
print(distance_a_b)
print(distance_a_c)
print(distance_b_c)

# Найдите пару перпендикулярных векторов с помощью скалярного произведения (оно должно быть равно нулю).
print(np.dot(a, b))
print(np.dot(a, c))
print(np.dot(b, c))
# такой пары нет

