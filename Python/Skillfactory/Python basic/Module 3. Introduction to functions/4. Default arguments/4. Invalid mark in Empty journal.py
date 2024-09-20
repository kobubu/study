# Введите свое решение ниже
def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if mark not in [2, 3, 4, 5]:
        raise ValueError("Invalid Mark!")
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal
