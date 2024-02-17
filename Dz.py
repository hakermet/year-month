import tkinter as tk


def on_click():
    global clicked, click_count
    clicked = not clicked

    if clicked:
        label.config(text="Кнопка натиснута")
    else:
        label.config(text="Кнопка відпущена")

    root.title("Кількість натискань: " + str(click_count))


def on_click_count():
    global click_count
    click_count += 1
    root.title("Кількість натискань: " + str(click_count))


root = tk.Tk()
root.title("Кількість натискань: 0")
root.geometry("300x100")

clicked = False
click_count = 0

label = tk.Label(root, text="Кнопка відпущена", font=("None", 14))
label.pack(pady=20)

btn = tk.Button(root, text="Натисни мене",bg='red',activebackground='lime', command=lambda: [on_click(), on_click_count()])
btn.pack()

root.mainloop()
