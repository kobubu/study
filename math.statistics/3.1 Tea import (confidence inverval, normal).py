'''
Импортёр упаковывает чай в пакеты с номинальным весом 125 грамм.
Известно, что упаковывающая машина работает с известным среднеквадратическим отклонением равным 10 г.
Случайным образом для проверки было выбрано 50 пакетов чая.
Выборочное среднее этих пакетов составило 125,8 г.
Постройте доверительный интервал уровня надёжности 0.95 для среднего веса пакета: 
P{<a<?} =0.95


'''
import scipy.stats as stats
import numpy as np

# Given values
sample_mean = 125.8  # Sample mean in grams
sigma = 10           # Population standard deviation in grams
n = 50               # Sample size
confidence_level = 0.95

# Calculate standard error
SE = sigma / np.sqrt(n)

# Calculate confidence interval
confidence_interval = stats.norm.interval(confidence_level, loc=sample_mean, scale=SE)

# Print the confidence interval
print(f"The {confidence_level*100}% confidence interval for the mean weight is ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f}) grams.")

# В предыдущей задаче найдите объём выборки , при котором длина доверительного интервала будет равна 2г.
# Заданные значения
sigma = 10           # стандартное отклонение генеральной совокупности в граммах
confidence_level = 0.95
interval_width = 2   # ширина доверительного интервала в граммах

# Вычисление погрешности (E)
E = interval_width / 2

# Вычисление z-значения для заданного доверительного уровня
z = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Вычисление необходимого объема выборки
n = (z * sigma / E) ** 2

# Округление в большую сторону
n = np.ceil(n)

# Вывод результатов
print(f"Необходимый объем выборки для получения доверительного интервала шириной {interval_width} грамм: {int(n)} пакетов.")
