'''
Мы генерируем текст с помощью нейронной сети.
В списке word_list в виде строк задана сгенерированная нейронной сетью последовательность слов. Например:

word_list = ["My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
Напишите программу для объединения строк из списка word_list в предложения.

Гарантируется, что конец каждого предложения обозначается специальной последовательностью символов 
— "EOS" (End Of Sentence). 
Вместо этого символа в предложении ставится точка — ".". 
Для простоты условимся, что другие знаки препинания (запятые, восклицательные знаки и т. д.)
 нейронная сеть генерировать не умеет.

Для решения задачи воспользуйтесь циклом for. Результирующий текст запишите в переменную text.

Напишите программу для объединения строк из списка word_list в предложения c заменой EOS на точку.

'''

import re

word_list = ["My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
text = re.sub(' EOS', '.', ' '.join(word_list).strip())

print(text)
#My name is Sergei. I'm from Moscow.
