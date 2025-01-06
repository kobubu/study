import pandas as pd

def create_medications(names, counts):
    # Создаем Series, где индексы - это названия лекарств, а значения - их количество
    medications = pd.Series(data=counts, index=names)
    return medications

def get_percent(medications, name):
    # Вычисляем общее количество товаров в поставке
    total_count = medications.sum()
    
    # Получаем количество товара с указанным именем
    specific_count = medications.get(name, 0)
    
    # Вычисляем долю в процентах
    if total_count == 0:
        return 0
    else:
        return (specific_count / total_count) * 100

# Пример использования:
names = ['chlorhexidine', 'cyntomycin', 'afobazol']
counts = [15, 18, 7]

medications = create_medications(names, counts)
print(medications)

percent = get_percent(medications, 'cyntomycin')
print(f"Доля товара 'cyntomycin' в поставке: {percent:.2f}%")
