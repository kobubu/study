## Введите свое решение ниже
import re
from statistics import mode

REMOVE_PUNCTUATION = re.compile(r'[.,;:!?\-\"()]', re.IGNORECASE)

def get_most_frequent_word(text):
    def get_words_list(text):
        # Удаляем знаки препинания и приводим текст к нижнему регистру
        text = REMOVE_PUNCTUATION.sub('', text).lower()
        # Разбиваем текст на слова
        return text.split()

    def get_unique_words(lst):
        # Возвращаем отсортированный список уникальных слов
        return sorted(list(set(lst)))

    if not text:
        return ''

    # Получаем список слов
    words_list = get_words_list(text)
    
    try:
        # Находим слово с максимальной частотой
        most_frequent_word = mode(words_list)
    except StatisticsError:
        # Если несколько слов имеют одинаковую максимальную частоту, выбираем первое по алфавиту
        unique_words = get_unique_words(words_list)
        word_counts = {word: words_list.count(word) for word in unique_words}
        most_frequent_word = max(unique_words, key=lambda word: (word_counts[word], word))
    
    return most_frequent_word
