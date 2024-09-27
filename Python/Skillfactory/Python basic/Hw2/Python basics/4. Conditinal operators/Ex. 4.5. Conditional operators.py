'''
Напишите функцию check_number_sign(), которая возвращает 1, если число положительное, -1 — если число отрицательное, и 0 — если число равно 0.
Функция принимает на вход одно число number.
Используйте в коде конструкцию if-elif-else.
Примеры работы функции:

print(check_number_sign(5290))
# 1
print(check_number_sign(-983))
# - 1
print(check_number_sign(0))
# 0
'''

def check_number_sign(number):
    return  1 if number > 0 else -1 if number < 0 else 0



