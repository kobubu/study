'''
Напишите функцию get_unique_words(), которая принимает на вход аргумент words_list (список из слов)
и возвращает упорядоченный по алфавиту список уникальных слов.
Гарантируется, что на вход функции подаётся список из слов, приведённых к единому регистру.
Примеры работы программы:
words_list_example = ['and', 'take', 'the', 'most', 'special', 'care', 'that', 'you', 'locate', "muad'dib", 'in', 'his', 'place', 'the', 'planet', 'arrakis', 'do', 'not', 'be', 'deceived', 'by', 'the', 'fact', 'that', 'he', 'was', 'born', 'on', 'caladan', 'and', 'lived', 'his', 'first', 'fifteen', 'years', 'there', 'arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
print(get_unique_words(words_list=words_list_example))
## ['and', 'arrakis', 'as', 'be', 'born
'''

def get_unique_words(lst):
    return sorted(list(set(lst)))

words_list_example = ['and', 'take', 'the', 'most', 'special', 'care', 'that', 'you', 'locate', "muad'dib", 'in', 'his', 'place', 'the', 'planet', 'arrakis', 'do', 'not', 'be', 'deceived', 'by', 'the', 'fact', 'that', 'he', 'was', 'born', 'on', 'caladan', 'and', 'lived', 'his', 'first', 'fifteen', 'years', 'there', 'arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
print(get_unique_words(words_list_example))
## ['and', 'arrakis', 'as', 'be', 'born






