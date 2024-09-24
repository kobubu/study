'''
Представьте, что мы пытаемся выгрузить несколько новостей с сайта kommersant.ru. У вас есть список путей до интересующих вас статей.

Пример такого списка:

docs = [
'//doc/5041434?query=data%20science',
'//doc/5041567?query=data%20science',
'//doc/4283670?query=data%20science',
'//doc/3712659?query=data%20science',
'//doc/4997267?query=data%20science',
'//doc/4372673?query=data%20science',
'//doc/3779060?query=data%20science',
'//doc/3495410?query=data%20science',
'//doc/4308832?query=data%20science',
'//doc/4079881?query=data%20science'
]
Как вы видите, представленные ссылки на статьи — неполные: в них не хватает адреса самого сайта — "https://www.kommersant.ru".
Ваша задача составить новый список links, в котором будут храниться полные ссылки до статей на сайте «Коммерсанта».
Например, полная ссылка на первую статью будет иметь вид: "https://www.kommersant.ru//doc/5041434?query=data%20science".

Для решения задачи используйте функцию map().
К каждому элементу списка docs (размер списка может быть любым) примените функцию-преобразование, которая добавляет к ссылке на начальную страницу сайта путь до статьи из списка docs.

Результат работы функции map() оберните в список и занесите в переменную links.
Примеры работы программы:

docs = ['//doc/5041434?query=data%20science','//doc/5041567?query=data%20science', '//doc/4283670?query=data%20science','//doc/3712659?query=data%20science', '//doc/4997267?query=data%20science'
]
## links = ['https://www.kommersant.ru//doc/5041434?query=data%20science', 'https://www.kommersant.ru//doc/5041567?query=data%20science', 'https://www.kommersant.ru//doc/4283670?query=data%20science', 'https://www.kommersant.ru//doc/3712659?query=data%20science', 'https://www.kommersant.ru//doc/4997267?query=data%20science']

docs = ['//doc/5041434?query=data%20science','//doc/5041567?query=data%20science','//doc/4283670?query=data%20science','//doc/3712659?query=data%20science','//doc/4997267?query=data%20science','//doc/4372673?query=data%20science','//doc/3779060?query=data%20science','//doc/3495410?query=data%20science','//doc/4308832?query=data%20science','//doc/4079881?query=data%20science'
]
## links = ['https://www.kommersant.ru/
'''

docs = [
'//doc/5041434?query=data%20science',
'//doc/5041567?query=data%20science',
'//doc/4283670?query=data%20science',
'//doc/3712659?query=data%20science',
'//doc/4997267?query=data%20science',
'//doc/4372673?query=data%20science',
'//doc/3779060?query=data%20science',
'//doc/3495410?query=data%20science',
'//doc/4308832?query=data%20science',
'//doc/4079881?query=data%20science'
]

prefix = "https://www.kommersant.ru"
convert = lambda x:  prefix + x

links = list(map(convert, docs))
print(links)
