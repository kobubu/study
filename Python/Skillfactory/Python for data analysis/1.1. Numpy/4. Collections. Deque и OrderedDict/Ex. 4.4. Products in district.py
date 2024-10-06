'''
В переменных center, south и north хранятся списки из перечней купленных позиций в трёх торговых точках, расположенных в разных районах города.
Вначале избавьтесь от излишней вложенности: в каждой переменной (center, south, north) должен храниться объединённый список купленных товаров без разбиения по чекам.

Пример:[['Milk', 'Bread'], ['Meat']] -> ['Milk', 'Bread', 'Meat']
После этого определите, в каком магазине было куплено больше всего товаров.
'''

from collections import  OrderedDict

# Пример данных
center = [['Milk', 'Bread'], ['Meat'], ['Cheese', 'Eggs']]
south = [['Bread', 'Butter'], ['Milk'], ['Cheese']]
north = [['Meat', 'Cheese'], ['Bread'], ['Milk', 'Eggs']]

# Объединение вложенных списков
center_flat = [item for sublist in center for item in sublist]
south_flat = [item for sublist in south for item in sublist]
north_flat = [item for sublist in north for item in sublist]

# Определение количества товаров в каждом магазине
center_count = len(center_flat)
south_count = len(south_flat)
north_count = len(north_flat)

# Определение магазина с наибольшим количеством товаров
max_count = max(center_count, south_count, north_count)

# Вывод результата
if center_count == max_count:
    print("Больше всего товаров было куплено в центре.")
if south_count == max_count:
    print("Больше всего товаров было куплено на юге.")
if north_count == max_count:
    print("Больше всего товаров было куплено на севере.")


from collections import Counter
# Получение объектов-счетчиков
center_counter = Counter(center_flat)
south_counter = Counter(south_flat)
north_counter = Counter(north_flat)

# Определение самого редкого товара в магазине north
rarest_item_north = north_counter.most_common()[-1]

# Вывод количества покупок самого редкого товара в магазине north
print(rarest_item_north[1])

# Находим товары, которые покупали чаще в магазине center, чем в магазине north
more_frequent_in_center = [item for item in center_counter if center_counter[item] > north_counter.get(item, 0)]

# Вывод результата
print(more_frequent_in_center)

# Вывод результата
print(more_frequent_in_center)

combined_south_north = south_counter + north_counter
combined_center_south = center_counter + south_counter
combined_center_north = center_counter + north_counter

# Находим товары, которые покупали чаще в одном магазине, чем в двух других вместе взятых
popular_in_center = [item for item in center_counter if center_counter[item] > combined_south_north[item]]
popular_in_south = [item for item in south_counter if south_counter[item] > combined_center_north[item]]
popular_in_north = [item for item in north_counter if north_counter[item] > combined_center_south[item]]

# Определяем, в каком магазине есть такой товар
if popular_in_center:
    print("В магазине center есть товар, который покупали чаще, чем в south и north вместе взятых.")
if popular_in_south:
    print("В магазине south есть товар, который покупали чаще, чем в center и north вместе взятых.")
if popular_in_north:
    print("В магазине north есть товар, который покупали чаще, чем в center и south вместе взятых.")

# Суммирование всех счетчиков
total_counter = center_counter + south_counter + north_counter

# Определение второго по популярности товара
most_common_items = total_counter.most_common()
second_most_popular_item = most_common_items[1]

# Вывод количества продаж второго по популярности товара
print(second_most_popular_item[1])
