def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print('-----------------------------')

print_params(b=25)
print_params(c=[1, 2, 3])

print_params()                                  # Вывод функции без аргументов
print('--------------------------------')

values_list = [9.8, 'cucumber', True]
values_dict = {'a': 'ananas', 'b': False, 'c': 0}

print_params(*values_list)
print_params(**values_dict)
print('--------------------------------')

def append_to_list(item, values_list=None):
    if values_list is None:
        values_list = []
        values_list.append(item)

print_params(*values_list)
print('--------------------------------')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)