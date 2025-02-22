import numpy as np
from collections import defaultdict

def train(data: str) -> dict:
    # Разбиваем входную строку на слова
    words = data.split()
    
    # Если строка пустая, возвращаем пустой словарь
    if not words:
        return {}
    
    # Создаем список уникальных слов (словарь)
    vocab = list(set(words))
    
    # Создаем словарь для сопоставления слов с их индексами
    word2id = {word: i for i, word in enumerate(vocab)}
    
    # Размер словаря (количество уникальных слов)
    vocab_size = len(vocab)
    
    # Размерность векторов эмбеддингов
    vector_size = 100
    
    # Размер окна для контекста (сколько слов слева и справа учитывать)
    window_size = 5
    
    # Скорость обучения (шаг градиентного спуска)
    learning_rate = 0.025
    
    # Количество эпох (итераций по данным)
    epochs = 10
    
    # Количество негативных примеров для отрицательного сэмплирования
    neg_samples = 5

    # Инициализация входных эмбеддингов (векторы для каждого слова)
    np.random.seed(42)  # Фиксируем случайное состояние для воспроизводимости
    input_emb = np.random.normal(0, 0.1, (vocab_size, vector_size))
    
    # Инициализация выходных эмбеддингов (векторы для контекстных слов)
    output_emb = np.random.normal(0, 0.1, (vocab_size, vector_size))

    # Подготовка данных для отрицательного сэмплирования
    # Считаем частоту каждого слова в тексте
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    
    # Преобразуем частоты в массив и применяем степенное преобразование (0.75)
    word_freq = np.array([word_counts[word] for word in vocab], dtype=np.float32)
    word_freq = np.power(word_freq, 0.75)
    
    # Нормализуем частоты, чтобы получить вероятности для отрицательного сэмплирования
    word_probs = word_freq / np.sum(word_freq)

    # Генерация обучающих примеров (пар целевое слово - контекстное слово)
    training_pairs = []
    for i, target in enumerate(words):
        # Определяем границы окна для контекста
        start = max(0, i - window_size)
        end = min(len(words), i + window_size + 1)
        
        # Проходим по всем словам в окне
        for j in range(start, end):
            # Исключаем само целевое слово и выходим за пределы списка
            if j != i and j < len(words):
                context = words[j]
                # Добавляем пару (индекс целевого слова, индекс контекстного слова)
                training_pairs.append((word2id[target], word2id[context]))

    # Обучение модели
    for epoch in range(epochs):
        # Перемешиваем пары для каждой эпохи
        np.random.shuffle(training_pairs)
        
        # Проходим по всем парам
        for target_id, context_id in training_pairs:
            # Входной вектор для целевого слова
            input_vec = input_emb[target_id]
            
            # Выходной вектор для контекстного слова
            output_vec = output_emb[context_id]
            
            # Вычисляем скалярное произведение (оценка близости)
            score = np.dot(input_vec, output_vec)
            
            # Вычисляем градиент для позитивного примера
            grad = 1 / (1 + np.exp(-score)) - 1  # Производная лосса
            
            # Обновляем входной вектор
            input_emb[target_id] -= learning_rate * grad * output_vec
            
            # Обновляем выходной вектор
            output_emb[context_id] -= learning_rate * grad * input_vec

            # Негативные примеры
            # Выбираем случайные слова для негативного сэмплирования
            neg_ids = np.random.choice(vocab_size, neg_samples, p=word_probs)
            
            # Обновляем векторы для каждого негативного примера
            for neg_id in neg_ids:
                # Выходной вектор для негативного слова
                neg_vec = output_emb[neg_id]
                
                # Вычисляем скалярное произведение
                score = np.dot(input_vec, neg_vec)
                
                # Вычисляем градиент для негативного примера
                grad = 1 / (1 + np.exp(-score))  # Производная для негативов
                
                # Обновляем входной вектор
                input_emb[target_id] += learning_rate * grad * neg_vec
                
                # Обновляем выходной вектор для негативного слова
                output_emb[neg_id] += learning_rate * grad * input_vec

    # Создание словаря эмбеддингов
    # Возвращаем словарь, где ключ — слово, значение — его эмбеддинг
    return {word: input_emb[word2id[word]] for word in vocab}
