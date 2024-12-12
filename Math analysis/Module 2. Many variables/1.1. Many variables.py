from sympy.calculus.util import continuous_domain, function_range, log
import sympy as sp
from sympy import S, solveset, Eq

# Определяем символы
x = sp.Symbol('x')
y = sp.Symbol('y')

# Определяем функцию
f = x**3+4*x-5

# Вычисляем первую и вторую производные
first_derivative = sp.diff(f, x, 1)
second_derivative = sp.diff(f, x, 2)

# Область определения функции
domain = continuous_domain(f, x, S.Reals)

# Область значений функции
range_of_f = function_range(f, x, S.Reals)

# Пересечение с осью y (при x = 0)
intersection_y = f.subs(x, 0)

# Пересечение с осью x (решаем уравнение f(x) = 0)
intersection_x = solveset(Eq(first_derivative, 0), x, domain=S.Reals)

# Значение производной при x = 1 (решаем уравнение f(x) = 0)
value_at_1 = first_derivative.subs(x, 1)


#находим точки макс. и мин (находим, где значение производной = 0)
mm = solveset(Eq(first_derivative, 0), x)

# Вывод результатов
print("Пересечение с осью y:", intersection_y)
print("Пересечение с осью x:", intersection_x)
print("Область определения:", domain)
print("Область значений:", range_of_f)
print("Первая производная:", first_derivative)
print("Вторая производная:", second_derivative)
print("Точка максимума/минимума:", mm)
print("Значение производной в точке 1", value_at_1)
