from tkinter import *
from tkinter import filedialog

def save_options():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            for key, value in selected_options.items():
                file.write(f"{key}: {value.get()}\n")

def update_results(*args):
    text_results.delete(1.0, END)
    for key, value in selected_options.items():
        text_results.insert(END, f"{key}: {value.get()}\n")

root = Tk()
root.title("Салон нових та б/у автомобілів")
root.geometry('500x500')
root['bg']='wheat'
selected_brand = StringVar()
selected_age = StringVar()
selected_fuel = StringVar()
selected_color = StringVar()
selected_region = StringVar()
selected_model = StringVar()
selected_engine = StringVar()
frame = Frame(root, bg='#f0f0f0')
frame.pack(padx=10, pady=10)

brand_label = Label(frame, text="Марка автомобіля:",background='lime')
brand_label.grid(row=0, column=0, sticky=W)

brand_menu = OptionMenu(frame, selected_brand, "BMW", "Mercedes", "Volkswagen", "Mazda", "Audi", "Toyota")
brand_menu.grid(row=0, column=1, sticky=W)

model_label = Label(frame, text="Модель автомобіля:",background='lime')
model_label.grid(row=1, column=0, sticky=W)

model_menu = OptionMenu(frame, selected_model, "Седан", "Хетчбек", "Універсал", "Кросовер", "Позашляховик")
model_menu.grid(row=1, column=1, sticky=W)

age_label = Label(frame, text="Скільки років:",background='lime')
age_label.grid(row=2, column=0, sticky=W)

age_menu = OptionMenu(frame, selected_age, "До 5 років", "6-10 років", "11-15 років", "Більше 15 років")
age_menu.grid(row=2, column=1, sticky=W)

fuel_label = Label(frame, text="Вид двигуна:",background='lime')
fuel_label.grid(row=3, column=0, sticky=W)

engine_label = Label(frame, text="Об'єм двигуна:",background='lime')
engine_label.grid(row=6, column=0, sticky=W)

engine_menu = OptionMenu(frame, selected_engine, "1.0L", "1.5L", "2.0L", "2.5L", "3.0L")
engine_menu.grid(row=6, column=1, sticky=W)

fuel_menu = OptionMenu(frame, selected_fuel, "Гібрид", "Дизель", "Бензин", "Електрика", "Газ")
fuel_menu.grid(row=3, column=1, sticky=W)

color_label = Label(frame, text="Колір:",background='lime')
color_label.grid(row=5, column=0, sticky=W)

color_menu = OptionMenu(frame, selected_color, "Червоний", "Синій", "Чорний", "Білий", "Зелений")
color_menu.grid(row=5, column=1, sticky=W)

region_label = Label(frame, text="Регіон:",background='lime')
region_label.grid(row=4, column=0, sticky=W)

region_menu = OptionMenu(frame, selected_region, "Європа", "Азія", "Америка", "Австралія")
region_menu.grid(row=4, column=1, sticky=W)

selected_options = {
    "Марка": selected_brand,
    "Модель": selected_model,
    "Рік": selected_age,
    "Паливо": selected_fuel,
    "Колір": selected_color,
    "Регіон": selected_region,
    "Об'єм двигуна": selected_engine,
}

selected_brand.trace("w", update_results)
selected_model.trace("w", update_results)
selected_age.trace("w", update_results)
selected_engine.trace("w", update_results)
selected_fuel.trace("w", update_results)
selected_color.trace("w", update_results)
selected_region.trace("w", update_results)

text_results = Text(root, width=40, height=7)
text_results.pack(padx=20, pady=10)

label_frame = Frame(root)
label_frame.pack(pady=10)

def label_color(event=None):
    color = selected_color.get()
    if color == 'Чорний':
        label.config(bg='black')
    elif color == 'Синій':
        label.config(bg='blue')
    elif color == 'Червоний':
        label.config(bg='red')
    elif color == 'Білий':
        label.config(bg='white')
    elif color == 'Зелений':
        label.config(bg='green')
    else:
        label.config(bg='white')
root.bind('<Motion>', label_color)
label = Label(frame, width=5, height=1, bg='white', highlightthickness=1, highlightbackground='black')
label.grid(row=5, column=2, padx=5, pady=5, sticky=W)

button_frame = Frame(root)
button_frame.pack()

save_button = Button(button_frame, text="Зберегти", command=save_options, width=10, highlightthickness=1, highlightbackground='black',background="wheat", activebackground='Lime')
save_button.pack(side=LEFT, padx=10)

root.mainloop()
