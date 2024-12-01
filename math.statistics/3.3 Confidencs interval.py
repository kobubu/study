'''
По выборке объёма n=17
вычислено выборочное среднее xˉ 20.5 мм
выборочная смещенная дисперсия S^2 = 16 мм диаметра валиков.
Постройте доверительные интервалы уровня надёжности 0.9
для среднего значения диаметра валика и для дисперсии диаметра валика.
Предполагается, что диаметры валиков имеют нормальное ра.преде.ление.
Впишите в поле для ответа границы интервала через запятую
Округлите значения до второго знака после запятой. Пример: 0.44, 0.56
Приводить дисперсию к несмещенному варианту не нужно.
'''
import scipy.stats as stats
import numpy as np

# Заданные значения
n = 17               # объем выборки
sample_mean = 20.5   # выборочное среднее
sample_variance = 16 # выборочная дисперсия
confidence_level = 0.9

# Вычисление доверительного интервала для среднего диаметра
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=n-1)
margin_of_error = t_critical * np.sqrt(sample_variance / n)
mean_ci_lower = sample_mean - margin_of_error
mean_ci_upper = sample_mean + margin_of_error

# Вычисление доверительного интервала для дисперсии диаметра
chi2_lower = stats.chi2.ppf((1 - confidence_level) / 2, df=n-1)
chi2_upper = stats.chi2.ppf((1 + confidence_level) / 2, df=n-1)
variance_ci_lower = (n * sample_variance) / chi2_upper
variance_ci_upper = (n * sample_variance) / chi2_lower

# Вывод результатов
print(f"Доверительный интервал для среднего диаметра: ({mean_ci_lower:.2f}, {mean_ci_upper:.2f})")
print(f"Доверительный интервал для дисперсии диаметра: ({variance_ci_lower:.2f}, {variance_ci_upper:.2f})")
