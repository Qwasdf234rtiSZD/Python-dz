#НОМЕР 1
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
my_dict['Vasya'] = 2000
my_dict['Artem'] = 2008
print(my_dict)
my_dict.update({'Sanechka': 1200, 'Sergey': 777})
a = my_dict.pop('Egor')
print(a)
print(my_dict)

#НОМЕР 2
my_set = {1, 1, 'Яблоко', 42.314}
print(my_set)
my_set.add('cucumber')
my_set.add(5)
print(my_set)
my_set.discard(1)
print(my_set)