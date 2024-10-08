'''
Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок line правильной.
Примечание 1. Какая последовательность скобок правильная?
Правильной скобочной последовательностью назовём такую последовательность скобок, в которой для каждой открывающей скобки есть последующая соответствующая ей закрывающая скобка. Соответственно, остальные скобочные последовательности назовём неправильными. Пустую строку будем считать правильной последовательностью.
Примечание 2.Для решения этой задачи потребуется использовать стек.
Посимвольно переберите строку. Если встретилась открывающаяся скобка, положите её в стек. Если встретилась закрывающаяся скобка, извлеките скобку из стека.
Если стек пустой, то есть извлечь скобку нельзя, последовательность неправильная.
Если строка закончилась и стек стал пустым, последовательность правильная.
Если в стеке остались скобки, последовательность неправильная.
Пример
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False
'''

def brackets(line):
    stack = []
    for c in line:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False
