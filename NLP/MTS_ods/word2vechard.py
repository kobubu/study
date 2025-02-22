import numpy as np
from collections import defaultdict

def train(data: str) -> dict:
    # Разделение входной строки на слова
    words = data.split()
    if not words:
        return {}  # Если строка пуста, возвращаем пустой словарь

    # Создание словаря для сопоставления слов с уникальными индексами
    word2id = {}
    # Генерация списка индексов для каждого слова, создание словаря word2id
    indices = [word2id.setdefault(word, len(word2id)) for word in words]
    vocab_size = len(word2id)  # Размер словаря (количество уникальных слов)
    
    # Гиперпараметры модели
    vector_size = 128        # Размер вектора для каждого слова
    window_size = 15         # Размер окна для контекста
    learning_rate = 0.025    # Скорость обучения
    epochs = 300             # Количество эпох обучения
    neg_samples = 25         # Количество негативных примеров для обучения
    batch_size = 1024        # Размер батча для обучения
    l2_lambda = 1e-5         # Коэффициент L2-регуляризации
    
    # Инициализация случайных чисел для воспроизводимости
    np.random.seed(42)
    # Масштабирование для инициализации векторов
    scale = 0.1 / np.sqrt(vector_size)
    # Инициализация входных и выходных векторов
    input_emb = np.random.normal(0, scale, (vocab_size, vector_size))
    output_emb = np.zeros((vocab_size, vector_size))
    
    # Вычисление частот слов для субсемплинга
    word_counts = np.bincount(indices)
    total_words = len(words)
    # Вероятность сохранения слова в зависимости от его частоты
    keep_prob = np.minimum(np.sqrt(1e-5/(word_counts/total_words)), 1.0)
    # Фильтрация индексов слов на основе вероятности сохранения
    valid_indices = np.where(np.random.rand(total_words) < keep_prob[indices])[0]
    
    # Генерация пар (целевое слово, контекстное слово) с весами
    pairs = []
    for i in valid_indices:
        window = np.random.randint(1, window_size + 1)  # Случайный размер окна
        start = max(0, i - window)  # Начало окна
        end = min(total_words, i + window + 1)  # Конец окна
        for j in range(start, end):
            if j != i:
                weight = 1.0/(abs(i-j)+1)  # Вес обратно пропорционален расстоянию
                pairs.append((indices[i], indices[j], weight))
    
    # Преобразование списка пар в массив NumPy
    pairs = np.array(pairs, dtype=np.float32)
    
    # Обучение модели
    for epoch in range(epochs):  # Цикл по количеству эпох обучения
    np.random.shuffle(pairs)  # Перемешивание пар (целевое слово, контекстное слово) для улучшения обучения
    lr = learning_rate * np.exp(-epoch/100)  # Экспоненциальное затухание скорости обучения для стабилизации
    
    # Обучение по батчам
    for i in range(0, len(pairs), batch_size):  # Цикл по батчам
        batch = pairs[i:i+batch_size]  # Выбор текущего батча из пар
        if len(batch) == 0: continue  # Пропуск пустых батчей
        
        # Разделение батча на целевые слова, контекстные слова и веса
        targets, contexts, weights = batch.T.astype(int)  # Преобразование батча в массивы
        input_vecs = input_emb[targets]  # Векторы целевых слов из входной матрицы
        output_vecs = output_emb[contexts]  # Векторы контекстных слов из выходной матрицы
        
        # Обновление векторов для позитивных примеров
        scores = np.sum(input_vecs * output_vecs, axis=1)  # Скалярное произведение векторов
        grads = weights * (1/(1 + np.exp(-scores)) - 1) - l2_lambda * np.linalg.norm(input_vecs, axis=1)  # Градиенты с регуляризацией
        delta = grads[:, None] * output_vecs  # Изменение для входных векторов
        input_emb[targets] -= lr * delta  # Обновление входных векторов
        output_emb[contexts] -= lr * grads[:, None] * input_vecs  # Обновление выходных векторов
        
        # Обновление векторов для негативных примеров
        neg_probs = (word_counts**0.75)/np.sum(word_counts**0.75)  # Вероятности для негативных примеров
        neg_ids = np.random.choice(vocab_size, (len(batch), neg_samples), p=neg_probs)  # Выбор негативных примеров
        neg_vecs = output_emb[neg_ids]  # Векторы негативных примеров
        
        neg_scores = np.einsum('ij,ikj->ik', input_vecs, neg_vecs, optimize=True)  # Скалярное произведение для негативных примеров
        neg_grads = 1/(1 + np.exp(-neg_scores)) - l2_lambda  # Градиенты для негативных примеров
        input_emb[targets] += lr * np.einsum('ik,ikj->ij', neg_grads, neg_vecs, optimize=True)  # Обновление входных векторов
        output_emb[neg_ids] += lr * np.einsum('ik,ij->ikj', neg_grads, input_vecs, optimize=True)  # Обновление выходных векторов

    # Агрессивная нормализация векторов каждые 20 эпох
    if epoch % 20 == 0:  # Проверка, является ли текущая эпоха кратной 20
        norms = np.linalg.norm(input_emb, axis=1, keepdims=True)  # Вычисление норм векторов
        input_emb = input_emb / np.where(norms < 1e-8, 1e-8, norms)  # Нормализация векторов
    
    # Финальная нормализация векторов
    input_emb /= np.linalg.norm(input_emb, axis=1, keepdims=True).clip(1e-8)
    # Возвращение словаря с векторами слов
    return {word: input_emb[word2id[word]] for word in word2id}
