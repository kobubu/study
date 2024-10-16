'''
Вы разрабатываете систему управления звуковым оборудованием в театре.

У вас есть базовый класс SoundEquipment с методом switch_on(), который включает оборудование, и методом switch_off(), который выключает оборудование.
Создайте два дочерних класса: Microphone и Speaker. Оба должны наследоваться от SoundEquipment.
В классе Microphone должен быть инициализатор, который задает уровень громкости — volume (от 0 до 10) и состояние — state (включен/выключен).
Также этот класс должен содержать метод adjust_volume(), который позволяет изменять уровень громкости на переданную в качестве аргумента величину. После изменения уровня громкости метод должен выводить на экран фразу в формате "Volume is now <volume>".
В классе Speaker должен быть инициализатор, который задаёт уровень басов — bass (от 0 до 10) и состояние — state (включен/выключен).
Этот класс должен содержать метод adjust_bass(), который позволяет изменять уровень басов на переданную в качестве аргумента величину. После изменения уровня громкости метод должен выводить на экран фразу в формате "Bass level is now <bass>".
Пример использования классов

# Создаём объект микрофон с громкостью 5 состоянием "включен"
mic = Microphone(volume=5, state=True)
# Отключаем микрофон
mic.switch_off()
# Устаналиваем новый уровень громкости
mic.adjust_volume(7)

# Volume is now 7
# Создаём объект динамик с уровнем бассов 7 и состоянием "выключен"
sp = Speaker(7, False)
# Включили динамик
sp.switch_on()
# Устаналиваем новый уровень бассов
sp.adjust_bass(8)

# Bass level is now 8
Обратите внимание, что создавать экземпляры классов не нужно, необходимо только объявить классы. После того, как вы протестируете работу классов на приведенных примерах, и перед тем, как отправить код на проверку, не забудьте удалить все, кроме объявления класса.
'''

class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False


class Microphone(SoundEquipment):
    def __init__(self, volume, state):
        self.volume = volume
        self.state = state

    def adjust_volume(self, volume):
        self.volume = volume
        print(f'Volume is now {self.volume}')

class Speaker(SoundEquipment):
    def __init__(self, bass, state):
        self.bass = bass
        self.state = state

    def adjust_bass(self, bass):
        self.bass = bass
        print(f'Bass level is now {self.bass}')















