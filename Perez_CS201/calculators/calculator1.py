import tkinter as tk
from tkinter import *
win = tk.Tk()
win.title("Calculator")
win.geometry("1010x350+{}+{}".format((win.winfo_screenwidth()-1010)//2, (win.winfo_screenheight()-350)//2))
win.configure(bg="#FFE4E1")
def calcu(op):
    num1 = float(inp1.get())
    num2 = float(inp2.get())
    if op == '+':result.set(f"{num1 + num2:.2f}")
    elif op == '-':result.set(f"{num1 - num2:.2f}")
    elif op == '*':result.set(f"{num1 * num2:.2f}")
    elif op == '/':result.set("Error" if num2 == 0 else f"{num1 / num2:.2f}")
    elif op == '//':result.set("Error" if num2 == 0 else f"{num1 // num2}")
    elif op == '^':result.set(f"{num1 ** num2:.2f}")
    elif op == '%': result.set(f"{num1 % num2:.2f}")
inp1 = tk.Entry(win, width=54, font=("Century Gothic", 16), bd=2, relief="solid")
inp1.place(x=300, y=50)
inp2 = tk.Entry(win, width=54, font=("Century Gothic", 16), bd=2, relief="solid")
inp2.place(x=300, y=100)
result = tk.StringVar()
result_label = tk.Label(win, textvariable=result, width=54, font=("Century Gothic", 16), relief="solid", bg="#FFFFFF")
result_label.place(x=300, y=150)
tk.Label(win, text="First Number:", font=("Century Gothic", 14), bg="#FFE4E1").place(x=50, y=50)
tk.Label(win, text="Second Number:", font=("Century Gothic", 14), bg="#FFE4E1").place(x=50, y=100)
tk.Label(win, text="Result:", font=("Century Gothic", 14), bg="#FFE4E1").place(x=50, y=150)
operations = ['+', '-', '*', '/', '//', '^', '%']
button_frame = tk.Frame(win, bg="#FFE4E1")
button_frame.place(x=50, y=220)
for i, op in enumerate(operations):
    tk.Button(button_frame, text=op, command=lambda o=op: calcu(o), width=10, height=2, font=("Century Gothic", 14), 
              bg="#FFB6C1", fg="#000000", activebackground="#FF69B4").grid(row=0, column=i, padx=5, pady=5)
win.mainloop()