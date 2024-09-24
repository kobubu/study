'''

Дана строка, содержащая только английские буквы (большие и маленькие).
Напишите рекурсивную функцию add_asterisk(). Она должна принимать в качестве аргумента строку и добавлять символ * (звёздочка) между буквами.
Перед первой и после последней буквами символ * добавлять не нужно.
Пример вызова функции:
print(add_asterisk('hello'))
## h*e*l*l*o
print(add_asterisk('LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO'))
## L*I*t*B*e*o*F*L*c*S*G*B*O*F*Q*x*M*H*o*I*u*D*D*W*c*q*c*V*g*k*c*R*o*A*e*o*c*X*O
print(add_asterisk('gkafkafkKdaflkfa'))
## g*k*a*f*k*a*f*k*K*d*a*f*l*k*f*a
'''
import re

def add_asterisk(s):
    if len(s) == 1 or len(s) == 0:
        return s
    return f'{s[0]}*{add_asterisk(s[1:])}'

