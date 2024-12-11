'''
Вычислить производную для функции.
'''
import sympy as sp

# Определяем символы
x = sp.Symbol('x')
a = 4  # Задаем значение a = 4

# Определяем функцию
f = x**3 -6*x

# Вычисляем вторую производную и подставляем x = 4
# first_derivative = sp.diff(f, x, 1).subs(x, 4)

first_derivative = sp.diff(f, x, 1)
# Выводим результат
# print("Значение второй производной в точке 4", first_derivative)

print("Значение второй производной", first_derivative)

# Решаем уравнение первой производной, равной нулю
roots = sp.solve(first_derivative, x)

# Выводим корни
print("Корни уравнения первой производной:", roots)
