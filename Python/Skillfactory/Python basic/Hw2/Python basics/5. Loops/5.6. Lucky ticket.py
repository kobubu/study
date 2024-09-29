'''
Напишите функцию lucky_ticket(), которая проверяет, является ли билет счастливым.
Примечание. Билет счастливый, если сумма первых трёх цифр в его номере равна сумме последних трёх цифр.
На вход функция принимает шестизначное число ticket_number и должна возвращать одно из булевых значений
(True или False) в зависимости от того, является ли билет счастливым.
При решении постарайтесь не использовать встроенную функцию sum() — примените циклы.
Примеры работы программы:
print(lucky_ticket(111111))
# True
print(lucky_ticket(123456))
# False
'''

def lucky_ticket(ticket_number):
    return sum(int(digit) for digit in str(ticket_number)[:3]) == sum(int(digit) for digit in str(ticket_number)[3:])


print(lucky_ticket(111111))
print(lucky_ticket(123456))







