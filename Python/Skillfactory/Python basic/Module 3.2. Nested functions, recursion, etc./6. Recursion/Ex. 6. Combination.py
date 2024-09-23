'''
Напишем функцию combination(n, k), которая позволит нам автоматически вычислять значение сочетания по формуле, приведённой выше, для любых n и k.
При расчёте воспользуйтесь рекурсивной функцией factorial(), которую мы написали выше.
Можете сделать её внутренней для функции combination() или независимой функцией, на ваш вкус.
Главное, добавьте в свой код объявление функции factorial().
Пример работы функции:
print(combination(n=10, k=5))
## 252.0
print(combination(n=12, k=3))
## 220.0
print(combination(n=1, k=1))
## 1.0
print(combination(n=0, k=0))
## 1.0
'''
def combination(n, k):
    def factorial(n):
        # Задаём условия выхода из рекурсии:
        if n == 0: return 1
        if n == 1: return 1
        # Во всех других случаях возвращаем
        # произведение текущего числа n и функции от n-1
        return factorial(n - 1) * n
    return factorial(n)/(factorial(n-k)*factorial(k))


print(combination(n=10, k=5))
## 252.0
print(combination(n=12, k=3))
## 220.0
print(combination(n=1, k=1))
## 1.0
print(combination(n=0, k=0))
## 1.0



