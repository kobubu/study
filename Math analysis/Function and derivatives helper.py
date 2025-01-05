from sympy.calculus.util import continuous_domain, function_range, log
import sympy as sp
from sympy import S, solveset, Eq

# Определяем символы
x = sp.Symbol('x')
y = sp.Symbol('y')

# Определяем функцию
f = x**3-6*x+2

# Область определения функции
domain = continuous_domain(f, x, S.Reals)

# Область значений функции
range_of_f = function_range(f, x, S.Reals)

# Пересечение графика функции с осью x (y=0)
function_intersection_x = solveset(Eq(f, 0), x)

# Пересечение с осью y (при x = 0)
intersection_y = f.subs(x, 0)

# Вычисляем первую и вторую производные
first_derivative = sp.diff(f, x, 1)
second_derivative = sp.diff(f, x, 2)


#находим точки экстремума (находим значения х, где значение производной = 0)
extremum = solveset(Eq(first_derivative, 0), x)

# Значение производной при x = 1 (решаем уравнение f(x) = )
first_derivative_value_at_0 = first_derivative.subs(x, 0)

# Значение производной при x = 1 (решаем уравнение f(x) = 0)
second_derivative_value_at_1 = second_derivative.subs(x, 1)


# Вывод результатов
print("Область определения:", domain)
print("Область значений:", range_of_f)
print("Пересечение графика функции с осью y:", intersection_y)
print("Пересечение графика функции с осью x:", function_intersection_x)
print("Первая производная:", first_derivative)
print("Вторая производная:", second_derivative)
print("Точка максимума/минимума:", extremum)
print("Значение производной в точке 0", first_derivative_value_at_0)
print("Значение второй производной в точке 1", second_derivative_value_at_1)
