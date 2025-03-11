import pickle
'''
asd
'''
import os

model_filename = r"C:\Users\Igor\Downloads\model (1).pkl"

if os.path.getsize(model_filename) == 0:
    print("Ошибка: Файл model.pkl пуст!")
else:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print(model)
a = model.predict([[1, 1, 1, 0.661212487096872]])
print(a)

# Создание словаря из атрибутов модели
data_dict = {
    'a': model.a,  # Значение атрибута a
    'b': model.b   # Значение атрибута b
}

# Сохранение словаря в файл
output_filename = 'output.pkl'
with open(output_filename, 'wb') as file:
    pickle.dump(data_dict, file)

print(f"Словарь сохранен в файл: {output_filename}")
