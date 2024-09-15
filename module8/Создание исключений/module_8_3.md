## Задача "Некорректность":

### Создайте 3 класса (2 из которых будут исключениями):
#### Класс Car должен обладать следующими свойствами:
1. Атрибут объекта model - название автомобиля (строка).
2. Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
3. Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
4. Атрибут __numbers - номера автомобиля (строка).
5. Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
6. Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

#### Работа методов __is_valid_vin и __is_valid_numbers:
#### __is_valid_vin
1. Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
2. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
3. Возвращает True, если исключения не были выброшены.
#### __is_valid_numbers
1. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
2. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
3. Возвращает True, если исключения не были выброшены.

### ВАЖНО!
Методы **\_\_is_valid_vin** и **\_\_is_valid_numbers** должны вызываться и при создании объекта (в **\_\_init__** при объявлении атрибутов **\_\_vin** и **\_\_numbers**).

### Пример результата выполнения программы:
Пример выполняемого кода:
```python
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
``` 
Вывод на консоль:
```
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера
```
### Примечания:
Для выбрасывания исключений используйте оператор **raise**