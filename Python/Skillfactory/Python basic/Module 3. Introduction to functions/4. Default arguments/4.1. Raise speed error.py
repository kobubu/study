'''
Попробуйте добавить в функцию get_time проверку скорости на равенство нулю. Если скорость равна нулю, верните ValueError с сообщением "Speed cannot be equal to 0!". словаря используйте переменную с именем word_dict.
'''

# Введите свое решение ниже
def get_time(distance, speed):
    if distance < 0 or speed < 0:
        raise ValueError("Distance or speed cannot be below 0!")
    elif speed == 0:
        raise ValueError("Speed cannot be equal to 0!")
    return distance / speed
