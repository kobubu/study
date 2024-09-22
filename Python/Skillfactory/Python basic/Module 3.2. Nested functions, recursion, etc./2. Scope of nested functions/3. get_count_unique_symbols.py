'''
На первом этапе напишите функцию get_count_unique_symbols(), которая:
принимает на вход строку s,
одит её к нижнему регистру,
убирает из неё все пробелы,
возвращает количество уникальных символов в строке.
Примеры вызова функции:
    get_count_unique_symbols('Это простая строка')
    ## 9
    get_count_unique_symbols('This is a simple string')
    ## 12
'''

def get_count_unique_symbols(s):
    return len(set(s.lower().replace(' ', '')))

string = 'asdghqwjeklqw;ejqhwegkqwl;dfpouidgchljok'
print(get_count_unique_symbols(string))
