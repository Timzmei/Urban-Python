my_dict = {
    "Napoleon": 1769,
    "Alexander the Great": 356,
    "Julius Caesar": 100,
    "Leonardo da Vinci": 1452,
    "Isaac Newton": 1643,
    "Albert Einstein": 1879
}

print(my_dict)

print(f'значение по существующему ключу "Napoleon": {my_dict.get("Napoleon")}')
print(f'значение по отсутствующему ключу "Stalin": {my_dict.get("Stalin")}')


print(my_dict)
my_dict["Galileo Galilei"] = 1564
my_dict["Marie Curie"] = 1867

print(my_dict)

print(f'Удаляем одну из пар в словаре по существующему ключу из словаря my_dict и выводим значение из этой пары на экран: {my_dict.pop("Galileo Galilei")}')
print(my_dict)


my_set = {1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, "hello", "world", "hello", 3.14, 3.14, True, False, True}
print(my_set)

my_set.add("One")
my_set.add("Two")
print(my_set)

my_set.pop()

print(my_set)