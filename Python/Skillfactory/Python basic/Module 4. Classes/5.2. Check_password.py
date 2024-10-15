'''
При дальнейшей реализации сервиса вам поручили реализовать класс PasswordChecke,
который будет выполнять проверку паролей в соответствии с заданными условиями. Для этого в классе надо реализовать следующие два метода:

set_password_range(), который принимает в качестве первого аргумента минимально допустимую длину пароля,
в качестве второго — максимально допустимую длину пароля, и сохраняет их в локальных атрибутах min_len и max_len;
check_passwords(), который принимает в качестве аргумента список из строк-паролей и возвращает список соответствующей длины,
где на месте каждого пароля стоит булево значение: допустим он или нет (длина строки находится в диапазоне [min_len, max_len] включительно).
Пример использования класса:

checker1 = PasswordChecker()
checker1.set_password_range(5, 10)
print(checker1.min_len, checker1.max_len)

# 5 10

print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))

# [False, True, False]
'''


class PasswordChecker:
    def set_password_range(self, min_length, max_length):
        """
        Устанавливает минимальную и максимальную длину пароля.

        :param min_length: Минимальная длина пароля.
        :param max_length: Максимальная длина пароля.
        """
        self.min_len = min_length
        self.max_len = max_length

    def check_passwords(self, passwords):
        """
        Проверяет список паролей на соответствие заданному диапазону длин.

        :param passwords: Список паролей для проверки.
        :return: Список результатов проверки (True или False).
        """
        # Используем функцию map для применения проверки к каждому паролю
        return list(map(lambda x: self.min_length <= len(x) <= self.max_length, passwords))
