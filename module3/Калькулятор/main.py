from tkinter import *
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value + operation)

def calculate():
    try:
        value = eval(calc.get())
        calc.delete(0, END)
        calc.insert(0, value)
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
        calc.insert(0, 0)

def clear():
    calc.delete(0, END)
    calc.insert(0, 0)

root = Tk()
root.title("Калькулятор")
root.geometry("400x350")

calc = Entry(root, width=35, borderwidth=5)
calc.grid(row=0, column=0, columnspan=4)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_digit('1'))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_digit('2'))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_digit('3'))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_digit('4'))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_digit('5'))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_digit('6'))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_digit('7'))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_digit('8'))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_digit('9'))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_digit('0'))

button_add = Button(root, text="+", padx=40, pady=20, command=lambda: add_operation('+'))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: add_operation('-'))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: add_operation('*'))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: add_operation('/'))
button_equal = Button(root, text="=", padx=40, pady=20, command=calculate)
button_clear = Button(root, text="C", padx=39, pady=20, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()