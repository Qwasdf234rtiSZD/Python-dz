grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
#print(students)
cucumber = list(zip(grades, students))
#print(cucumber)

a = sum([5, 3, 3, 5, 4])
a2 = len([5, 3, 3, 5, 4])
a = a/a2


b = sum([2, 2, 2, 3])
b2 = len([2, 2, 2, 3])
b = b/b2


j = sum([4, 5, 5, 2])
j2 = len([4, 5, 5, 2])
j = j/j2


k = sum([4, 4, 3])
k2 = len([4, 4, 3])
k = k/k2


s = sum([5, 5, 5, 4, 5])
s2 = len([5, 5, 5, 4, 5])
s = s/s2

pelmeni = {'Aaron': (a), 'Bilbo': (b), 'Johnny': (j), 'Khendrik': (k), 'Steve': (s)}
print(pelmeni)
