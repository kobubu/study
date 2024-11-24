'''
На вебинар по программированию записались потенциальные слушатели со следующими электронными адресами:

bennet@xyz.com
darcy@abc.com
margaret@xyz.com
pa@hhh.com
marimari@xyz.com
mallika@yahoo.com
abc@xyz.com
0071235@gmail.ru
На вебинар по машинному обучению записались потенциальные слушатели со следующими электронными адресами:

marimari@xyz.com
darcy@abc.com
0071235@gmail.ru
darcy@abc.com
petr44@xyz.com
katrin@ya.com

С помощью операций множеств в Python определите, сколько слушателей записалось на оба вебинара.
'''

# Данные
prog_listeners = {"bennet@xyz.com", "darcy@abc.com", "margaret@xyz.com", "pa@hhh.com", "marimari@xyz.com", "mallika@yahoo.com", "abc@xyz.com", "0071235@gmail.ru"}
machine_listeners = {"marimari@xyz.com", "darcy@abc.com", "0071235@gmail.ru", "darcy@abc.com", "petr44@xyz.com","katrin@ya.com"}

# С помощью операций множеств в Python определите, сколько слушателей записалось на оба вебинара.
both = prog_listeners & machine_listeners

#Сколько человек заинтересованы в посещении хотя бы одного вебинара?
at_least_1 = prog_listeners | machine_listeners

# Сколько человек заинтересованы в посещении только одного вебинара из двух?
only_1 = at_least_1-both

print(len(at_least_1-both))
