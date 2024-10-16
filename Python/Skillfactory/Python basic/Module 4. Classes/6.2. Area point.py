'''
Вы участвуете в разработке библиотеки визуализации данных.
Вам поручено реализовать класс AreaPoint с двумя локальными атрибутами — координатами i и j.
Они должны определяться внутри инициализатора класса как обязательные позиционные аргументы.
Также добавьте в инициализатор аргумент height со значением по умолчанию 15.
Далее создайте двумерный список area_list размером 3 x 3, состоящий из таких объектов.
При этом атрибуты i и j должны соответствовать индексам объекта в списке.
Таким образом, ваш двумерный список должен будет представлять такое поле:

area_list:
AreaPoint:	AreaPoint:	AreaPoint:
i = 0	i = 1	i = 2
j = 0	j = 0	j = 0
height = 15	height = 15	height = 15
AreaPoint:	AreaPoint:	AreaPoint:
i = 0	i = 1	i = 2
j = 1	j = 1	j = 1
height = 15	height = 15	height = 15
AreaPoint:	AreaPoint:	AreaPoint:
i = 0	i = 1	i = 2
j = 2	j = 2	j = 2
height = 15	height = 15	height = 15
На экран ничего выводить не нужно — только создать двумерный список area_list.
'''

class AreaPoint:
    def __init__(self, i, j, height=15):
        self.i = i
        self.j = j
        self.height = height

area_list = [[AreaPoint(i, j) for i in range(3)] for j in range(3)]
