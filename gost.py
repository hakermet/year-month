phone_book = {}

def contact():
    while True:
        dovidnuk = int(input('1. Додати новий запис\n'
                            '2. Пошук за номером\n'
                            '3. Пошук за іменем\n'
                            '4. Вивести існуючі контакти\n'
                            '5. Видалення абонента\n'
                            '6. Оновлення номера телефону\n'
                            '7. Вихід\n>>>>>>'))
        if dovidnuk == 1:
            name = input("Введіть ім'я контакту: ")
            phone_number = input("Введіть номер телефону контакту: ")
            phone_book[name] = phone_number
            print(f"Контакт {name} з номером {phone_number} додано до телефонного довідника.")
        elif dovidnuk == 2:
            phone_number = input("Введіть номер телефону для пошуку: ")
            for name, number in phone_book.items():
                if number == phone_number:
                    print(f"Знайдено контакт за номером {phone_number}: {name}")
                    return
            print(f"Контакт з номером {phone_number} не знайдено у телефонному довіднику.")
        elif dovidnuk == 3:
            name = input("Введіть ім'я для пошуку: ")
            if name in phone_book:
                print(f"Знайдено контакт {name}: {phone_book[name]}")
            else:
                print(f"Контакт з іменем {name} не знайдено у телефонному довіднику.")
        elif dovidnuk == 4:
            print('Збережені контакти:', phone_book)
        elif dovidnuk == 5:
            b = input('Який контакт ви хочете видалити?\n>>>>')
            del phone_book[b]
        elif dovidnuk == 6:
            name_to_update = input("Введіть ім'я контакту, для якого потрібно оновити номер телефону: ")
            if name_to_update in phone_book:
                new_phone_number = input("Введіть новий номер телефону: ")
                phone_book[name_to_update] = new_phone_number
                print(f"Номер телефону для контакту {name_to_update} оновлено: {new_phone_number}")
            else:
                print(f"Контакт з іменем {name_to_update} не знайдено у телефонному довіднику.")
        elif dovidnuk == 7:
            break

contact()
