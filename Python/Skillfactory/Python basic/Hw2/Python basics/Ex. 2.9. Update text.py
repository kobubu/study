'''
Предположим, мы обучили нейронную сеть генерировать текст (предложения), однако на этапе тестирования выяснилось,
 что мы допустили ошибку при обучении и слова генерируются в неправильной последовательности — справа налево, а не слева направо.
Ошибку мы нашли, однако оказалось, что переобучать модель очень долго и дорого.
Поэтому мы решили вручную разворачивать сгенерированный текст на этапе постобработки. Он хранится в переменной generated_text в виде строки.
Создайте новую строку updated_text, в которой слова будут храниться в обратном порядке.
Для простоты гарантируется, что в предложениях, сгенерированных моделью, нет знаков препинания и весь текст представлен в нижнем регистре.
Примеры работы программы:

generated_text = "глаза нее на поднял он и она попросила что-нибудь скажи"
## updated_text = "скажи что-нибудь попросила она и он поднял на нее глаза"

generated_text = "задачи своей решения способ или информацию ищет он поисковик в запрос вводит человек когда"
## updated_text = когда человек вводит запрос в поисковик он ищет информацию или способ решения своей задачи
Примечание. Обратите внимание, что для отправки кода на проверку переменную generated_text объявлять не нужно. Не забудьте удалить строку с её объявлением перед отправкой кода на тестирование.
'''
generated_text = "глаза нее на поднял он и она попросила что-нибудь скажи"
words = generated_text.split(' ')
words.reverse()
updated_text = ' '.join(words)
print(updated_text)