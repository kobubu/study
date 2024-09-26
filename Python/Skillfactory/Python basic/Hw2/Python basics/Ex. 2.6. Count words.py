'''
Дана строка input_string. Избавьтесь от знаков препинания в ней и напишите программу для подсчёта количества слов в этой строке.
 Программа должна записывать результат в переменную count_words.
Гарантируется, что из знаков препинания в строке input_string могут содержаться только точки ('.'), запятые (','), восклицательные ('!') и вопросительные ('?') знаки.
Примеры работы программы:

input_string = 'Hello! My name is Python. I will help you to analyze some data.'
## count_words = 13
input_string = 'There are many great articles about Artificial Intelligence and its benefits for business and society. However, many of these articles are too technical for the average reader.'
## count_words = 27
'''
import re

REMOVE_PUNCTUATION = re.compile('[.,\?!]', re.IGNORECASE)

input_string = 'Hello! My name is Python. I will help you to analyze some data.'
input_string = REMOVE_PUNCTUATION.sub('', input_string)
count_words = len(input_string) - len(input_string.replace(' ', '')) + 1
print(count_words)
## count_words = 13
input_string = 'There are many great articles about Artificial Intelligence and its benefits for business and society. However, many of these articles are too technical for the average reader.'
## count_words = 27.

#OR
count_words = len(input_string.split())
