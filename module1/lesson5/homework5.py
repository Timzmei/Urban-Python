immutable_var = (15, 'Hello', 3.7, 56)
print(immutable_var)

# кортеж не поддерживает обращение по элементам.
# Следующий код выдаст ошибку
# immutable_var[0] = 'One' 
# TypeError: 'tuple' object does not support item assignment

mutable_list = [5, 6, 8, 'Hello', 'World', 'One', 76]

print(mutable_list)

mutable_list[1] = 'Two'

print(mutable_list)