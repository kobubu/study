'''
Skillfactory | Задача по Python

Инструкция по использованию платформы

У вас есть список prices стоимости аренды помещения под магазин за месяц. Вам необходимо создать список filtered_prices из стоимости, которая не выше 30000, чтобы уложиться в бюджет. В решении примените filter() и lambda.

Примеры работы программы:


prices = [34562, 66572, 25683, 17683, 56389, 28973]
## filtered_prices = [25683, 17683, 28973]

prices = [21490, 24901, 24901, 34901, 24142, 64521]
## filtered_prices = [21490, 24901, 24901, 24142]
Примечание: Обратите внимание, что для отправки кода на проверку переменную prices объявлять не нужно. Не забудьте удалить строку кода с их объявлением перед тем, как отправить код на тестирование.
'''


prices = [34562, 66572, 25683, 17683, 56389, 28973]
filtered_prices = list(filter(lambda x: x < 30000, prices))
## filtered_prices = [25683, 17683, 28973]
