'''
Напишите новую функцию index(), которая будет возвращать строку "Test message
The server is running". Оберните эту функцию в декоратор app.route(), указав в качестве эндпоинта '/'.
 Данный эндпоинт будет соответствовать обращению к сайту по дефолтному адресу: http://localhost:5000/.
 добавить обращение по времени
'''
from flask import Flask, request, Response, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def time():
    now = datetime.now()
    return {'time': now}

@app.route('/')
def index():
    return 'Test message The server is running'

@app.route('/add', methods=['POST'])
def add_func():
    num = request.json.get('num')
    if num is None:
        return jsonify({'error': 'num is required'}), 400
    if num > 10:
        return jsonify({'error': 'too much'}), 400
    return jsonify({'result': num + 1})  # Возвращаем словарь с ключом 'result'

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'Hello {name}!', 200

@app.route('/predict', methods=['POST'])
def add_func():
    features = request.json

    if num is None:
        return jsonify({'error': 'num is required'}), 400
    if num > 10:
        return jsonify({'error': 'too much'}), 400
    return jsonify({'result': num + 1})  # Возвращаем словарь с ключом 'result'

if __name__ == '__main__':
    app.run('localhost', 5001)

app.run('localhost', 5001)