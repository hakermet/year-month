from tkinter import *
from tkinter import ttk,messagebox,PhotoImage,filedialog

root = Tk()
root.geometry('600x400')
root.title('ТЕСТИ')



def next_question(tab_index):
    notebook.select(tab_index)

notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)

notebook.add(tab1, text="Питання 1")
notebook.add(tab2, text="Питання 2")
notebook.add(tab3, text="Питання 3")
notebook.add(tab4, text="Питання 4")
notebook.add(tab5, text="Питання 5")
notebook.add(tab6, text="Питання 6")
notebook.add(tab7, text="Завершити роботу")

balu = 0

def check_answer1():
    global balu
    correct_answer1 = 1  # 1 for 'Tesla'
    if var.get() == correct_answer1:
        balu+=2
    else:
        balu+=0

def check_answer2():
    global balu
    correct_answer2 = 4  # 4 for 'SpaceX'
    if var1.get() == correct_answer2:
        balu += 2
    else:
        balu += 0



def check_answer3():
    global balu
    correct_countries = {5, 6, 4}  # 5 for 'Україна', 6 for 'Польща', 4 for 'Німеччина'
    selected_countries = set()
    if var1.get() == 1:
        selected_countries.add(1)
    if var2.get() == 1:
        selected_countries.add(2)
    if var3.get() == 1:
        selected_countries.add(3)
    if var4.get() == 1:
        selected_countries.add(4)
    if var5.get() == 1:
        selected_countries.add(5)
    if var6.get() == 1:
        selected_countries.add(6)

    if selected_countries == correct_countries:
        balu += 2
    else:
        balu += 0

def check_answer4():
    global balu
    correct_answer4 = 7
    user_answer = spinbox.get()
    user_answer = int(user_answer)

    if user_answer == correct_answer4:
        balu += 2
    else:
        balu += 0

def check_answer5():
    global balu
    correct_languages = {"Python", "Java", "C++", "JavaScript", "Pascal", "C"}
    selected_languages = set()
    for i in listbox.curselection():
        selected_languages.add(listbox.get(i))

    if selected_languages == correct_languages:
        balu += 2
    else:
        balu += 0

def check_answer6():
    global balu
    correct_answer6 = "Кругліков Олександр"
    user_answer = entry.get()
    user_answer = user_answer.strip()

    if user_answer.lower() == correct_answer6.lower() or user_answer.lower() == correct_answer6.lower().split()[::-1]:
        balu += 2
    else:
        balu += 0

try:
    label1 = ttk.Label(tab1, text="Яка компанія випустила перший електричний автомобіль масового виробництва?     (2 бали)")
    label1.pack(padx=10, pady=10)

    var = IntVar()
    radiobutton1 = Radiobutton( tab1,text='Tesla', variable=var, value=1)
    radiobutton2 = Radiobutton(tab1, text='Toyota', variable=var, value=2)
    radiobutton3 = Radiobutton(tab1, text='Nissan', variable=var, value=3)
    radiobutton4 = Radiobutton(tab1, text='Audi', variable=var, value=4)

    radiobutton1.pack(side='top')
    radiobutton2.pack(side='top')
    radiobutton3.pack(side='top')
    radiobutton4.pack(side='top')

    next_button = Button(tab1,text='Next',command=lambda: next_question(notebook.index(tab2)))
    next_button.pack(side='bottom')
except:
    messagebox.showwarning('Warning', 'Please select an answer to the question')

try:
    label2 = ttk.Label(tab2, text="Яка з цих компаній не займається розробкою штучного інтелекту?      (2 бали)")
    label2.pack(padx=10, pady=10)

    var1 = IntVar()

    radiobutton1 = ttk.Radiobutton(tab2, text='Google', variable=var1, value=1)
    radiobutton2 = ttk.Radiobutton(tab2, text='Microsoft', variable=var1, value=2)
    radiobutton3 = ttk.Radiobutton(tab2, text='IBM', variable=var1, value=3)
    radiobutton4 = ttk.Radiobutton(tab2, text='SpaceX', variable=var1, value=4)

    radiobutton1.pack(side='top')
    radiobutton2.pack(side='top')
    radiobutton3.pack(side='top')
    radiobutton4.pack(side='top')

    next_button = ttk.Button(tab2, text='Next', command=lambda: next_question(notebook.index(tab3)))
    next_button.pack(side='bottom')
except:
    messagebox.showwarning('Warning', 'Please select an answer to the question')

try:
    label2 = ttk.Label(tab3, text="Які з цих країн розташовані в Європі?      (2 бали)")
    label2.pack(padx=10, pady=10)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()

    checkbutton1 = Checkbutton(tab3, text='Австралія', variable=var1)
    checkbutton2 = Checkbutton(tab3, text='Японія', variable=var2)
    checkbutton3 = Checkbutton(tab3, text='Канада', variable=var3)
    checkbutton4 = Checkbutton(tab3, text='Німеччина', variable=var4)
    checkbutton5 = Checkbutton(tab3, text='Україна', variable=var5)
    checkbutton6 = Checkbutton(tab3, text='Польша', variable=var6)

    checkbutton1.pack(side='top')
    checkbutton2.pack(side='top')
    checkbutton3.pack(side='top')
    checkbutton4.pack(side='top')
    checkbutton5.pack(side='top')
    checkbutton6.pack(side='top')
    next_button = ttk.Button(tab3, text='Next', command=lambda: next_question(notebook.index(tab4)))
    next_button.pack(side='bottom')

except:
    messagebox.showwarning('Warning','Ви не вибрали відповідь на питання')

try:
    label2 = ttk.Label(tab4, text="Скільки материків на планеті Земля?      (2 бали)")
    label2.pack(padx=10, pady=10)

    spinbox = Spinbox(tab4, from_=0, to=10, increment=1)
    spinbox.pack()

    next_button = ttk.Button(tab4, text='Next', command=lambda: next_question(notebook.index(tab5)))
    next_button.pack(side='bottom')
    photo = PhotoImage(file="C:\\Users\Lenovo\OneDrive\Рабочий стол\pycharm\earh.png")
    label = Label(tab4, image=photo)
    label.pack()

except:
    messagebox.showwarning('Warning','Ви не вибрали відповідь на питання')

try:
    label2 = ttk.Label(tab5, text="Вибери,які мови програмування існують.      (2 бали)")
    label2.pack(padx=10, pady=10)


    def on_select(event):
        selected_indices = listbox.curselection()
        selected_items = [listbox.get(idx) for idx in selected_indices]


    listbox = Listbox(tab5, selectmode=MULTIPLE)
    listbox.pack(pady=10)
    lst=['Python','Java','Kolos','C++','JavaScript','Pand','kifir','Pascal','C']
    for i in lst:
        listbox.insert(END, f" {i}")
    listbox.bind("<<ListboxSelect>>", on_select)
    next_button = ttk.Button(tab5, text='Next', command=lambda: next_question(notebook.index(tab6)))
    next_button.pack(side='bottom')
except:
    messagebox.showwarning('Warning','Ви не вибрали відповідь на питання')

try:
    label2 = ttk.Label(tab6, text="Яке прізвище та ім'я учня,який зробив цю домашню роботу?      (2 бали)")
    label2.pack(padx=10, pady=10)

    entry = Entry(tab6)
    entry.pack()

    next_button = ttk.Button(tab6, text='Next', command=lambda: next_question(notebook.index(tab7)))
    next_button.pack(side='bottom')

except:
        messagebox.showwarning('Warning', 'Ви не вибрали відповідь на питання')
def tick():
    try:
        global balu
        labl.pack()
        file = filedialog.asksaveasfilename(defaultextension='txt', filetypes=(('Текстові файли', "*.txt"), ('File', '*.html;*.htm'), ('all file', '*.*')))

        with open(file, 'w', encoding='utf-8') as f:
                f.write(str(check_answer1))
                f.write(str(check_answer2))
                f.write(str(check_answer3))
                f.write(str(check_answer4))
                f.write(str(check_answer5))
                f.write(str(check_answer6))
                f.write(str(balu))
    except:
        pass




try:
    button = Button(tab7, text='Завершити роботу',command=tick)
    button.pack(side='top')
    labl=Label(tab7,text='Йде обрахунок балів...')
    labl['state'] = 'disable'

    labl.after_cancel()


except:
        pass
notebook.pack(expand=1, fill="both")

root.mainloop()
