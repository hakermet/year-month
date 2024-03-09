from tkinter import *
import tkinter.ttk

def konverтуй_валюту():
    сума = float(сума_entry.get())
    валюта_з = валюта_з_var.get()
    валюта_на = валюта_на_var.get()

    курси_валют = {
        "USD": 0.026,
        "EUR": 0.024,
        "GBP": 0.020,
        "JPY": 3.85,
        "CNY": 0.19,
        "UAH": 1
    }

    сума_usd = сума / курси_валют[валюта_з]

    сума_konvertovana = сума_usd * курси_валют[валюта_на]

    result_label.config(text=f"{сума} {валюта_з} дорівнює {сума_konvertovana:.2f} {валюта_на}.")

root = Tk()
root.title("Конвертор валют")


frame = LabelFrame(root, text="Конвертація валют")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

сума_label = Label(frame, text="Сума:")

сума_entry = Entry(frame, width=10)
сума_entry.insert(0, "1.00")

валюта_з_label = Label(frame, text="З:")
валюта_з_var = StringVar(value="USD")

валюта_на_label = Label(frame, text="На:")
валюта_на_var = StringVar(value="EUR")

конвертувати_button = Button(frame, text="Конвертувати", command=konverтуй_валюту)

result_label = Label(frame, text="")

сума_label.grid(row=0, column=0, sticky="w")
сума_entry.grid(row=0, column=1, padx=(5, 0))
валюта_з_label.grid(row=1, column=0, sticky="w")
Radiobutton(frame, text="USD", variable=валюта_з_var, value="USD").grid(row=1, column=1, padx=(5, 0))
Radiobutton(frame, text="EUR", variable=валюта_з_var, value="EUR").grid(row=1, column=2, padx=(5, 0))
Radiobutton(frame, text="GBP", variable=валюта_з_var, value="GBP").grid(row=1, column=3, padx=(5, 0))
Radiobutton(frame, text="JPY", variable=валюта_з_var, value="JPY").grid(row=1, column=4, padx=(5, 0))
Radiobutton(frame, text="CNY", variable=валюта_з_var, value="CNY").grid(row=1, column=5, padx=(5, 0))
Radiobutton(frame, text="UAH", variable=валюта_з_var, value="UAH").grid(row=1, column=6, padx=(5, 0))
валюта_на_label.grid(row=2, column=0, sticky="w")
Radiobutton(frame, text="USD", variable=валюта_на_var, value="USD").grid(row=2, column=1, padx=(5, 0))
Radiobutton(frame, text="EUR", variable=валюта_на_var, value="EUR").grid(row=2, column=2, padx=(5, 0))
Radiobutton(frame, text="GBP", variable=валюта_на_var, value="GBP").grid(row=2, column=3, padx=(5, 0))
Radiobutton(frame, text="JPY", variable=валюта_на_var, value="JPY").grid(row=2, column=4, padx=(5, 0))
Radiobutton(frame, text="CNY", variable=валюта_на_var, value="CNY").grid(row=2, column=5, padx=(5, 0))
Radiobutton(frame, text="UAH", variable=валюта_на_var, value="UAH").grid(row=2, column=6, padx=(5, 0))

конвертувати_button.grid(row=3, columnspan=7, pady=(10, 0))

result_label.grid(row=4, columnspan=7, pady=(10, 0))
root.configure(bg="#f0f0f0")
frame.configure(bg="#f0f0f0")
сума_label.configure(bg="#f0f0f0")
сума_entry.configure(bg="white")
валюта_з_label.configure(bg="#f0f0f0")
валюта_на_label.configure(bg="#f0f0f0")
конвертувати_button.configure(bg="#4CAF50", fg="white")
result_label.configure(bg="#f0f0f0")
root.mainloop()

