'''
Напишите lambda-функцию is_palindrom(str), которая принимает на вход одну строку str (имя параметра - x)
 и проверяет, является ли она палиндромом, то есть читается ли она слева-направо и справа-налево одинаково.
Функция возвращает yes, если строка является палиндромом, иначе — no.
Примечание. Не пытайтесь схитрить — в тест включена проверка на то, что функция действительно является lambda.
Пример:
print(is_palindrom('1234'))
print(is_palindrom('12321'))
# no
# yes
'''
def is_palindrom(str):
    if str[::] == str[len(str)-1: :-1]:
        return 'yes'
    return 'no'
is_palindrom = lambda x: 'yes' if x[::] == x[len(x)-1: :-1] else 'no'

print(is_palindrom('1234'))
print(is_palindrom('12321'))

