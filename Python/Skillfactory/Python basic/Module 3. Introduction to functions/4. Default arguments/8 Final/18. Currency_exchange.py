'''
Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), сумму в рублях (rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар. Например, курс 85.46 означает, что один доллар стоит 85 рублей и 46 копеек.

В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, должна возникнуть ошибка ValueError('Not enough arguments'). Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').

Функция должна находить третий аргумент по двум переданным. Например, если переданы суммы в разных валютах, должен возвращаться обменный курс. Если известны сумма в рублях и курс, должна быть получена эквивалентная сумма в долларах, аналогично — если передана сумма в долларах и обменный курс.

Пример:
print(exchange(usd=100, rub=8500))
# 85.0
print(exchange(usd=100, rate=85))
# 8500
print(exchange(rub=1000, rate=85))
# 11.764705882352942
print(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments
print(exchange(rub=1000))
# ValueError: Not enough arguments
'''

def exchange(*args, **kwargs):
    if len(args) + len(kwargs) < 2:
        raise ValueError('Not enough arguments')
    elif len(args) + len(kwargs) > 2:
        raise ValueError('Too many arguments')

    usd = kwargs.get('usd')
    rub = kwargs.get('rub')
    rate = kwargs.get('rate')

    if usd is not None and rub is not None:
        return rub / usd
    elif usd is not None and rate is not None:
        return usd * rate
    elif rub is not None and rate is not None:
        return rub / rate
    else:
        raise ValueError('Not enough arguments')

# Примеры использования:
print(exchange(usd=100, rub=8500))  # Вывод: 85.0
print(exchange(usd=100, rate=85))   # Вывод: 8500
print(exchange(rub=1000, rate=85))   # Вывод: 11.764705882352942
print(exchange(rub=1000, rate=85, usd=90))  # ValueError: Too many arguments
print(exchange(rub=1000))  # ValueError: Not enough arguments
