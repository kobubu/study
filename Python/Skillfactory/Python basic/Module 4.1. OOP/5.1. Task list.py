'''
Вы — разработчик программного обеспечения в стартапе, который создаёт продукт управления задачами.
Ваша команда хочет, чтобы вы разработали прототип системы управления задачами на языке Python.
Для этого вам необходимо создать класс TaskList, который содержит инициализатор, который, в свою очередь, инициализирует приватное свойство task_list пустым списком.
В процессе работы программы список task_list будет наполняться элементами — задачами (task).
task — словарь вида {'name': str, 'done': bool}, где ключ done при дальнейшей реализации будет говорить о статусе её выполнения.
Метод add_task() должен добавлять задачу в список, проверяя, есть ли уже такая задача в списке
и выводя строки "Задача <name> добавлена в список" и "Задача <name>  уже есть в списке" соответственно.
Метод remove_task() должен принимать название задачи и удалять эту задачу (соответствующий словарь) из списка, проверяя, существует ли такая задача, выводя при этом на экране соответствующие сообщения: "Задача <название_задачи> удалена из списка" или "Задачи <название_задачи> нет в списке".
Вспомогательный приватный метод is_task_in_list() должен проверять, существует ли такая задача в списке и возвращать значение True или False соответственно.
Пример использования класса


# Создаём контейнер задач
ts = TaskList()
# Добавляем задачи в контейнер
ts.add_task('Create get_task_list() method')

# Пытаемся добавить две одинаковые задач
ts.add_task('Show students how __task_list attr looks like')
ts.add_task('Show students how __task_list attr looks like')

# Добавляем задачу и удаляем ее
ts.add_task('Show students how work remove_task() method')
ts.remove_task('Show students how work remove_task() method')

# Смотрим приватный список задач
print(ts._TaskList__task_list)

# Задача "Create get_task_list() method" добавлена в список
# Задача "Show students how __task_list attr looks like" добавлена в список

# Задача "Show students how __task_list attr looks like" уже есть в списке

# Задача "Show students how work remove_task() method" добавлена в список
# Задача "Show students how work remove_task() method" удалена из списка

# [{'name': 'Create get_task_list method
'''
class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task_name):
        """Проверяет, существует ли задача с заданным именем в списке."""
        for task in self.__task_list:
            if task['name'] == task_name:
                return True
        return False

    def add_task(self, task_name):
        """Добавляет задачу в список, если её там ещё нет."""
        if self.__is_task_in_list(task_name):
            print(f'Задача "{task_name}" уже есть в списке')
        else:
            task = {'name': task_name, 'done': False}
            self.__task_list.append(task)
            print(f'Задача "{task_name}" добавлена в список')

    def remove_task(self, task_name):
        """Удаляет задачу из списка, если она существует."""
        if self.__is_task_in_list(task_name):
            self.__task_list = [task for task in self.__task_list if task['name'] != task_name]
            print(f'Задача "{task_name}" удалена из списка')
        else:
            print(f'Задачи "{task_name}" нет в списке')
