'''
Допустим, вы работаете в отделе разработки в МФЦ. Центр предоставляет некоторый спектр услуг многодетным семьям.
Необходимо создать функциональность, которая позволяет отфильтровать среди всех запрашиваемых пользователем услуг
 (их количество произвольное) только те, которые предоставляются многодетным семьям.
При решении задачи вам понадобится список услуг, предоставляемых многодетным семьям:
family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
 ]
Реализуйте функцию filter_family(): на вход подаётся список с названием услуг МФЦ, а в результате возвращается список услуг,
которые могут быть оказаны только многодетной семье.
Для фильтрации входного списка аргументов используйте функцию filter().
Примеры работы функции:
print(filter_family(['newborn registration', 'parking permit',
                     'maternity capital', 'tax benefit', 'medical policy']))
## ['parking permit', 'maternity capital', 'tax benefit']
print(filter_family(['reimbursement of expenses', 'parking permit', 'maternity capital', 'medical policy']))
## ['reimbursement of expenses', 'parkin
'''

family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
 ]

def filter_family(lst):
    new_lst = []
    for el in lst:
        if el in family_list:
            new_lst.append(el)
    return new_lst

## filtered_prices = [25683, 17683, 28973]
