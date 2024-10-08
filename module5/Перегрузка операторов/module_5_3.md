## Цель: применить знания о перегурзке арифметических операторов и операторов сравнения.

### Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс **House** следующими специальными методами:
1. **\_\_eq__(self, other)** - должен возвращать **True**, если количество этажей одинаковое у **self** и у **other**.
2. Методы **\_\_lt__(<)**, **\_\_le__(<=)**, **\_\_gt__(>)**, **\_\_ge__(>=)**, **\_\_ne__(!=)** должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе **\_\_eq__** в сравнении участвует кол-во этажей.
3. **\_\_add__(self, value)** - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
4. **\_\_radd__(self, value)**, **\_\_iadd__(self, value)** - работают так же как и **\_\_add__** (возвращают результат его вызова).
   
Остальные методы арифметических операторов, где **self - x**, **other - y**:

Следует заметить, что **other** может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов **\_\_eq__, \_\_add__**  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции **isinstance**:
- **isinstance(other, int)** - **other** указывает на объект типа **int**.
- **isinstance(other, House)** - **other** указывает на объект типа **House**.

Пример результата выполнения программы:

Пример выполняемого кода:
```python
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
```
Вывод на консоль:
```
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
```
### Примечания:
- Методы **\_\_iadd__** и **\_\_radd__** не обязательно описывать заново, достаточно вернуть значение вызова **\_\_add__**.
- Более подробно о работе всех перечисленных методов можно прочитать [здесь](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) и [здесь](https://docs.python.org/3/reference/datamodel.html#object.__eq__).