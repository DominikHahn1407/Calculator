from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, padx=10, pady=10, columnspan=5)


def btn_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def btn_clear():
    e.delete(0, END)


def btn_equal():
    value = e.get()
    e.delete(0, END)
    if '+' in str(value):
        value = value.split('+')
        result = int(value[0]) + int(value[1])
        e.insert(0, result)
    elif '-' in str(value):
        value = value.split('-')
        result = int(value[0]) - int(value[1])
        e.insert(0, result)
    elif '*' in str(value):
        value = value.split('*')
        result = int(value[0]) * int(value[1])
        e.insert(0, result)
    elif '/' in str(value):
        value = value.split('/')
        if int(value[1]) == 0:
            e.insert(0, 'You can`t divide by 0 please try again')
        else:
            result = round(int(value[0]) / int(value[1]), 2)
            e.insert(0, result)
    elif '²' in str(value):
        value = value.split('²')
        result = int(value[0]) * int(value[0])
        e.insert(0, result)


btn1 = Button(root, text='1', width=7, command=lambda: btn_click(1)).grid(row=3, column=0, ipadx=2, ipady=4)
btn2 = Button(root, text='2', width=7, command=lambda: btn_click(2)).grid(row=3, column=1, ipadx=2, ipady=4)
btn3 = Button(root, text='3', width=7, command=lambda: btn_click(3)).grid(row=3, column=2, ipadx=2, ipady=4)
btn4 = Button(root, text='4', width=7, command=lambda: btn_click(4)).grid(row=2, column=0, ipadx=2, ipady=4)
btn5 = Button(root, text='5', width=7, command=lambda: btn_click(5)).grid(row=2, column=1, ipadx=2, ipady=4)
btn6 = Button(root, text='6', width=7, command=lambda: btn_click(6)).grid(row=2, column=2, ipadx=2, ipady=4)
btn7 = Button(root, text='7', width=7, command=lambda: btn_click(7)).grid(row=1, column=0, ipadx=2, ipady=4)
btn8 = Button(root, text='8', width=7, command=lambda: btn_click(8)).grid(row=1, column=1, ipadx=2, ipady=4)
btn9 = Button(root, text='9', width=7, command=lambda: btn_click(9)).grid(row=1, column=2, ipadx=2, ipady=4)
btn0 = Button(root, text='0', width=7, command=lambda: btn_click(0)).grid(row=4, column=1, ipadx=2, ipady=4)

btn_clear = Button(root, text='Clear', width=5, command=btn_clear).grid(row=5, columnspan=6, ipadx=110, ipady=4)
btn_eql = Button(root, text='=', width=7, command=btn_equal).grid(row=4, column=2, ipadx=2, ipady=4)

btn_add = Button(root, text='+', width=7, command=lambda: btn_click('+')).grid(row=1, column=3, ipadx=2, ipady=4)
btn_sub = Button(root, text='-', width=7, command=lambda: btn_click('-')).grid(row=2, column=3, ipadx=2, ipady=4)
btn_mul = Button(root, text='*', width=7, command=lambda: btn_click('*')).grid(row=3, column=3, ipadx=2, ipady=4)
btn_div = Button(root, text='/', width=7, command=lambda: btn_click('/')).grid(row=4, column=3, ipadx=2, ipady=4)

btn_sqr = Button(root, text='²', width=7, command=lambda: btn_click('²')).grid(row=4, column=0, ipadx=2, ipady=4)

root.mainloop()