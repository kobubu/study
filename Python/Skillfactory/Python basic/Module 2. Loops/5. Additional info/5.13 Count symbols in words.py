'''
Дан список из строк str_list. Например:


str_list = ["text", "morning", "notepad", "television", "ornament"]
Напишите программу для подсчёта количества вхождений заданного символа в каждую из строк этого списка. Искомый символ хранится в переменной symbol_to_check.

Для подсчёта используйте словарь: в качестве ключа запишите в него строку, в качестве значения — число вхождений искомого символа в эту строку. Для хранения словаря используйте переменную с именем word_dict.
'''

str_list = ["text", "morning", "notepad", "television", "ornament"]
symbol_to_check = 'a'
word_dict = {word: word.count(symbol_to_check) for word in set(str_list)}

print(word_dict)
