'''
Напишите функцию get_chess, которая принимает на вход длину стороны квадрата a и возвращает двумерный массив формы (a, a),
 заполненный 0 и 1 в шахматном порядке. В левом верхнем углу всегда должен быть ноль.
Примечание: воспользуйтесь функцией zeros из библиотеки numpy, а затем с помощью срезов без циклов задайте необходимым элементам значение 1.
Напоминание: в Python для получения каждого второго элемента используется срез [::2]. Подумайте, как грамотно применить этот принцип к двумерному массиву.
Пример:
get_chess(1)
# array([[0.]])
get_chess(4)
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])
'''
import numpy as np
def get_chess(a):
    # Создаем двумерный массив заданного размера, заполненный нулями
    array = np.zeros((a, a), dtype=str)
    for i in range(a):
        for j in range(a):
            if (i + j) % 2 != 0:
                array[i][j] = "1."
            else:
                array[i][j] = "0."
    return array
print(get_chess(3))


#OR

def get_chess(a):
    # Создаем двумерный массив заданного размера, заполненный нулями с типом float
    array = np.zeros((a, a), dtype=float)
    
    # Заполняем каждую вторую строку, начиная с первой строки
    array[::2, 1::2] = 1.0
    
    # Заполняем каждую вторую строку, начиная со второй строки
    array[1::2, ::2] = 1.0
    
    return array