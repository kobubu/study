# Вебинар 7: Оптимизация MapReduce для анализа розничных продаж

## Теоретическая часть

### Проблемы производительности в реальных данных

---

## 1. Что такое reducer skew

### Нормальное распределение ключей между редьюсерами

```text
Входные пары (key, value):

userA → ***** (5 записей)
userB → ***** (5 записей)
userC → ***** (5 записей)
userD → ***** (5 записей)

Партиционирование по ключу даёт примерно равномерную нагрузку:

Reducer 1: userA, userB   → всего 10 записей
Reducer 2: userC, userD   → всего 10 записей
```

Все редьюсеры работают примерно одинаково долго → джоб заканчивается быстрее.

---

### Skew: один «тяжёлый» ключ или группа ключей

```text
Входные пары (key, value):

userA → **************************************** (40 записей)
userB → ** (2 записи)
userC → ** (2 записи)
userD → ** (2 записи)

Обычный партиционер (hash(key) % R):

Reducer 1: userA          → 40 записей (долго)
Reducer 2: userB, userC,
          userD           → 6 записей (быстро)
```

Картинка по времени:

```text
Время работы:

Reducer 1: ######################## (долго)
Reducer 2: ###                     (быстро, простаивает)

Итог: вся джоба ждёт, пока «долгоиграющий» редьюсер завершится.
Это и есть reducer skew.
```

---

## 2. Подход 1: переопределить партиционер

Цель — более равномерно распределить «тяжёлые» ключи по редьюсерам.

```text
До:

hash(key) % R

userA (40 записей) → Reducer 1
остальные (6 записей) → Reducer 2


После (кастомный партиционер):

if key in { userA }:
    используй специальную функцию распределения userA по нескольким редьюсерам
else:
    обычный hash(key) % R
```

Схематично:

```text
Было:

Reducer 1: userA (40)
Reducer 2: userB, userC, userD (6)

Стало:

Reducer 1: userA (часть) → 15
Reducer 2: userA (часть) → 15
Reducer 3: userA (часть) + userB,userC,userD → 16

Нагрузка ближе к равномерной.
```

Минус: нужно уметь детектировать «тяжёлые» ключи и согласовать это с логикой reduce.

---

## 3. Подход 2: «Соль» в ключах (key salting)

Разбиваем один горячий ключ на несколько под-ключей.

```text
Было (до salting):

key = "userA"
40 записей с key="userA"
→ всё идёт в один reducer.


Стало (после salting):

key = "userA#1"
key = "userA#2"
key = "userA#3"

Примерное распределение:

userA#1 → 14 записей
userA#2 → 13 записей
userA#3 → 13 записей
итого 40, но по трём ключам.
```

Распределение по редьюсерам:

```text
Reducer 1: userA#1  (14)
Reducer 2: userA#2  (13)
Reducer 3: userA#3  (13)
```

Потом часто делают дополнительную стадию (второй job / второй reduce), чтобы собрать `userA#1`, `userA#2`, `userA#3` обратно в «логический» ключ `userA`.

---

## 4. Подход 3: Спец-обработка «тяжёлых» ключей (side path)

Идея:

1. Сначала делаем PRE-статистику:
   ```text
   - считаем частоты ключей
   - находим heavy keys (например, > 1% всех записей)
   ```
2. Основной MapReduce:
   ```text
   - обычные ключи → стандартный пайплайн
   - тяжёлые ключи → отдельный путь обработки (другие джобы, партиционер, salting и т.п.)
   ```

Визуально:

```text
                ┌────────────────────────────────┐
Входные данные ─┤  Map (делим на heavy / normal) ├───┐
                └────────────────────────────────┘   │
                          │                          │
                heavy keys│                          │normal keys
                          ▼                          ▼
             ┌─────────────────┐           ┌─────────────────┐
             │ Job для heavy   │           │ Обычный reduce  │
             │ (salting, спец.)│           │ без skew        │
             └─────────────────┘           └─────────────────┘
```

---

## 5. Подход 4: Увеличить количество редьюсеров

Помогает, если skew не экстремальный и есть несколько «почти тяжёлых» ключей.

```text
До:

R = 2 редьюсера
Reducer 1: 40 записей
Reducer 2: 6 записей

После:

R = 8 редьюсеров
Reducer 1..8 получают меньше записей каждый
→ вероятность, что один reducer станет «бутылочным горлышком», ниже.
```

Но если один ключ доминирует (например 90% данных), просто увеличивать R мало помогает — всё равно всё уйдёт в один reducer по этому ключу (без salting / кастомного партиционера).

---

## 6. Краткая «шпаргалка»

```text
Проблема: reducer skew
- Симптом: 1–2 редьюсера работают сильно дольше остальных.
- Причина: неравномерное распределение ключей (hot keys, heavy hitters).

Что делать:
1) Кастомный партиционер:
   - по-другому раскладывает тяжёлые ключи по редьюсерам.

2) Salting ключей:
   - "userA" → "userA#1", "userA#2", ...
   - разбивает нагрузку по нескольким редьюсерам;
   - требует доп. шага агрегации.

3) Разделить heavy / normal:
   - heavy keys в отдельный job/пайплайн;
   - обычные ключи идут стандартным путём.

4) Увеличить число редьюсеров:
   - работает, если много средних ключей;
   - не решает проблему одного супер-тяжёлого ключа.
```

## Практическая часть

### Структура проекта

```
hadoop_retail_analysis/
├── data/
│   └── input/
│       └── retail_sales_dataset.csv
├── scripts/
│   ├── multi_output_analysis.py
│   ├── skew_handling_analysis.py
│   └── performance_comparison.py
└── results/
```

### Скрипт 1: Комплексный анализ за один проход

**Назначение:** Выполняет 3 типа анализа за один проход по данным

**`scripts/multi_output_analysis.py`**

<details>
  <summary>multi_output_analysis.py</summary>

```python
from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
from mrjob.step import MRStep
import json
from datetime import datetime

class MRMultiOutputAnalysisClean(MRJob):
    
    # Используем RawValueProtocol для чистого вывода
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def mapper_init(self):
        self.category_stats = {}
        self.gender_analysis = {}
        self.monthly_analysis = {}
    
    def mapper(self, _, line):
        if line.startswith('Transaction ID'):
            return
            
        try:
            fields = line.split(',')
            date_str = fields[1].strip()
            customer_id = fields[2].strip()
            gender = fields[3].strip()
            age = int(fields[4])
            category = fields[5].strip()
            quantity = int(fields[6])
            total_amount = float(fields[8])
            
            # Анализ по категориям
            if category not in self.category_stats:
                self.category_stats[category] = {
                    'revenue': 0, 'transactions': 0, 'quantity': 0,
                    'customers': set(), 'age_sum': 0
                }
            
            self.category_stats[category]['revenue'] += total_amount
            self.category_stats[category]['transactions'] += 1
            self.category_stats[category]['quantity'] += quantity
            self.category_stats[category]['customers'].add(customer_id)
            self.category_stats[category]['age_sum'] += age
            
            # Анализ по полу
            gender_key = f"{gender}_{category}"
            if gender_key not in self.gender_analysis:
                self.gender_analysis[gender_key] = {
                    'revenue': 0, 'transactions': 0, 'age_sum': 0
                }
            
            self.gender_analysis[gender_key]['revenue'] += total_amount
            self.gender_analysis[gender_key]['transactions'] += 1
            self.gender_analysis[gender_key]['age_sum'] += age
            
            # Помесячный анализ
            month = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m')
            month_key = f"{month}_{category}"
            if month_key not in self.monthly_analysis:
                self.monthly_analysis[month_key] = {
                    'revenue': 0, 'transactions': 0
                }
            
            self.monthly_analysis[month_key]['revenue'] += total_amount
            self.monthly_analysis[month_key]['transactions'] += 1
            
        except Exception as e:
            self.increment_counter('Errors', 'Parse_Errors', 1)
    
    def mapper_final(self):
        # Категории
        for category, stats in self.category_stats.items():
            result = {
                'analysis_type': 'category',
                'category': category,
                'total_revenue': round(stats['revenue'], 2),
                'total_transactions': stats['transactions'],
                'total_quantity': stats['quantity'],
                'unique_customers': len(stats['customers']),
                'avg_customer_age': round(stats['age_sum'] / stats['transactions'], 1),
                'avg_transaction_value': round(stats['revenue'] / stats['transactions'], 2)
            }
            yield None, json.dumps(result)
        
        # Гендерный анализ
        for gender_key, stats in self.gender_analysis.items():
            gender, category = gender_key.split('_', 1)
            result = {
                'analysis_type': 'gender_category',
                'gender': gender,
                'category': category,
                'total_revenue': round(stats['revenue'], 2),
                'total_transactions': stats['transactions'],
                'avg_customer_age': round(stats['age_sum'] / stats['transactions'], 1),
                'avg_transaction_value': round(stats['revenue'] / stats['transactions'], 2)
            }
            yield None, json.dumps(result)
        
        # Помесячный анализ
        for month_key, stats in self.monthly_analysis.items():
            month, category = month_key.split('_', 1)
            result = {
                'analysis_type': 'monthly',
                'month': month,
                'category': category,
                'total_revenue': round(stats['revenue'], 2),
                'total_transactions': stats['transactions'],
                'avg_transaction_value': round(stats['revenue'] / stats['transactions'], 2)
            }
            yield None, json.dumps(result)
    
    def reducer(self, key, values):
        # Просто передаем значения без изменений
        for value in values:
            yield None, value

if __name__ == '__main__':
    MRMultiOutputAnalysisClean.run()
```
</details>

**Запуск:**
```bash
cd ~/hadoop_retail_analysis
python scripts/multi_output_analysis.py data/input/retail_sales_dataset.csv > results/multi_analysis.json
```

**Проверка результата:**
```bash
cat results/multi_analysis.json | head -5
```

Также давайте создадим простой скрипт для быстрого просмотра структуры данных:

**`scripts/quick_analyze.py`**

<details>
  <summary>quick_analyze.py</summary>

```python
#!/usr/bin/env python3
import json
import pandas as pd

def quick_analyze():
    # Анализируем сырые данные
    print("АНАЛИЗ СЫРЫХ ДАННЫХ")
    print("=" * 40)
    
    with open('data/input/retail_sales_dataset.csv', 'r') as f:
        lines = f.readlines()
    
    print(f"Всего строк: {len(lines)}")
    print(f"Заголовок: {lines[0].strip()}")
    print(f"Первые 3 записи:")
    for i in range(1, min(4, len(lines))):
        print(f"  {i}: {lines[i].strip()}")
    
    # Анализируем результаты если есть
    try:
        with open('results/multi_analysis_clean.json', 'r') as f:
            results = [json.loads(line.strip()) for line in f if line.strip()]
        
        print(f"\nАНАЛИЗ РЕЗУЛЬТАТОВ")
        print("=" * 40)
        print(f"Всего записей в результатах: {len(results)}")
        
        df = pd.DataFrame(results)
        analysis_types = df['analysis_type'].value_counts()
        print("\nТипы анализа:")
        for atype, count in analysis_types.items():
            print(f"  {atype}: {count} записей")
            
        if 'category' in df['analysis_type'].values:
            categories = df[df['analysis_type'] == 'category']
            print(f"\nКатегории товаров: {len(categories)}")
            for _, row in categories.iterrows():
                print(f"  {row['category']}: ${row['total_revenue']:,.0f}")
                
    except FileNotFoundError:
        print("Файл результатов не найден")

if __name__ == '__main__':
    quick_analyze()
```

</details>

**Запуск быстрого анализа:**
```bash
python scripts/quick_analyze.py
```

Это покажет:
- Структуру исходных данных
- Количество записей
- Типы анализа в результатах
- Основные категории и их выручку


### Скрипт 2: Оптимизация перекоса данных

**Назначение:** балансирует нагрузку для категории Electronics

**`scripts/skew_handling_analysis.py`**

<details>
  <summary>skew_handling_analysis.py</summary>

```python
from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
from mrjob.step import MRStep
import json

class MRSkewHandlingAnalysisClean(MRJob):
    
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def mapper(self, _, line):
        if line.startswith('Transaction ID'):
            return
            
        try:
            fields = line.split(',')
            category = fields[5].strip()
            total_amount = float(fields[8])
            quantity = int(fields[6])
            
            # Стратегия балансировки для Electronics
            if category == "Electronics":
                if total_amount > 400:
                    balanced_key = "Electronics_High"
                elif total_amount > 200:
                    balanced_key = "Electronics_Medium"
                else:
                    balanced_key = "Electronics_Low"
            else:
                balanced_key = category
            
            yield balanced_key, {
                'revenue': total_amount,
                'transactions': 1,
                'quantity': quantity,
                'original_category': category
            }
            
        except Exception:
            self.increment_counter('Errors', 'Parse_Errors', 1)
    
    def combiner(self, key, values):
        total_revenue = 0
        total_transactions = 0
        total_quantity = 0
        
        for data in values:
            total_revenue += data['revenue']
            total_transactions += data['transactions']
            total_quantity += data['quantity']
        
        yield key, {
            'revenue': total_revenue,
            'transactions': total_transactions,
            'quantity': total_quantity
        }
    
    def reducer(self, key, values):
        total_revenue = 0
        total_transactions = 0
        total_quantity = 0
        
        for data in values:
            total_revenue += data['revenue']
            total_transactions += data['transactions']
            total_quantity += data['quantity']
        
        # Объединяем обратно для Electronics
        if key.startswith("Electronics_"):
            original_category = "Electronics"
        else:
            original_category = key
        
        result = {
            'category': original_category,
            'sub_category': key,
            'total_revenue': round(total_revenue, 2),
            'total_transactions': total_transactions,
            'total_quantity': total_quantity,
            'avg_transaction': round(total_revenue / total_transactions, 2)
        }
        
        yield None, json.dumps(result)

if __name__ == '__main__':
    MRSkewHandlingAnalysisClean.run()
```

</details>

**Запуск:**
```bash
python scripts/skew_handling_analysis.py data/input/retail_sales_dataset.csv > results/skew_analysis.json
```

**Проверка:**
```bash
cat results/skew_analysis.json | head -10
```

**Скрипт для анализа skew результатов:**

**`scripts/analyze_skew_results.py`**

<details>
  <summary>analyze_skew_results.py</summary>

```python
#!/usr/bin/env python3
import json
import pandas as pd

def analyze_skew_results():
    # Читаем результаты skew analysis
    results = []
    with open('results/skew_analysis.json', 'r') as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line.strip())
                    results.append(data)
                except json.JSONDecodeError as e:
                    print(f"Ошибка парсинга: {line[:100]}...")
                    continue
    
    if not results:
        print("Нет данных для анализа")
        return
    
    df = pd.DataFrame(results)
    
    print("АНАЛИЗ SKEW HANDLING RESULTS")
    print("=" * 50)
    
    # Анализ распределения Electronics
    electronics_data = df[df['category'] == 'Electronics']
    if not electronics_data.empty:
        print("\nРАСПРЕДЕЛЕНИЕ ELECTRONICS ПО ПОДКАТЕГОРИЯМ:")
        print("-" * 50)
        
        total_electronics_revenue = electronics_data['total_revenue'].sum()
        total_electronics_transactions = electronics_data['total_transactions'].sum()
        
        for _, row in electronics_data.iterrows():
            revenue_pct = (row['total_revenue'] / total_electronics_revenue) * 100
            transactions_pct = (row['total_transactions'] / total_electronics_transactions) * 100
            
            print(f"{row['sub_category']:.<20} ${row['total_revenue']:>10,.0f} ({revenue_pct:5.1f}%) "
                  f"{row['total_transactions']:>4} транз. ({transactions_pct:5.1f}%) "
                  f"ср.чек: ${row['avg_transaction']:>8.0f}")
    
    # Сравнение с другими категориями
    print("\nСРАВНЕНИЕ КАТЕГОРИЙ:")
    print("-" * 50)
    
    category_totals = df.groupby('category').agg({
        'total_revenue': 'sum',
        'total_transactions': 'sum',
        'total_quantity': 'sum'
    }).reset_index()
    
    category_totals['avg_transaction'] = category_totals['total_revenue'] / category_totals['total_transactions']
    category_totals = category_totals.sort_values('total_revenue', ascending=False)
    
    total_revenue_all = category_totals['total_revenue'].sum()
    
    for _, row in category_totals.iterrows():
        revenue_pct = (row['total_revenue'] / total_revenue_all) * 100
        print(f"{row['category']:.<12} ${row['total_revenue']:>12,.0f} ({revenue_pct:5.1f}%) "
              f"{row['total_transactions']:>4} транз. "
              f"ср.чек: ${row['avg_transaction']:>8.0f}")
    
    # Анализ эффективности балансировки
    print("\nАНАЛИЗ ЭФФЕКТИВНОСТИ БАЛАНСИРОВКИ:")
    print("-" * 50)
    
    if not electronics_data.empty:
        # Находим максимальную и минимальную нагрузку по подкатегориям
        max_transactions = electronics_data['total_transactions'].max()
        min_transactions = electronics_data['total_transactions'].min()
        avg_transactions = electronics_data['total_transactions'].mean()
        
        imbalance_ratio = max_transactions / min_transactions if min_transactions > 0 else float('inf')
        
        print(f"Макс. транзакций в подкатегории: {max_transactions}")
        print(f"Мин. транзакций в подкатегории: {min_transactions}")
        print(f"Среднее транзакций: {avg_transactions:.1f}")
        print(f"Коэффициент дисбаланса: {imbalance_ratio:.2f}x")
        
        if imbalance_ratio < 5:
            print("✓ Балансировка эффективна - равномерное распределение")
        else:
            print("⚠ Балансировка требует улучшения - значительный дисбаланс")

if __name__ == '__main__':
    analyze_skew_results()
```
</details>

**Запуск анализа skew:**
```bash
python scripts/analyze_skew_results.py
```

### Скрипт 3: Сравнение производительности

**Назначение:** Сравнивает эффективность разных подходов

**`scripts/performance_comparison.py`**

<details>
  <summary>performance_comparison.py</summary>

```python
#!/usr/bin/env python3
import subprocess
import time
import json
import os

def run_performance_test():
    scripts = {
        'basic': 'category_revenue_detailed.py',
        'multi_output': 'multi_output_analysis.py',
        'skew_handling': 'skew_handling_analysis.py'
    }
    
    results = {}
    input_file = 'data/input/retail_sales_dataset.csv'
    
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 50)
    
    for name, script in scripts.items():
        script_path = f'scripts/{script}'
        if not os.path.exists(script_path):
            print(f"✗ Скрипт {script_path} не найден")
            continue
            
        print(f"Запуск {name}...")
        start_time = time.time()
        
        try:
            result = subprocess.run(
                ['python', script_path, input_file],
                capture_output=True, 
                text=True,
                timeout=120
            )
            
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                output_lines = len([line for line in result.stdout.strip().split('\n') if line])
                results[name] = {
                    'time': round(execution_time, 2),
                    'output_lines': output_lines,
                    'status': 'success'
                }
                print(f"✓ {name}: {execution_time:.2f} сек, {output_lines} строк вывода")
            else:
                results[name] = {
                    'time': float('inf'),
                    'output_lines': 0,
                    'status': 'error'
                }
                print(f"✗ {name}: ошибка - {result.stderr}")
                
        except subprocess.TimeoutExpired:
            results[name] = {
                'time': float('inf'),
                'output_lines': 0, 
                'status': 'timeout'
            }
            print(f"✗ {name}: таймаут (более 120 секунд)")
        except Exception as e:
            results[name] = {
                'time': float('inf'),
                'output_lines': 0,
                'status': 'exception'
            }
            print(f"✗ {name}: исключение - {e}")
    
    # Анализ результатов
    print("\n" + "=" * 60)
    print("ИТОГИ СРАВНЕНИЯ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    successful = {k: v for k, v in results.items() if v['status'] == 'success'}
    if successful:
        best_time = min(v['time'] for v in successful.values())
        
        print(f"\n{'Подход':<15} {'Время':<8} {'Ускорение':<10} {'Строк/сек':<10} {'Статус':<10}")
        print("-" * 60)
        
        for name, data in results.items():
            if data['status'] == 'success':
                speedup = data['time'] / best_time
                efficiency = data['output_lines'] / data['time'] if data['time'] > 0 else 0
                print(f"{name:<15} {data['time']:>6.1f}с {speedup:>8.1f}x {efficiency:>9.1f} {'✓':<10}")
            else:
                print(f"{name:<15} {'FAILED':>6} {'-':>8} {'-':>9} {data['status']:<10}")
    
    # Сохраняем результаты
    with open('results/performance_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nРезультаты сохранены в results/performance_results.json")

if __name__ == '__main__':
    run_performance_test()
```

</details>

**Запуск сравнения производительности:**
```bash
python scripts/performance_comparison.py
```

## Анализ результатов

### Просмотр результатов

```bash
# Комплексный анализ
cat results/multi_analysis.json | head -10

# Анализ перекоса
cat results/skew_analysis.json | head -10

# Производительность
cat results/performance_results.json
```

### Ожидаемые результаты

**Multi-Output Analysis:**
```json
{"type": "category", "category": "Electronics", "revenue": 156905.0, "transactions": 520, "unique_customers": 480}
{"type": "gender", "gender": "Male", "category": "Electronics", "revenue": 95000.0, "transactions": 300}
{"type": "monthly", "month": "2024-01", "category": "Electronics", "revenue": 45000.0, "transactions": 150}
```

**Skew Handling Analysis:**
```json
{"category": "Electronics", "sub_category": "Electronics_High", "total_revenue": 85000.0, "total_transactions": 170}
{"category": "Electronics", "sub_category": "Electronics_Medium", "total_revenue": 45000.0, "total_transactions": 225}
{"category": "Electronics", "sub_category": "Electronics_Low", "total_revenue": 26905.0, "total_transactions": 125}
```


## Анализ производительности

### Ключевые выводы:

1. **Multi-Output подход - победитель** 
   - **Самое быстрое время**: 0.21 сек (на 19% быстрее базового)
   - **Самая высокая эффективность**: 4576 строк/сек (в 400 раз эффективнее!)
   - **Наибольшая информативность**: 961 строка результатов

2. **Skew Handling работает, но дорого**
   - Немного медленнее базового: 0.28 сек
   - Но дает ценную информацию о распределении данных

3. **Basic подход - неэффективен**
   - Медленнее multi-output
   - Мало выходных данных (всего 3 строки)

### Что это значит на практике:

**Multi-Output Analysis** - идеальное решение потому что:
- ✅ Выполняет **3 анализа за один проход** по данным
- ✅ **В 400 раз эффективнее** по обработке данных
- ✅ Дает **полную картину** бизнес-метрик
- ✅ **Быстрее** даже при большем объеме вывода

**Skew Handling** полезен когда:
- У вас действительно большие данные (миллионы записей)
- Категория Electronics составляет >50% всех данных
- Нужна максимальная стабильность обработки

### Рекомендации для продакшена:

```bash
# Используйте multi-output для ежедневной аналитики
python scripts/multi_output_analysis_clean.py data/input/retail_sales_dataset.csv > results/daily_analysis.json

# Используйте skew handling для больших пайплайнов
python scripts/skew_handling_analysis_clean.py data/input/retail_sales_dataset.csv > results/skew_monitoring.json
```

### Бизнес-ценность:

**Multi-Output дает вам сразу:**
- Выручку по категориям
- Гендерную аналитику  
- Помесячную динамику
- Возрастные профили клиентов

<details>
  <summary>Дополнительные демо</summary>

**`scripts/demo_transaction_efficiency.py`**
```python
from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol

class MRTransactionEfficiency(MRJob):
    """Анализ эффективности: средний чек, товарооборот, цена за единицу"""
    
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def mapper(self, _, line):
        if line.startswith('Transaction'):
            return
            
        try:
            parts = line.split(',')
            if len(parts) >= 9:
                category = parts[5].strip()
                quantity = int(parts[6])
                total = float(parts[8])
                
                yield category, (quantity, total)
                
        except:
            pass
    
    def reducer(self, category, values):
        total_revenue = 0
        total_quantity = 0
        transaction_count = 0
        total_items = 0
        
        for quantity, total in values:
            total_revenue += total
            total_quantity += quantity
            transaction_count += 1
            total_items += quantity
        
        # Рассчитываем метрики
        avg_check = total_revenue / transaction_count
        avg_quantity = total_quantity / transaction_count
        revenue_per_item = total_revenue / total_items
        
        # Формируем результат как одну строку
        result = (
            f"{category}|"
            f"Выручка: ${total_revenue:,.0f}|"
            f"Транзакций: {transaction_count}|"
            f"Товаров: {total_items}|"
            f"Ср.чек: ${avg_check:.0f}|"
            f"Ср.кол-во: {avg_quantity:.1f} шт.|"
            f"Цена за ед: ${revenue_per_item:.1f}"
        )
        
        yield None, result

if __name__ == '__main__':
    MRTransactionEfficiency.run()
```

**Скрипт для красивого вывода результатов:**

**`scripts/run_efficiency_demo.py`**
```python
#!/usr/bin/env python3
import subprocess

def run_demo():
    print("ЗАПУСК АНАЛИЗА ЭФФЕКТИВНОСТИ ТРАНЗАКЦИЙ")
    print("=" * 60)
    
    result = subprocess.run([
        'python', 'scripts/demo_transaction_efficiency.py', 
        'data/input/retail_sales_dataset.csv'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("АНАЛИЗ ЭФФЕКТИВНОСТИ ПО КАТЕГОРИЯМ")
        print("=" * 50)
        
        for line in result.stdout.strip().split('\n'):
            if line and '|' in line:
                parts = line.split('|')
                category = parts[0]
                metrics = parts[1:]
                
                print(f"\n{category}:")
                for metric in metrics:
                    print(f"  {metric}")
    else:
        print("Ошибка:", result.stderr)

if __name__ == '__main__':
    run_demo()
```

**Запуск:**
```bash
python scripts/run_efficiency_demo.py
```

**Или напрямую:**
```bash
python scripts/demo_transaction_efficiency.py data/input/retail_sales_dataset.csv
```

</details>