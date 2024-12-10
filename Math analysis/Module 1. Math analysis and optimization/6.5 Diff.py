'''
Вычислить производную для функции.
'''
import sympy
from sympy import diff, sin, exp, log, Symbol
x = sympy.Symbol("x")
expr = sin(x*3+log(x))*exp**x
expr.diff(x)
print(expr.diff(x))
