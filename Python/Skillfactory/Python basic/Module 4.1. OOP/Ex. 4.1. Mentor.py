'''
Вы работаете в агентстве недвижимости и вам необходимо разработать программу для управления объектами недвижимости,
такими как дома, квартиры и земельные участки.
Вам нужно создать классы, которые будут представлять разные типы объектов недвижимости, а также класс агентства, который будет отвечать за управление списком доступных объектов.
Базовый класс SellItem:
Инициализатор, который устанавливает локальные свойства:
name: строка;
price: целое или дробное число;
Дочерний класс House класса SellItem:
Инициализатор, который устанавливает локальные свойства:
name: строка (установка должна осуществляться инициализатором базового класса);
price: целое или дробное число (установка должна осуществляться инициализатором базового класса);
material: строка;
square: целое или дробное число.
Дочерний класс Flat класса SellItem:

Инициализатор, который устанавливает локальные свойства:
name: строка (установка должна осуществляться инициализатором базового класса)
price: целое или дробное число (установка должна осуществляться инициализатором базового класса)
size: целое или дробное число
square: целое или дробное число
Класс Agency:

Инициализатор, который устанавливает локальные свойства:
name: строка
objs: пустой список (не передаётся в качестве аргумента инициализатору)
Метод add_object() добавляет переданный объект в список objs
Метод remove_object() удаляет переданный объект из списка objs
Метод get_objects() возвращает свойство objs
'''


class Student:
    def __init__(self, fio, group):
        self.fio = fio  # ФИО студента (строка)
        self.group = group  # группа (строка)
        self.lect_marks = []  # оценки за лекции
        self.homework_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self.lect_marks.append(mark)

    def add_homework_marks(self, mark):
        self.homework_marks.append(mark)

    def __str__(self):
        return f"Студент {self.fio}: оценки на лекциях: {str(self.lect_marks)}; оценки за д/з: {str(self.homework_marks)}"

class Mentor():
    def __init__(self, fio, subject):
        self.fio = fio
        self.subject = subject

    def set_mark(self, student, mark):
        raise NotImplementedError

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f"Лектор {self.fio}: предмет {self.subject}"

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_homework_marks(mark)

    def __str__(self):
        return f"Эксперт {self.fio}: предмет {self.subject}"

