import random
import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Вгадай число')

def gen():
    try:
        start_num = int(entery.get())
        end_num = int(entery1.get())
        if start_num >= end_num:
            tkinter.messagebox.showwarning('Помилка', 'Початкове число має бути менше за кінцеве')
        else:
            global gen_number
            gen_number = random.randint(start_num, end_num)
            root.title(gen_number)
            btm['state'] = 'disable'
            entery['state'] = 'disable'
            entery1['state'] = 'disable'
            c.place(x=14, y=250)
            entery2.place(x=159, y=250)
            btm1.place(x=200, y=300)
    except ValueError:
        tkinter.messagebox.showerror('Помилка', 'Потрібно ввести цілі числа')

def guess():
    try:
        guess_num = int(entery2.get())
        if gen_number == guess_num:
            tkinter.messagebox.showinfo('Ти вгадав', f'Загадане число було: {gen_number}')
            reset_game()
        else:
            global attempts
            if attempts < 4:
                attempts += 1
                if guess_num < gen_number:
                    tkinter.messagebox.showwarning('Не вгадав', 'Загадане число більше')
                else:
                    tkinter.messagebox.showwarning('Не вгадав', 'Загадане число менше')
            else:
                tkinter.messagebox.showinfo('Кінець гри', f'Загадане число було: {gen_number}')
                reset_game()
    except ValueError:
        tkinter.messagebox.showerror('Помилка', 'Потрібно ввести ціле число')

def reset_game():
    global attempts
    attempts = 0
    root.title('Вгадай число')
    btm['state'] = 'normal'
    entery['state'] = 'normal'
    entery1['state'] = 'normal'
    c.place_forget()
    entery2.delete(0, 'end')

attempts = 0

a = Label(text='Початкове число:')
a.place(x=14, y=100)
b = Label(text="Кінцеве число:")
b.place(x=14, y=150)
c = Label(text='Введи число:')

btm = Button(text='Генерувати', width=10, height=1, command=gen)
labl = Button(text='Result =')
btm.place(x=200, y=200)
entery2 = Entry(root)

entery1 = Entry(root)
btm1 = Button(text='Вгадати', width=10, height=1, command=guess)

entery1.place(x=150, y=150)
entery = Entry(root)
entery.place(x=150, y=100)

def validate_input(new_value):
    return new_value.isdigit()

vcmd = root.register(validate_input)
entery2.config(validate="key", validatecommand=(vcmd, '%P'))

mainloop()
