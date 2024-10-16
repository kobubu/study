'''
При разработке сервиса охраны бизнес-центра вам поручили реализовать класс Person для создания пропускных карточек.
В этом классе инициализатор __init__() должен принимать аргументы:
- name;
- age;
- gender;
- occupation.

В качестве значения по умолчанию у этих аргументов должно быть None.Также __init__()
должен создавать локальные свойства в экземпляре с соответствующими именами.

Реализуйте методы:
- set_attributes(), который принимает словарь с произвольным числом записей, которые представлены в нём в виде имя_атрибута:
 значение и которые вам необходимо обновить в классе (в словаре может быть произвольное значение записей, например только для name и age).
- show_card(), который выводит строку (многострочную) следующего вида:

Name: значение_атрибута_name
Age: значение_атрибута_age
Gender: значение_атрибута_gender
Occupation: значение_атрибута_occupation
Пример использования класса:

p1 = Person()
p1.set_attributes({'name': 'Elon', 'age': 51, 'gender': 'Male', 'occupation': 'CEO', 'company': 'Tesla'})
p1.show_card()
# Name: Elon
# Age: 51
# Gender: Male
# Occupation: CEO
p2 = Person(name='Mark', occupation='Expert')
p2.set_attributes({'name': 'Bob', 'occupation': 'Worker', 'company': 'StenWoods'})
p2.show_card()
# Name: Bob
# Age: None
# Gender: None
# Occupation: Worker
'''

class Person:
    def __init__(self, name=None, age=None, gender=None, occupation=None):
        self.name = name,
        self.age = age,
        self.gender = gender,
        self.occupation = occupation

    def set_attributes(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

    def show_card(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")







