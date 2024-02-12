import sys
def main():
    while True:
        print('1)Додати користувача 2)Вивести список користувачів 3)Закінчити програму')
        user_vubir = int(input('Введіть число'))
        if user_vubir == 1:
            name, year, month = get_user_input()
            text_file(name, year, month)
        elif user_vubir == 2:
            read_file()
        elif user_vubir == 3:
            def clear_file():
                with open("test_file.txt", "r+") as file:
                    file.truncate(0)
                    file.seek(0)
            print('Дякую що провели час з нами')
            clear_file()
            sys.exit()

def get_user_input():
    while True:
        name = input("Введіть ім'я: ")
        if validate_name(name):
            break
        else:
            print("Некоректне ім'я. Будь ласка, спробуйте ще раз.")
    while True:
        global year
        year = int(input("Введіть рік народження (від 5 до 120 років): "))
        if validate_year(year):
            break
        else:
            print("Некоректний рік. Будь ласка, спробуйте ще раз.")
    while True:
        global month
        month = int(input("Введіть місяць народження (від 1 до 12): "))
        if validate_month(month):
            break
        else:
            print("Некоректний місяць. Будь ласка, спробуйте ще раз.")
    return name, year, month

def validate_name(name):
    if 0 < len(name) < 16:
        return name
    else:
        print("Погане ім'я")

def validate_year(year):
    try:
        year = int(year)
        if 5 <= year <= 120:
            return year
        else:
            print("Рік повинен бути в межах від 5 до 120. Будь ласка, спробуйте ще раз.")
    except ValueError:
        print("Введено не число. Будь ласка, спробуйте ще раз.")

def validate_month(month):
    try:
        month = int(month)
        if 1 <= month <= 12:
            return  month
        else:
            print('Введено невірне значення')
    except ValueError:
        print("Введено не число")

def text_file(name, year, month):
    # text_file(name, year, month)
    with open("test_file.txt", "a") as file:
        file.write("\n"+name + "\n")
        file.write(str(year) + "\n")
        file.write(str(month) + "\n")
    print("Дані успішно записані у файл 'test_file.txt'.")

def read_file():
    with open("test_file.txt",'w', encoding='utf-8') as file:
        file.write()
        # file.truncate(0)

if __name__ == "__main__":
    main()