'''
В нашем распоряжении есть список строк разной длины.
Напишите функцию equalize_lengths(), которая принимает на вход список и возвращает новый список из строк одинаковой длины.
Длина итоговой строки должна быть равна длине самой длинной из строк. Если конкретная строка короче самой длинной, её необходимо дополнить до требуемого количества символов нижними подчёркиваниями с правого края.
Важно! Результирующий список должен быть отсортирован от меньшего к большему по количеству добавленных символов нижнего подчёркивания. То есть первым должен идти элемент с максимальной длиной строки.
Примеры работы программы:

print(equalize_lengths(['крот', 'белка', 'выхухоль']))
# ['выхухоль', 'белка___', 'крот____']

print(equalize_lengths(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# ['aaaaa', 'aaaa_', 'aaa__', 'aa___', 'a____']

print(equalize_lengths(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))

# ['qweasdqweas', 'ewqqqqq____', 'rteww______', 'q__________']

'''


def equalize_lengths(lst):
    # Находим максимальную длину строки в списке
    max_length = max(len(el) for el in lst)

    # Дополняем каждую строку до максимальной длины и сортируем по количеству добавленных символов
    result = sorted([el.ljust(max_length, '_') for el in lst], key=lambda x: x.count('_'), reverse=False)

    return result


# Примеры работы программы
print(equalize_lengths(['крот', 'белка', 'выхухоль']))
# Вывод: ['выхухоль', 'белка___', 'крот____']

print(equalize_lengths(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# Вывод: ['aaaaa', 'aaaa_', 'aaa__', 'aa___', 'a____']

print(equalize_lengths(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
# Вывод: ['qweasdqweas', 'ewqqqqq____
