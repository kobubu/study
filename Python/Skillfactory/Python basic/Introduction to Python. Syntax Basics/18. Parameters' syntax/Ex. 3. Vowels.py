'''
Напишите программу, которая принимает на вход слово (word) и последовательно выводит все русские гласные из этого слова.
'''
# Введите свое решение ниже
import re

word = 'йцухйзцухйцхуфыжвфжыьясячмь'
IS_VOWAL = re.compile(r'[^аоуеиюыяэ]', re.IGNORECASE)
word = IS_VOWAL.sub('', word)
[print(c) for c in word]