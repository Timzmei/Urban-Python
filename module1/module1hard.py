students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = list(students)

print(type(students))
students.sort()
print(students)

print(list(map(sum, grades)))

dict_grades = dict(zip(students, list(map(lambda x: sum(x) / len(x), grades)))) 

print(dict_grades)