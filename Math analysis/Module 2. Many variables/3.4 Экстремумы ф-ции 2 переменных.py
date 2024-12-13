import sympy as sp

# Определяем переменные
x, y = sp.symbols('x y')

# Определяем функцию
z = 4*x**2 - 6*x*y - 34*x + 5*y**2 + 42*y + 7

# Находим частные производные
dz_dx = sp.diff(z, x)
dz_dy = sp.diff(z, y)

# Решаем систему уравнений для нахождения стационарных точек
stationary_points = sp.solve((dz_dx, dz_dy), (x, y))

# Выводим стационарные точки
print("Стационарная точка:", stationary_points)

# Проверяем характер экстремума
d2z_dx2 = sp.diff(z, x, 2)
d2z_dy2 = sp.diff(z, y, 2)
d2z_dxdy = sp.diff(z, x, y)

# Вычисляем определитель матрицы Гессе
H = sp.Matrix([[d2z_dx2, d2z_dxdy], [d2z_dxdy, d2z_dy2]])
D = H.det()

# Выводим результаты
print("Определитель матрицы Гессе:", D.subs(stationary_points))
print("Значение второй производной по x:", d2z_dx2.subs(stationary_points))

# Определяем характер экстремума
if D.subs(stationary_points) > 0 and d2z_dx2.subs(stationary_points) > 0:
    print("Точка минимума")
elif D.subs(stationary_points) > 0 and d2z_dx2.subs(stationary_points) < 0:
    print("Точка максимума")
else:
    print("Точка седловая")
