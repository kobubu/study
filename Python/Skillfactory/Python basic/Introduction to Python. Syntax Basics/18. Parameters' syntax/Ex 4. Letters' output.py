'''
Вам дано имя (name). С помощью цикла выведите каждую букву этого имени на экран,
сопроводив порядковым номером с помощью фразы:
"Буква ... в этом имени - ..." (например, "Буква 1 в этом имени - С").
'''
# Введите свое решение ниже

name = 'йцухйзцухйцхуфыжвфжыьясячмь'
[print(f"Буква {idx} в этом имени - {c}") for idx,c in enumerate(name)]