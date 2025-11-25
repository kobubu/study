# Retail Data Analysis на MapReduce

### Теория: Архитектура MapReduce



```markdown

         ┌────────────────────────────┐
         │     Входные данные         │
         │      input_data.csv        │
         └─────────────┬──────────────┘
                       │
                       ▼
         ┌────────────────────────────┐
         │        Split               │
         │  Разделение на блоки       │
         └─────────────┬──────────────┘
               ┌───────┴─────────┬───────────┐
               ▼                 ▼           ▼
   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
   │   Map Task 1    │  │   Map Task 2    │  │   Map Task 3    │
   └───────┬─────────┘  └────────┬────────┘  └────────┬────────┘
           │                     │                    │
           └───────────┬─────────┴──────────┬─────────┘
                       ▼                    ▼
              ┌──────────────────────────────────────┐
              │           Shuffle & Sort             │
              │        Группировка по ключам         │
              └───────────┬───────────┬──────────────┘
                          │           │
                 ┌────────┴───┐   ┌───┴────────┐   ┌────────────┐
                 ▼            ▼   ▼            ▼   ▼            ▼
        ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
        │ Reduce Task 1  │ │ Reduce Task 2  │ │ Reduce Task 3  │
        │   Group 1      │ │   Group 2      │ │   Group 3      │
        └──────┬─────────┘ └──────┬─────────┘ └──────┬─────────┘
               │                  │                  │
       ┌───────▼──────┐   ┌───────▼──────┐   ┌───────▼──────┐
       │ Результат 1  │   │ Результат 2  │   │ Результат 3  │
       └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
              └──────────────┬───┴───────────────┬──┘
                             ▼                   ▼
                      ┌────────────────────────────────┐
                      │         Финальный вывод        │
                      └────────────────────────────────┘
```
# Создание полной структуры проекта и просмотр

## Создание всей структуры папок

```bash
# Создаем основную директорию проекта
mkdir -p ~/hadoop_retail_analysis
cd ~/hadoop_retail_analysis

# Создаем всю структуру папок
mkdir -p config data/input data/output scripts logs results

# Проверяем создание
ls -la
```
<details>
  <summary> Создание кластера </summary>

## Создание необходимых файлов

### Создаем docker-compose.yml
```bash
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    restart: always
    ports:
      - 9871:9870
      - 9001:9000
    volumes:
      - hadoop_namenode:/hadoop/dfs/name
      - ./data:/data
      - ./scripts:/scripts
      - ./config:/config
    environment:
      - CLUSTER_NAME=retail_cluster
    env_file:
      - ./config/hadoop.env

  datanode1:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode1
    restart: always
    volumes:
      - hadoop_datanode1:/hadoop/dfs/data
      - ./data:/data
      - ./scripts:/scripts
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    env_file:
      - ./config/hadoop.env
    depends_on:
      - namenode

  datanode2:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode2
    restart: always
    volumes:
      - hadoop_datanode2:/hadoop/dfs/data
      - ./data:/data
      - ./scripts:/scripts
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    env_file:
      - ./config/hadoop.env
    depends_on:
      - namenode

  datanode3:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode3
    restart: always
    volumes:
      - hadoop_datanode3:/hadoop/dfs/data
      - ./data:/data
      - ./scripts:/scripts
    environment:
      - CORE_CONF_fs_defaultFS=hdfs://namenode:9000
    env_file:
      - ./config/hadoop.env
    depends_on:
      - namenode

  resourcemanager:
    image: bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8
    container_name: resourcemanager
    restart: always
    ports:
      - 8089:8088
      - 8032:8032
    depends_on:
      - namenode
    env_file:
      - ./config/hadoop.env

  nodemanager1:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
    container_name: nodemanager1
    restart: always
    volumes:
      - ./scripts:/scripts
    depends_on:
      - namenode
      - resourcemanager
    env_file:
      - ./config/hadoop.env

  nodemanager2:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
    container_name: nodemanager2
    restart: always
    volumes:
      - ./scripts:/scripts
    depends_on:
      - namenode
      - resourcemanager
    env_file:
      - ./config/hadoop.env

  nodemanager3:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
    container_name: nodemanager3
    restart: always
    volumes:
      - ./scripts:/scripts
    depends_on:
      - namenode
      - resourcemanager
    env_file:
      - ./config/hadoop.env

volumes:
  hadoop_namenode:
  hadoop_datanode1:
  hadoop_datanode2:
  hadoop_datanode3:
EOF
```

### Создаем config/hadoop.env
```bash
cat > config/hadoop.env << 'EOF'
CORE_CONF_fs_defaultFS=hdfs://namenode:9000
CORE_CONF_hadoop_http_staticuser_user=root
CORE_CONF_hadoop_proxyuser_hue_hosts=*
CORE_CONF_hadoop_proxyuser_hue_groups=*

HDFS_CONF_dfs_webhdfs_enabled=true
HDFS_CONF_dfs_permissions_enabled=false
HDFS_CONF_dfs_replication=3

YARN_CONF_yarn_log_aggregation_enable=true
YARN_CONF_yarn_resourcemanager_recovery_enabled=true
YARN_CONF_yarn_resourcemanager_store_class=org.apache.hadoop.yarn.server.resourcemanager.recovery.FileSystemRMStateStore
YARN_CONF_yarn_resourcemanager_fs_statestore_uri=/rmstate
YARN_CONF_yarn_nodemanager_remote_app_log_dir=/app-logs
YARN_CONF_yarn_nodemanager_remote_app_log_dir_suffix=logs
YARN_CONF_yarn_log_server_url=http://historyserver:8188/applicationhistory/logs/

MAPRED_CONF_mapred_child_java_opts=-Xmx512m
MAPRED_CONF_mapreduce_map_memory_mb=1024
MAPRED_CONF_mapreduce_reduce_memory_mb=1024
MAPRED_CONF_mapreduce_map_java_opts=-Xmx768m
MAPRED_CONF_mapreduce_reduce_java_opts=-Xmx768m
MAPRED_CONF_mapreduce_framework_name=yarn
MAPRED_CONF_yarn_app_mapreduce_am_env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1/
MAPRED_CONF_mapreduce_application_classpath=/opt/hadoop-3.2.1/etc/hadoop:/opt/hadoop-3.2.1/share/hadoop/common/*:/opt/hadoop-3.2.1/share/hadoop/common/lib/*:/opt/hadoop-3.2.1/share/hadoop/hdfs/*:/opt/hadoop-3.2.1/share/hadoop/hdfs/lib/*:/opt/hadoop-3.2.1/share/hadoop/mapreduce/*:/opt/hadoop-3.2.1/share/hadoop/mapreduce/lib/*:/opt/hadoop-3.2.1/share/hadoop/yarn/*:/opt/hadoop-3.2.1/share/hadoop/yarn/lib/*
EOF
```
</details>


<details>
  <summary> Установка и запуск Python окружения </summary>
  
# Установка и запуск Python окружения

## 1. Проверка текущего состояния

```bash
# Проверяем версию Python
python3 --version

# Проверяем установлен ли pip
pip3 --version

# Проверяем виртуальное окружение
echo $VIRTUAL_ENV
```

## 2. Создание виртуального окружения

```bash
# Создаем виртуальное окружение
python3 -m venv ~/hadoop_venv

# Активируем окружение
source ~/hadoop_venv/bin/activate

# Проверяем активацию (должен показать путь к venv)
echo $VIRTUAL_ENV
```

## 3. Установка необходимых пакетов

```bash
# Обновляем pip
pip install --upgrade pip

# Устанавливаем основные пакеты
pip install mrjob pandas matplotlib seaborn jupyter

# Проверяем установку
pip list
```

## 4. Проверка работы окружения

```bash
# Проверяем импорты
python -c "import mrjob; import pandas; import matplotlib; print('Все пакеты работают!')"

# Проверяем скрипт анализа данных
python scripts/analyze_data.py

# Проверяем MapReduce
python scripts/category_revenue_detailed.py --mapper ./data/input/retail_sales_dataset.csv | head -5
```

## 5. Если возникают ошибки

### Проблема: Нет Python3
```bash
# Устанавливаем Python3
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### Проблема: Нет прав для установки
```bash
# Используем флаг для обхода защиты
pip install mrjob pandas --break-system-packages
```

### Проблема: Не активируется venv
```bash
# Принудительная активация
source ~/hadoop_venv/bin/activate
# Или
. ~/hadoop_venv/bin/activate
```

## 6. Быстрая проверка всего окружения

```bash
#!/bin/bash
echo "=== ПРОВЕРКА PYTHON ОКРУЖЕНИЯ ==="

# Проверка Python
echo "Python version: $(python3 --version 2>/dev/null || echo 'Не установлен')"

# Проверка виртуального окружения
if [ -n "$VIRTUAL_ENV" ]; then
    echo "Venv: АКТИВИРОВАН ($VIRTUAL_ENV)"
else
    echo "Venv: НЕ АКТИВИРОВАН"
fi

# Проверка пакетов
echo "Пакеты:"
python3 -c "try: import mrjob; print(' mrjob'); except: print(' mrjob')"
python3 -c "try: import pandas; print(' pandas'); except: print(' pandas')"
python3 -c "try: import matplotlib; print(' matplotlib'); except: print(' matplotlib')"
```

## 7. Автоматическая активация при входе (опционально)

```bash
# Добавляем в ~/.bashrc
echo "source ~/hadoop_venv/bin/activate" >> ~/.bashrc

# Или создаем алиас
echo "alias hadoopenv='source ~/hadoop_venv/bin/activate'" >> ~/.bashrc
source ~/.bashrc
```

**После выполнения этих команд у вас будет рабочее Python окружение для Hadoop!**

Запускай проверку и сообщи о результате!
</details>

## Копирование данных

```bash
# копируем файл в папку input
cp "/path/to/retail_sales_dataset.csv" ./data/input/

# проверяем, что файл скопировался
ls -la ./data/input/retail_sales_dataset.csv
```

## Просмотр структуры проекта

```bash
# устанавливаем tree если нет
sudo apt install tree -y

# просматриваем структуру проекта
tree -L 3
```

**Ожидаемый вывод:**
```
.
├── config
│   └── hadoop.env
├── data
│   ├── input
│   │   └── retail_sales_dataset.csv
│   └── output
├── docker-compose.yml
├── logs
├── results
└── scripts
    ├── 01_analyze_data.py
    └── 02_category_revenue.py

7 directories, 6 files
```

## Запуск проекта

```bash
# запускаем Hadoop кластер
docker-compose up -d

# проверяем статус
docker-compose ps

# загружаем данные в HDFS
docker exec namenode hdfs dfs -mkdir -p /retail/input
docker exec namenode hdfs dfs -put /data/input/retail_sales_dataset.csv /retail/input/

# проверяем загрузку
docker exec namenode hdfs dfs -ls /retail/input/
```

<details>
  <summary>Архитектура данных</summary>

## Архитектура данных

**Структура файла retail_sales_dataset.csv:**
```
Transaction ID,Date,Customer ID,Gender,Age,Product Category,Quantity,Price per Unit,Total Amount
1,2024-01-15,C101,Male,32,Electronics,2,299.99,599.98
2,2024-01-16,C102,Female,28,Clothing,1,49.99,49.99
3,2024-01-17,C103,Male,45,Beauty,1,25.50,25.50
```

**Колонки:**
- `Transaction ID` - уникальный идентификатор транзакции
- `Date` - дата совершения покупки
- `Customer ID` - идентификатор клиента
- `Gender` - пол покупателя (Male/Female)
- `Age` - возраст покупателя
- `Product Category` - категория товара (Electronics/Clothing/Beauty)
- `Quantity` - количество товаров
- `Price per Unit` - цена за единицу
- `Total Amount` - общая сумма транзакции

</details>

## Проверка распределения данных

```bash
# проверяем как файл разбит на блоки
docker exec namenode hdfs fsck /retail/input/retail_sales_dataset.csv -blocks -locations

# проверяем репликацию (должно быть 3 копии на разных DataNode)
docker exec namenode hdfs dfs -stat "%r" /retail/input/retail_sales_dataset.csv
```

## Веб-интерфейс для просмотра данных

Откройте в браузере: http://localhost:9871

**Путь для просмотра:**
- Перейдите в "Utilities" -> "Browse the file system"
- Перейдите в папку `/retail/input`
- Увидите файл `retail_sales_dataset.csv` с информацией о размере и репликации

Теперь данные готовы для обработки в MapReduce!

### Практика: настройка и базовый анализ

#### Подготовка данных и анализ структуры

**scripts/analyze_data.py**

---
<details>
  <summary>analyze_data.py</summary>

```python
#!/usr/bin/env python3
import pandas as pd
import os

def analyze_dataset():
    # анализируем структуру данных перед MapReduce
    data_path = "./data/input/retail_sales_dataset.csv"
    
    if not os.path.exists(data_path):
        print(f"Файл не найден: {data_path}")
        return
    
    df = pd.read_csv(data_path)
    
    print("СТАТИСТИКА ДАННЫХ")
    print(f"Всего транзакций: {len(df):,}")
    print(f"Уникальных клиентов: {df['Customer ID'].nunique()}")
    print(f"Категорий товаров: {df['Product Category'].nunique()}")
    print(f"Период данных: {df['Date'].min()} до {df['Date'].max()}")
    
    print("\nРАСПРЕДЕЛЕНИЕ ПО КАТЕГОРИЯМ")
    category_stats = df.groupby('Product Category').agg({
        'Total Amount': ['sum', 'count', 'mean'],
        'Quantity': 'sum'
    }).round(2)
    print(category_stats)
    
    print("\nСТАТИСТИКА ПО ПОЛУ")
    gender_stats = df.groupby('Gender').agg({
        'Total Amount': ['sum', 'mean', 'count']
    }).round(2)
    print(gender_stats)

if __name__ == '__main__':
    analyze_dataset()
```

</details>

```bash
# запускаем анализ данных
python3 scripts/analyze_data.py

```

## Создание MApReduce

### Выручка по категориям с детальным выводом

**scripts/category_revenue_detailed.py**

----

<details>
  <summary>category_revenue_detailed.py</summary>

```python
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import RawValueProtocol
import json

class MRCategoryRevenueDetailed(MRJob):
    
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def mapper_extract(self, _, line):
        if line.startswith('Transaction ID'):
            return
            
        fields = line.split(',')
        if len(fields) == 9:
            try:
                category = fields[5].strip()
                total_amount = float(fields[8])
                quantity = int(fields[6])
                
                # Emit как JSON строку
                metrics = {
                    'revenue': total_amount,
                    'transactions': 1,
                    'quantity': quantity
                }
                yield f"CATEGORY_{category}", json.dumps(metrics)
                
            except ValueError:
                self.increment_counter('Data Quality', 'Parse Errors', 1)

    def reducer_combine(self, key, json_strings):
        total_revenue = 0
        total_transactions = 0
        total_quantity = 0
        
        for json_str in json_strings:
            metrics = json.loads(json_str)
            total_revenue += metrics['revenue']
            total_transactions += metrics['transactions']
            total_quantity += metrics['quantity']
        
        category = key.replace('CATEGORY_', '')
        result = {
            'category': category,
            'total_revenue': round(total_revenue, 2),
            'total_transactions': total_transactions,
            'total_quantity': total_quantity,
            'avg_transaction_value': round(total_revenue / total_transactions, 2)
        }
        
        yield None, json.dumps(result)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract,
                   reducer=self.reducer_combine)
        ]

if __name__ == '__main__':
    MRCategoryRevenueDetailed.run()
```

</details>

# Mapper

## Ввод команды:
```bash
python scripts/category_revenue_detailed.py --mapper ./data/input/retail_sales_dataset.csv | head -10
```

## Вывод Mapper:
```
"Clothing"      [100.0, 1, 2]
"Electronics"   [60.0, 1, 2]
"Electronics"   [150.0, 1, 3]
"Beauty"        [1000.0, 1, 2]
"Clothing"      [30.0, 1, 1]
"Clothing"      [50.0, 1, 1]
"Beauty"        [90.0, 1, 3]
"Beauty"        [100.0, 1, 4]
"Electronics"   [150.0, 1, 3]
"Electronics"   [120.0, 1, 4]
```

## Пояснения:

**Формат вывода:** `"Категория" [Сумма, Счетчик, Количество]`

- **Ключ**: Категория товара (`"Clothing"`, `"Electronics"`, `"Beauty"`)
- **Значение**: Кортеж из трех чисел:
  - **Сумма транзакции** (например: 100.0)
  - **Счетчик транзакций** (всегда 1) 
  - **Количество товаров** (например: 2)

**Mapper** преобразует сырые CSV данные в структурированный формат для последующей агрегации в Reducer.

## Reducer
### Запускаем задачу

```bash
python scripts/category_revenue_detailed.py ./data/input/retail_sales_dataset.csv --output-dir /tmp/detailed_results
```

### Смотрим результаты

```bash
# cмотрим что создалось в output директории
ls -la /tmp/detailed_results/

# читаем part-файлы 
cat /tmp/detailed_results/part-*

# Или все файлы в директории
cat /tmp/detailed_results/*
```

### Альтернативные способы просмотра

```bash
# сохраняем результаты в файл для анализа
python scripts/category_revenue_detailed.py ./data/input/retail_sales_dataset.csv > /tmp/results.json

# смотрим результаты
cat /tmp/results.json

# или построчно с нумерацией
cat /tmp/results.json | nl
```

### Если результаты в нескольких part-файлах

```bash
# объединяем все part-файлы
cat /tmp/detailed_results/part-* > /tmp/combined_results.json

# смотрим объединенные результаты
cat /tmp/combined_results.json
```

### Инструмент для визуализации результатов

**scripts/visualize_results.py**

----

<details>
  <summary>visualize_results.py</summary>

```python
#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
import pandas as pd
import re

def parse_hadoop_output(line):
    """Парсит строку вывода Hadoop в структурированные данные"""
    # пример строки: "Clothing"      "Revenue: $155,580.00, Transactions: 351, Quantity: 894, Avg: $443.25"
    # разделяем категорию и остальные данные
    parts = line.split('\t')
    if len(parts) < 2:
        return None
    
    category = parts[0].strip('"')
    data_str = parts[1].strip('"')
    
    # извлекаем числа с помощью регулярных выражений
    revenue_match = re.search(r'Revenue:\s*\$\s*([\d,]+\.\d+)', data_str)
    transactions_match = re.search(r'Transactions:\s*(\d+)', data_str)
    quantity_match = re.search(r'Quantity:\s*(\d+)', data_str)
    avg_match = re.search(r'Avg:\s*\$\s*([\d,]+\.\d+)', data_str)
    
    if not all([revenue_match, transactions_match, quantity_match, avg_match]):
        print(f"Не удалось распарсить строку: {line}")
        return None
    
    # преобразуем в числа
    revenue = float(revenue_match.group(1).replace(',', ''))
    transactions = int(transactions_match.group(1))
    quantity = int(quantity_match.group(1))
    avg = float(avg_match.group(1).replace(',', ''))
    
    return {
        'category': category,
        'total_revenue': revenue,
        'total_transactions': transactions,
        'total_quantity': quantity,
        'avg_transaction_value': avg
    }

def load_and_visualize_results():
    # загружаем результаты MapReduce
    results = []
    
    try:
        with open('/tmp/results.json', 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line:
                    print(f"Обрабатываю строку {line_num}: {line}")
                    parsed_data = parse_hadoop_output(line)
                    if parsed_data:
                        results.append(parsed_data)
    
    except FileNotFoundError:
        print("Файл /tmp/results.json не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    
    if not results:
        print("Нет данных для визуализации")
        return
    
    print(f"Успешно распаршено {len(results)} записей")
    
    # преобразуем в DataFrame
    df = pd.DataFrame(results)
    print("Данные в DataFrame:")
    print(df)
    
    # создаем визуализации
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # График 1: выручка по категориям
    df_sorted = df.sort_values('total_revenue', ascending=True)
    ax1.barh(df_sorted['category'], df_sorted['total_revenue'], color='skyblue')
    ax1.set_title('Общая выручка по категориям')
    ax1.set_xlabel('Выручка ($)')
    
    for i, v in enumerate(df_sorted['total_revenue']):
        ax1.text(v + 1000, i, f'${v:,.0f}', va='center', fontsize=10)
    
    # График 2: количество транзакций
    ax2.pie(df['total_transactions'], labels=df['category'], autopct='%1.1f%%', 
            colors=['lightcoral', 'lightgreen', 'lightsalmon'])
    ax2.set_title('Распределение транзакций по категориям')
    
    # График 3: средний чек
    df_sorted_avg = df.sort_values('avg_transaction_value', ascending=True)
    ax3.barh(df_sorted_avg['category'], df_sorted_avg['avg_transaction_value'], color='lightgreen')
    ax3.set_title('Средний чек по категориям')
    ax3.set_xlabel('Средний чек ($)')
    
    for i, v in enumerate(df_sorted_avg['avg_transaction_value']):
        ax3.text(v + 5, i, f'${v:.2f}', va='center', fontsize=10)
    
    # График 4: количество проданных товаров
    ax4.bar(df['category'], df['total_quantity'], color='lightsalmon')
    ax4.set_title('Количество проданных товаров по категориям')
    ax4.set_ylabel('Количество товаров')

    for i, v in enumerate(df['total_quantity']):
        ax4.text(i, v + 10, f'{v}', ha='center', va='bottom', fontsize=10)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('category_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # выводим таблицу с результатами
    print("\n" + "="*80)
    print("ИТОГОВЫЙ АНАЛИЗ КАТЕГОРИЙ")
    print("="*80)
    print(f"{'Категория':<12} {'Выручка':<15} {'Транзакции':<12} {'Ср.чек':<12} {'Товары':<10}")
    print("-"*80)
    
    for _, row in df.iterrows():
        print(f"{row['category']:<12} ${row['total_revenue']:<14,.2f} {row['total_transactions']:<12} ${row['avg_transaction_value']:<11.2f} {row['total_quantity']:<10}")

if __name__ == '__main__':
    load_and_visualize_results()
```
</details>

# Показ результатов работы скрипта визуализации
## Запускаем скрипт визуализации

```bash
python scripts/visualize_results.py
```

## 4. Что вы увидите:

### А) 4 графика:
1. **Столбчатая диаграмма** - выручка по категориям
2. **Круговая диаграмма** - распределение транзакций  
3. **Горизонтальные столбцы** - средний чек по категориям
4. **Вертикальные столбцы** - количество проданных товаров

### Б) Текстовая таблица в консоли:
```
ИТОГОВЫЙ АНАЛИЗ КАТЕГОРИЙ
================================================================================
Категория       Выручка       Транзакции   Ср.чек     Товары    
--------------------------------------------------------------------------------
Electronics     $156,905.0    520          $301.74    1040      
Clothing        $155,580.0    622          $250.13    933       
Beauty          $143,515.0    718          $199.88    1436      
```

