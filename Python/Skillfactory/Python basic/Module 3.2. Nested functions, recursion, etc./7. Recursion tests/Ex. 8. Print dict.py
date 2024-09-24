'''
Пусть у нас есть словарь input_dict следующего вида:
input_dict = {
    'key1': {
        'key2': ['value1', 'value2'],
        'key3': {
            'key4': ['value3']
        }
    },
    'key5': {
        'key6': {
            'key7': ['value3', 'value5', 'value6']
        }
    }
}
Мы хотим напечатать этот словарь следующим образом:
key1 ->
  key2 ->
    ['value1', 'value2']
  key3 ->
    key4 ->
      ['value3']
key5 ->
  key6 ->
    key7 ->
      ['value3', 'value5', 'value6']
Для этого мы написали рекурсивную функцию print_dict():
def print_dict(input_data, level=0):
    # Если input_data — словарь
    if type(input_data) is dict:
        # Создаём цикл по ключам словаря
        for key in input_data:
            # Выводим ключ в формате "<пробелы> <имя ключа> ->"
            print('  ' * level + '{} ->'.format(key))
            # Повторяем те же операции для каждого значения словаря
            print_dict(input_data[key], level=level)
    else: # В противном случае
        # Выводим значения в формате "<пробелы> <значения>"
        print('  ' * level + str(input_data))
Однако мы где-то допустили ошибку в функции и она печатает словарь в следующем виде:
key1 ->
key2 ->
['value1', 'value2']
key3 ->
key4 ->
['value3']
key5 ->
key6 ->
key7 ->
['value3', 'value5', 'value6']
Разберитесь в функции print_dict() и исправьте её так, чтобы словарь печатался в нужном формате.
'''

def print_dict(input_data, level=0):
    # Если input_data — словарь
    if type(input_data) is dict:
        # Создаём цикл по ключам словаря
        for key in input_data:
            # Выводим ключ в формате "<пробелы> <имя ключа> ->"
            print('  ' * level + '{} ->'.format(key))
            # Повторяем те же операции для каждого значения словаря
            print_dict(input_data[key], level=level+1)
    else: # В противном случае
        # Выводим значения в формате "<пробелы> <значения>"
        print('  ' * level + str(input_data))

input_dict = {
    'key1': {
        'key2': ['value1', 'value2'],
        'key3': {
            'key4': ['value3']
        }
    },
    'key5': {
        'key6': {
            'key7': ['value3', 'value5', 'value6']
        }
    }
}

print(print_dict(input_dict, 0))
