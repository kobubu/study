'''
Программа для поика наименьшего натурального числа x,
 квадрат которого нацело делится на число n, и выводит его на экран.
'''

n = 100
x = 1
while x ** 2 % n != 0:
    x += 1
print(x)