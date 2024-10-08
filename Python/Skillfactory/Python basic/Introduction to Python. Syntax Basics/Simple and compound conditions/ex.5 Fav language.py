```
Вы решили создать систему, которая может подобрать для человека язык программирования в зависимости от его любимого слова. Напишите программу, которая может вам в этом помочь. Программа принимает на вход слово (fav_word).

Если это слова 'рептилия', 'питон' или 'змея', программа выводит 'Python'.
Если это слова 'плюс' или 'плюсы', программа выводит 'C++'.
Если это слова 'рубин' или 'кристалл', программа выводит 'Ruby'.
Если это не какое-то из перечисленных выше слов, программа тоже выводит 'Python'.
```
# Введите свое решение ниже
import re
RUBY_FAV = re.compile(r'^(?=.*(рубин|кристалл)).*$')
CPP_FAV = re.compile(r'^(?=.*(плюс|плюсы)).*$')
a = RUBY_FAV.match(fav_word) is not None
b = CPP_FAV.match(fav_word) is not None

if a:
    print('Ruby')
elif b:
    print('C++')
else:
    print('Python')
