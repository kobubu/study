'''
Перепишите функцию between_min_max из задания 7.12 в lambda-функцию.
 Функция принимает на вход числа через запятую и возвращает одно число — среднее между максимумом и минимумом этих чисел.
'''

between_min_max = lambda *args: (max(args) + min(args))/2

print(between_min_max(2,3,4,5,6,7,8,9))
