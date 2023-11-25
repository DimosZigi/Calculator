import tkinter as tk


def add():
    global first_num
    first_num = entry.get()
    entry.delete(0, tk.END)
    global operation
    operation = "plus"


def subtract():
    global first_num
    first_num = entry.get()
    entry.delete(0, tk.END)
    global operation
    operation = "minus"


def multiply():
    global first_num
    first_num = entry.get()
    entry.delete(0, tk.END)
    global operation
    operation = "mult"


def divide():
    global first_num
    first_num = entry.get()
    entry.delete(0, tk.END)
    global operation
    operation = "div"


def equal():
    result = 0
    second_num = entry.get()
    if second_num == '':
        second_num = first_num
    second_num = int(second_num)
    entry.delete(0, tk.END)

    if operation == "plus":
        result = int(first_num) + second_num

    if operation == "minus":
        result = int(first_num) - second_num

    if operation == "mult":
        result = int(first_num) * second_num

    if operation == "div":
        result = int(first_num) / second_num

    entry.insert(0, str(result))


def number(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(num))


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Calculator")
root.iconbitmap("calculator-icon.png")

entry = tk.Entry(root, width=50, borderwidth=5)

button_1 = tk.Button(root, width=10, height=2, text='7', command=lambda: number(7))
button_2 = tk.Button(root, width=10, height=2, text='8', command=lambda: number(8))
button_3 = tk.Button(root, width=10, height=2, text='9', command=lambda: number(9))
button_4 = tk.Button(root, width=10, height=2, text='4', command=lambda: number(4))
button_5 = tk.Button(root, width=10, height=2, text='5', command=lambda: number(5))
button_6 = tk.Button(root, width=10, height=2, text='6', command=lambda: number(6))
button_7 = tk.Button(root, width=10, height=2, text='1', command=lambda: number(1))
button_8 = tk.Button(root, width=10, height=2, text='2', command=lambda: number(2))
button_9 = tk.Button(root, width=10, height=2, text='3', command=lambda: number(3))
button_0 = tk.Button(root, width=10, height=2, text='0', command=lambda: number(0))

button_plus = tk.Button(root, width=10, height=2, text='+', command=lambda: add())
button_minus = tk.Button(root, width=10, height=2, text='-', command=lambda: subtract())
button_mult = tk.Button(root, width=10, height=2, text='*', command=lambda: multiply())
button_div = tk.Button(root, width=10, height=2, text='/', command=lambda: divide())

button_equal = tk.Button(root, width=10, height=2, text='=', command=lambda: equal())
button_c = tk.Button(root, width=10, height=2, text='c', command=lambda: clear())

entry.grid(row=0, column=0, columnspan=4)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_c.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

root.mainloop()
