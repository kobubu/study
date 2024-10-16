'''
Мы разрабатываем приложение, которое подразумевает функционал авторизации пользователя,
а также управление его балансом на некотором виртуальном счете.

Определите класс для пользователей User.
У него должны быть
атрибуты email, password и balance, которые устанавливаются при инициализации в методе __init__();
метод login(), который реализует проверку почты и пароля. Метод должен принимать в качестве аргументов емайл (email) и пароль (password).
Если они совпадают с атрибутами объекта, он возвращает True, а иначе — False;
метод update_balance(), который должен принимать в качестве аргумента amount некоторое число и изменять текущий баланс счёта (атрибут balance)
на величину amount.
В случае правильного описания класса код, приведённый ниже, должен выдать следующий результат:
Пример использования класса:

user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700
Обратите внимание, что от вас требуется только объявить класс. Создавать экземпляров класса не нужно!
'''

class User:
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance

    def login(self, email, password):
        return self.email == email and self.password == password

    def update_balance(self, amount):
        self.balance += amount




















