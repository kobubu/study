'''
На втором этапе напишите функцию get_min_string(), которая:
принимает на вход две строки s1 и s2,
возвращает ту, в которой количество уникальных символов меньше.
Чтобы определить количество уникальных символов, воспользуйтесь функцией get_count_unique_symbols(),
которую вы написали в предыдущем задании. Поместите ее определение и вызов внутрь функции get_min_string().
У вас должна получиться такая конструкция:
    def get_min_string(s1, s2):
        def get_count_unique_symbols(s):
            # Код внутренней функции
        # Применяем вложенную функцию к каждой из строк
        s1_len = get_count_unique_symbols(s1)
        s2_len = get_count_unique_symbols(s2)
        # код внешней функции
Функция get_min_string() должна возвращать:
строку s1, если количество уникальных символов в ней меньше, чем в s2;
строку s2, если количество уникальных символов в ней меньше, чем в s1;
кортеж из строк s1 и s2 при равенстве количества уникальных символов.
'''


def get_min_string(s1, s2):
    def get_count_unique_symbols(s):
        return len(set(s.lower().replace(' ', '')))
    s1_len = get_count_unique_symbols(s1)
    s2_len = get_count_unique_symbols(s2)
    return s1 if s2_len > s1_len else s2 if s1_len>s2_len else (s1, s2)

