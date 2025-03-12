'''
Напишите новую функцию index(), которая будет возвращать строку "Test message
The server is running". Оберните эту функцию в декоратор app.route(), указав в качестве эндпоинта '/'.
 Данный эндпоинт будет соответствовать обращению к сайту по дефолтному адресу: http://localhost:5000/.
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test message The server is running'


@app.route('/hello')
def hello_func():
    return 'Hello!'

if __name__ == 'main':
    app.run('localhost', 5001)

app.run('localhost', 5001)
