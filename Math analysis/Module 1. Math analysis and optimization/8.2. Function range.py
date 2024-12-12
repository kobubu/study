from sympy.calculus.util import continuous_domain
import sympy as sp
from sympy import S

# Определяем символы
x = sp.Symbol('x')
# Определяем функцию
f = x**3/(2*(x+5)**2)

first_derivative = sp.diff(f, x, 1)
second_derivative = sp.diff(f, x, 2)

a = continuous_domain(f, x, S.Reals)

# Выводим корни
print("Область определения:", a)
