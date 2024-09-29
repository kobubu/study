'''
Напишите функцию print_personal_data(), которая должна принимать на вход неизвестное количество именованных аргументов
(персональных данных) в любом порядке и выводить их в виде аргумент: значение в отсортированном по алфавиту порядке имён аргументов.
Примеры работы функции:
print_personal_data(first_name='John', last_name='Doe', age=28, position='Python developer')
# age: 28
# first_name: John
# last_name: Doe
# position: Python developer
'''

def print_personal_data(**kwargs):
    sorted_keys = sorted(kwargs.keys())

    for key in sorted_keys:
        print(f'{key}: {kwargs[key]}')

print_personal_data(first_name='Jack', last_name='Smith', age=32, work_experience = '5 years', position='Project manager')
# age: 32
# first_name: Jack
# last_name: Smith
# position: Project manager
# work_experience: 5 years






