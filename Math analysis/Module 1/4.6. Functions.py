'''
Найдите координаты пересечения с осью x для функции : y=x*x+2x-8
Примечание. Здесь можно воспользоваться библиотекой SymPy.
'''

from sympy import solveset, Eq, symbols

# Определяем символ x
x = symbols('x')

# Решаем уравнение x^2 + 2x - 8 = 0
solution = solveset(Eq(x*x + 2*x - 8, 0), x)

# Выводим решение
print(solution)
