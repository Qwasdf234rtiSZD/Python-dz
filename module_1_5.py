immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
# Значения элементов кортежа нельзя изменить, потому что кортежи неизменяемы. Это означает, что после создания кортежа его элементы нельзя изменить, добавить или удалить.
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = "cucumber"
print(mutable_list)