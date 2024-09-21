'''
Напишите функцию sort_ignore_case(ls), которая принимает на вход список ls и сортирует его без учёта регистра по алфавиту.
Функция возвращает отсортированный список.
Пример:
print(sort_ignore_case(['Acc', 'abc']))
# ['abc', 'Acc']
'''

sort_ignore_case = lambda ls: sorted(ls, key=str.lower)

print(sort_ignore_case(['Acc', 'abc']))
['abc', 'Acc']
