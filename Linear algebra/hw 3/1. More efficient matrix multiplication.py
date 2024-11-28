#ваш код
#добавим зависимости
import numpy as np
import pandas as pd

def multiplication_order(A, B, C):
    # проверим размерности
    a, b = A.shape
    _, c = B.shape  # B - b x c
    _, d = C.shape  # C - c x d
    
    # считаем стоимость (AxB)xC
    cost1 = a * b * c + a * c * d
    
    # считаем стоимость Ax(BxC)
    cost2 = b * c * d + a * b * d
    
    # вычисляем более эффективный способ
    return "(AxB)xC" if cost1 <= cost2 else "Ax(BxC)"
    
# Проверка на тестовых данных - пример из задания
A = np.array([[1, 2]])
B = np.array([[2], [1]])
C = np.array([[5]])

print(multiplication_order(A, B, C))  # Вывод: "(AxB)xC"

# Проверка на тестовых данных
A = np.array([[1], [2]])  # 2x1
B = np.array([[3, 4]])    # 1x2
C = np.array([[5], [6]])  # 2x1

print(multiplication_order(A, B, C))  # Вывод: "Ax(BxC)"
