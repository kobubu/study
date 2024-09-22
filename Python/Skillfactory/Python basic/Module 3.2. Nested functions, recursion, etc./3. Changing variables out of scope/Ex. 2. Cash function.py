'''
Вам необходимо написать программу, которая будет вычислять сумму, оставшуюся на счёте у пользователя банковской карты. Посмотрите на код ниже и внесите в него исправление так, чтобы он работал верно.
    def cash(less_money):
        money -= less_money
        return money
    money = 200000
    print(cash(1000))
Не добавляйте аргументы в функцию cash, помимо less_money.
Примеры вызова функции:
    money = 200000
    print(cash(1000))
    ## 199000
    money = 30240
    print(cash(240))
    ## 30000
'''

def cash(less_money):
    global money
    money -= less_money
    return money
