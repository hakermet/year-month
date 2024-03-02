from tkinter import *
import math


root = Tk()
root.title("Калькулятор")
root.geometry("350x300")
root['bg'] = 'black'
root.minsize(350, 300)
root.maxsize(350,300)




input= Entry(root, width=25, font=("Arial", 16))
input.grid(row=0, columnspan=4, pady=10)

def button_click(char):
    input.insert(END, char)

def calculate():
    try:
        expression = input.get()
        result = eval(expression)
        input.delete(0, END)
        input.insert(0, result)
    except ZeroDivisionError:
        input.delete(0, END)
        input.insert(0, "Ділення на ноль!")
    except:
        input.delete(0, END)
        input.insert(0, "Ти нічого не ввів!")
def button_click(char):
    if char == "sin":
        try:
            expression = input.get()
            result = math.sin(float(expression))
            input.delete(0, END)
            input.insert(0, result)
        except:
            input.delete(0, END)
            input.insert(0, "Неправильно ввів!")
    elif char == ".":
        input.insert(END, char)
    else:
        input.insert(END, char)

# Create all buttons with appropriate grid placements
button_1 = Button(root, text="1", width=6, height=2,activebackground='lime', command=lambda: button_click("1")).grid(row=1, column=0, sticky="nsew")
button_2 = Button(root, text="2", width=6, height=2,activebackground='red', command=lambda: button_click("2")).grid(row=1, column=1, sticky="nsew")
button_3 = Button(root, text="3", width=6, height=2,activebackground='lime', command=lambda: button_click("3")).grid(row=1, column=2, sticky="nsew")
button_4 = Button(root, text="4", width=6, height=2,activebackground='red', command=lambda: button_click("4")).grid(row=2, column=0, sticky="nsew")
button_5 = Button(root, text="5", width=6, height=2,activebackground='lime', command=lambda: button_click("5")).grid(row=2, column=1, sticky="nsew")
button_6 = Button(root, text="6", width=6, height=2,activebackground='red', command=lambda: button_click("6")).grid(row=2, column=2,sticky="nsew")
button_7 = Button(root, text="7", width=6, height=2,activebackground='lime', command=lambda: button_click("7")).grid(row=3, column=0,sticky="nsew")
button_8 = Button(root, text="8", width=6, height=2,activebackground='red', command=lambda: button_click("8")).grid(row=3, column=1,sticky="nsew")
button_9 = Button(root, text="9", width=6, height=2,activebackground='lime', command=lambda: button_click("9")).grid(row=3, column=2,sticky="nsew")
button_0 = Button(root, text="0", width=6, height=2,activebackground='red', command=lambda: button_click("0")).grid(row=4, column=0,sticky="nsew")

button_plus = Button(root, text="+", width=6, height=2,activebackground='lime', command=lambda: button_click("+")).grid(row=1, column=3,sticky="nsew")
button_minus = Button(root, text="-", width=6, height=2,activebackground='red', command=lambda: button_click("-")).grid(row=2, column=3,sticky="nsew")
button_multiply = Button(root, text="*", width=6, height=2,activebackground='lime', command=lambda: button_click("*")).grid(row=3, column=3,sticky="nsew")
button_divide = Button(root, text="/", width=6, height=2,activebackground='red', command=lambda: button_click("/")).grid(row=4, column=3,sticky="nsew")

button_clear = Button(root, text="C", width=6, height=2,bg='DodgerBlue',activebackground='lime', command=lambda: input.delete(0, END)).grid(row=4, column=2,sticky="nsew")
button_equal = Button(root, text="=", width=6, height=2,activebackground='red', command=calculate).grid(row=5, columnspan=3,sticky="nsew")
button_sin = Button(root, text="sin", width=6, height=2,activebackground='lime', command=lambda: button_click("sin")).grid(row=4, column=3, sticky="nsew")
button_dot = Button(root, text=".", width=6, height=2,activebackground='red', command=lambda: button_click(".")).grid(row=4, column=1, sticky="nsew")
button_exit = Button(root, text="Вихід", width=6, height=2,activebackground='lime', command=root.quit).grid(row=5, column=3, sticky="nsew")



mainloop()
