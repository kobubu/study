'''
Допустим, мы решаем задачу оценки стоимости недвижимости.
В списке data представлены усреднённые данные по домам в районах Бостона. Каждый вложенный в список кортеж описывает средние данные по одному району (для примера представлены данные о семи участках). В этом кортеже представлены следующие признаки (в порядке следования):
x₁ — уровень преступности на душу населения по городам;
x₂ — среднее количество комнат в доме;
x₃ — доля зданий, построенных до 1940 г. и занимаемых владельцами;
x₄ — полная ставка налога на имущество за каждые 10 000 долларов стоимости;
x₅ — процент населения с низким статусом.

Пример данных:

data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
(0.02731, 6.421, 78.9, 242.0, 9.14),
(0.02729, 7.185, 61.1, 242.0, 4.03),
(0.03237, 6.998, 45.8, 222.0, 2.94),
(0.06905, 7.147, 54.2, 222.0, 5.33),
(0.02985, 6.43, 58.7, 222.0, 5.21),
(0.08829, 6.012, 66.6, 311.0, 12.43)]
Добавим в наш набор данных новый признак, который будет равен произведению трёх признаков — x₁, x₄ и x₅.
В результате выполнения программы у вас должен получиться список кортежей. Каждый кортеж должен состоять из шести элементов: первые пять — исходные признаки, а последний, шестой элемент — сгенерированный признак, округлённый до второго знака после запятой.
Результирующий список кортежей занесите в переменную updated_data.

Например, для исходного списка data, представленного выше, у вас должен получиться следующий список updated_data:

[(0.00632, 6.575, 65.2, 296.0, 4.98, 9.32),
(0.02731, 6.421, 78.9, 242.0, 9.14, 60.41),
(0.02729, 7.185, 61.1, 242.0, 4.03, 26.61),
(0.03237, 6.998, 45.8, 222.0, 2.94, 21.13),
(0.06905, 7.147, 54.2, 222.0, 5.33, 81.7),
(0.02985, 6.43, 58.7, 222.0, 5.21, 34.53),
(0.08829, 6.012, 66.6, 311.0, 12.43, 341.31)]
Примечание: Обратите внимание, что для отправки кода на проверку переменную data объявлять не нужно. Не забудьте удалить строку кода с её объявлением перед тем, как отправить код на тестирование.
'''
data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
        (0.02731, 6.421, 78.9, 242.0, 9.14),
        (0.02729, 7.185, 61.1, 242.0, 4.03),
        (0.03237, 6.998, 45.8, 222.0, 2.94),
        (0.06905, 7.147, 54.2, 222.0, 5.33),
        (0.02985, 6.43, 58.7, 222.0, 5.21),
        (0.08829, 6.012, 66.6, 311.0, 12.43)]

def add_new_feature(item):
    x1, x2, x3, x4, x5 = item
    new_feature = round(x1 * x4 * x5, 2)
    return (x1, x2, x3, x4, x5, new_feature)

updated_data = list(map(add_new_feature, data))

print(updated_data)

data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
        (0.02731, 6.421, 78.9, 242.0, 9.14),
        (0.02729, 7.185, 61.1, 242.0, 4.03),
        (0.03237, 6.998, 45.8, 222.0, 2.94),
        (0.06905, 7.147, 54.2, 222.0, 5.33),
        (0.02985, 6.43, 58.7, 222.0, 5.21),
        (0.08829, 6.012, 66.6, 311.0, 12.43)]

updated_data = list(map(lambda item: item + (round(item[0] * item[3] * item[4], 2),), data))

print(updated_data)
