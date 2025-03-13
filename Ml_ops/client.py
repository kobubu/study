import requests
import numpy as np

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    vector = np.array(a)

    # Преобразуем numpy.ndarray в список
    vector_list = vector.tolist()

    # Отправляем POST-запрос с JSON-телом
    r = requests.post('http://localhost:5001/predict', json={'features': vector_list})

    print(r.status_code)
    if r.status_code == 200:
        print(r.json()['prediction'])
    else:
        print(r.text)
