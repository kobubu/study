'''
Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов через запятую.
Гарантируется, что все векторы, которые передаются, одинаковой длины.
Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.
'''

import numpy as np

def min_max_dist(*vectors):
    # Преобразуем входные векторы в массив NumPy для удобства
    vectors = np.array(vectors)
    
    # Инициализируем минимальное и максимальное расстояние
    min_dist = float('inf')
    max_dist = 0
    
    # Вычисляем попарные расстояния между векторами
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            # Вычисляем евклидово расстояние между векторами i и j
            dist = np.linalg.norm(vectors[i] - vectors[j])
            
            # Обновляем минимальное и максимальное расстояние
            if dist < min_dist:
                min_dist = dist
            if dist > max_dist:
                max_dist = dist
    
    # Возвращаем кортеж с минимальным и максимальным расстоянием
    return min_dist, max_dist
