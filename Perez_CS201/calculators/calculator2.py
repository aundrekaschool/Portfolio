from tkinter import *
win = Tk()
win.title("Calculator")
win.geometry("340x440+{}+{}".format((win.winfo_screenwidth()-340)//2, (win.winfo_screenheight()-440)//2))
label = Label(win, width=20, font=('Century Gothic', 18), anchor="e", bd=10, bg="#EEABCC", fg="#333", relief="sunken", text="0")
win.config(bg="#FFABCC")
label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def calc(value):
    if value == 'C': label.config(text="0")
    elif value == '=':
        expression = label.cget("text").replace('x^a', '**').replace('|÷|', '//').replace('×', '*').replace('÷', '/')
        result = eval(expression)
        label.config(text=str(round(result, 8)))
    elif value == 'x^a': label.config(text=label.cget("text") + '**')
    else:
        current_text = label.cget("text")
        if current_text == '0' or current_text == '0.0': label.config(text=value)
        else: label.config(text=current_text + value)
buttons = [('x^a', '|÷|', '%', 'C'),('7', '8', '9', '+'),('4', '5', '6', '-'),('1', '2', '3', '÷'),('.', '0', '=', '×')]
for r, row in enumerate(buttons, 1):
    for c, text in enumerate(row):
        Button(win, text=text, width=5, height=2, font=('Century Gothic', 15), bg="#FFAACC", fg="#000",activebackground="#FF66B2", command=lambda v=text: calc(v)).grid(row=r, column=c, padx=5, pady=5)
win.mainloop()