'''
Напишите функцию shuffle_seed(array), которая принимает на вход массив из чисел,
генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает кортеж: 
еремешанный с данным seed массив (исходный массив должен оставаться без изменений), а также seed, с которым этот массив был получен.
'''
import numpy as np
from numpy import random

def shuffle_seed(array):
    seed = np.random.randint(0, 2**32-1)
    np.random.seed(seed)
    shuffled_array = np.random.permutation(array)
    return shuffled_array, seed
