class Model:
    # Константы для минимальной и максимальной длины имени модели
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 15

    def __init__(self):
        # Инициализация приватного атрибута __name значением None
        self.__name = None

    @property
    def name(self):
        # Геттер для атрибута name, возвращает значение __name
        return self.__name

    @name.setter
    def name(self, value):
        # Сеттер для атрибута name, проверяет длину значения и устанавливает __name
        if self.NAME_MIN_LENGTH <= len(value) <= self.NAME_MAX_LENGTH:
            # Если длина значения соответствует требованиям, устанавливаем __name
            self.__name = value
        else:
            # Если длина значения не соответствует требованиям, устанавливаем __name в None
            self.__name = None
