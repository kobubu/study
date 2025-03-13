from flask import Flask, request, jsonify
from datetime import datetime
import numpy as np
import os
import pickle

# Загрузка модели
model_filename = r"C:\Users\Igor\Downloads\model (3).pkl"

if os.path.getsize(model_filename) == 0:
    print("Ошибка: Файл model.pkl пуст!")
else:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print(model)

# Пример предсказания
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

# Создание Flask-приложения
app = Flask(__name__)

# Эндпоинт для получения текущего времени
@app.route('/time')
def time():
    now = datetime.now()
    return {'time': now.strftime("%Y-%m-%d %H:%M:%S")}

# Главный эндпоинт с сообщением и временем
@app.route('/')
def index():
    now = datetime.now()
    return f"Test message. The server is running. Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# Эндпоинт для приветствия
@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'name is required'}), 400
    return f'Hello {name}!', 200

# Эндпоинт для предсказания
@app.route('/predict', methods=['POST'])
def predict():
    features = request.json.get('features')
    if not features:
        return jsonify({'error': 'features are required'}), 400

    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

# Запуск сервера
if __name__ == '__main__':
    app.run(host='localhost', port=5001)
