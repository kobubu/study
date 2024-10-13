'''
Вам дан массив mystery:
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)
Получите булевый массив nans_index с информацией о np.nan в массиве mystery:
True - значение пропущено, False - значение не пропущено
В переменную n_nan сохраните число пропущенных значений
Скопируйте массив mystery в массив mystery_new. Заполните пропущенные значения в массиве mystery_new нулями
Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int
Отсортируйте значения в массиве mystery по возрастанию и сохраните результат в переменную array
Сохраните в массив table двухмерный массив, полученный из массива array. В нём должно быть 5 строк и 3 столбца.
 Причём порядок заполнения должен быть по столбцам!
Например,
 1, 2, 3, 4 -> 1    3
               2    4
Сохраните в переменную col средний столбец из table
'''
# Введите свое решение ниже
import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,
                    np.nan,  31244.,  -2365.,  -6974.,
                    -9212., np.nan, -17722.,  16132.,
                    25933.,  np.nan, -16431.,
                    29810.], dtype=np.float32)

nans_index = np.isnan(mystery)
n_nan = np.sum(nans_index)
mystery_new = mystery.copy()
mystery_new[np.isnan(mystery_new)] = 0
mystery_int = mystery.astype(np.int32)
array = np.sort(mystery)
table = array.reshape((5, 3), order='F')
col = table[:, 1]

