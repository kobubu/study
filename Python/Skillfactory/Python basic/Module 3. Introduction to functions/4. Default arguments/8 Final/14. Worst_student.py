'''
Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов имена студентов
 и их номера в рейтинге (нагляднее в примере).
Необходимо вернуть имя студента с минимальным номером по рейтингу.
print(best_student(Tom=12, Mike=3))
print(best_student(Tom=12))
print(best_student(Tom=12, Jerry=1, Jane=2))
# Mike
# Tom
# Jerry
'''

def best_student(**kwargs):
    best_rating = 1000
    for name, rating in kwargs.items():
        if int(rating) < best_rating:
            best_rating = rating
            best_student = name, rating
    return best_student[0]

print(best_student(Tom=12, Jerry=1, Jane=2))
