import tkinter as tk
from tkinter import *
win = Tk()
win.title("Calculator")
win.geometry("1000x440+{}+{}".format((win.winfo_screenwidth()-1000)//2, (win.winfo_screenheight()-440)//2))
win.configure(bg="pink")
def calcu(op):
    num1 = float(inp1.get())
    num2 = float(inp2.get())
    if op == '+':
        result.set(num1 + num2)
    elif op == '-':
        result.set(num1 - num2)
    elif op == '*':
        result.set(num1 * num2)
    elif op == '/':
        result.set(num1 / num2 if num2 != 0 else "Error")
    elif op == '//':
        result.set(num1 // num2 if num2 != 0 else "Error")
    elif op == '^':
        result.set(num1 ** num2)
    elif op == '%':
        result.set(num1 % num2 if num2 != 0 else "Error")
inp1 = Entry(win, width=60)
inp1.place(x=150,y=50)
inp2 = Entry(win, width=60)
inp2.place(x=150,y=100)
result = StringVar()
result_label = Label(win, textvariable=result, width=50, relief="solid")
result_label.place(x=150,y=150)
Label(win, text="First Number:", font=("Century Gothic", 12), bg="pink").place(x=10,y=50)
Label(win, text="Second Number:", font=("Century Gothic", 12), bg="pink").place(x=10,y=100)
Label(win, text="Result:", font=("Century Gothic", 12), bg="pink").place(x=10,y=150)
operations = ['+', '-', '*', '/', '//', '^', '%']
for i, op in enumerate(operations):
    Button(win, width=12, text=op, command=lambda o=op: calcu(o), bg="pink", font=("Century Gothic", 12)).grid(row=0, column=i, padx=5, pady=5)
win.mainloop()