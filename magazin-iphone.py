import time
from colorama import Fore, Back,Style
basket = []
sell = []
dod_list = []
#Характеристики
def display_info(model_tel, screen, memory, processor, camera, video, battery, weight, price):
    print(f'Модель: {model_tel}')
    print(f'Екран: {screen}')
    print(f"Пам'ять: {memory}")
    print(f'Процесор: {processor}')
    print(f'Камера: {camera}')
    print(f'Відео: {video}')
    print(f'Ємність батареї: {battery}')
    print(f'Вага: {weight}')
    print(f'Ціна: {price} грн')
    sell.append(price)

#Задавати питання
def ask_question(question):
    if question == 1:
        print(Fore.LIGHTGREEN_EX, 'iPhone 14 Pro Max - найкращий флагман Apple...',Fore.RESET)
    elif question == 2:
        print(Fore.LIGHTGREEN_EX, "iPhone 13. Головною новиною, а точніше її відсутністю, є те, що Apple використовує в основному той самий чип A15 Bionic...",Fore.RESET)
    elif question == 3:
        print(Fore.LIGHTGREEN_EX, "Найпопулярнішим смартфоном Apple в світі лишається модель, яку було презентовано у 2019 році...",Fore.RESET)
    elif question == 4:
        print(Fore.LIGHTGREEN_EX, "І iPhone 14, і iPhone 15 оснащені потужними процесорами, але iPhone 15 лідирує завдяки чіпу A16 Bionic...",Fore.RESET)
    elif question == 5:
        print(Fore.LIGHTGREEN_EX, "Знімки з високим контрастом або грою світла й тіні виходять трохи кращими на 14 завдяки кращій передачі контрастних зон та їх границь...",Fore.RESET)
#Додавання до кошика

def bask(thing):
    a=input('Бажаєте додати товар до кошика так\ні\n>>>>>')
    if a == 'так':

        basket.append(thing)
        print(Fore.LIGHTGREEN_EX,'Товар успішно додано до кошика',Fore.RESET)
    elif a == 'ні':
        print('Вибирайте далі')
#Додавання нового товару
def tovar_dod():
            dod = input('Який товар ви хочете додати?\n>>>>>')
            if dod == 'Iphone':
                dod_iphone = input('Яку модель ви хотіли б добавити?\n>>>>>')
                dod_list.append(dod_iphone)
                print('Модель добавлено до списку', dod_list)
            elif dod == 'Mac':
                dod_mac = input('Яку модель ви хотіли б добавити?\n>>>>>')
                dod_list.append(dod_mac)
                print('Модель добавлено до списку', dod_list)
            elif dod == 'Airpods':
                dod_Airpods = input('Яку модель ви хотіли б добавити?\n>>>>>')
                dod_list.append(dod_Airpods)
                print('Модель добавлено до списку', dod_list)
            elif dod == 'Ipad':
                dod_Ipad = input('Яку модель ви хотіли б добавити?\n>>>>>')
                dod_list.append(dod_Ipad)
                print('Модель добавлено до списку', dod_list)
            elif dod == 'Watch':
                dod_Watch = input('Яку модель ви хотіли б добавити?\n>>>>>')
                dod_list.append(dod_Watch)
                print('Модель добавлено до списку', dod_list)
#Оплата товару
def checkout():
    print(basket)
    print('До сплати:', sum(sell), 'грн')
    basket_2 = input('Бажаєте оплатити товар? Так/Ні----->')
    if basket_2 == 'так':
        def error():
            basket_3 = input('Введіть данні карти: ')
            basket_4 = input('Введіть пін код: ')
            if len(basket_3) == 16 and len(basket_4) == 4:
                print('Транзакція обробляється...')
                time.sleep(5)
                print(Fore.LIGHTGREEN_EX,'Транзакція пройшла успішно',Fore.RESET)
                print('Товар поверенню не підлягає')
                basket.clear()
                sell.clear()
                with open('Magazin.txt', 'w', encoding='utf-8') as c:

                    m=input('Хочете залишити відгук?\n>>>>>>')
                    if m=='так':
                        mv=int(input('Поставте оцінку\n>>>>>>>'))
                        if mv<=5:
                            vid=input('Що вам не сподобалося?\n>>>>>>>')
                            time.sleep(2)
                            print("Ми обов'язково виправимо всі проблеми")
                            c.write(vid)
                        elif mv>=6:
                            vid1=input('Що вам сподобалось?\n>>>>>>')
                            print('Дякуємо за відгук')
                            c.write(vid1)
                            vid2=input('хочете продовжити покупки?\n>>>>>>>')
                            if vid2 == 'ні':
                                exit()
                    elif m == 'ні':
                        print('Добре')
                        print('Дякуємо за покупку!')
            else:
                        print('Неправильні дані карти або пін код. Оплата не пройшла.')
                        return error()
        error()

while True:

#Головна
    print('..............','Вас вітає Apple Store Ukraine!','..............')
    print('Що ви б хотіли купити в нашому магазині?')
    model=input('В магазині є такі категорії:Iphone, Airpods, Ipad, Macbook, Apple Watch\n'
                'Хочете задати запитання----->?'
                '\nХочете додати новий товар--new'
                '\nКонсультант---consult'
                '\nЩоб перейти в кошик---->basket'
                '\nВидалення з кошика---nobasket'
                '\nЩоб вийти натисніть---break'
                '\n>>>>>>>')
    #Питання
    if model == '?':
        question = int(input('1) Який краще купити айфон в 2023 році?\n'
                             '2) Що краще 13 чи 14?\n'
                             '3) Який айфон найпопулярніший?\n'
                             '4) Яка різниця між 14 і 15 айфоном?\n'
                             '5) Де краща камера айфон 13 чи 14?\n>>>>>>'))
        ask_question(question)
    #Кошик
    elif model == 'basket':
            print(f'Ось товар доданий до кошика ')
            checkout()
    # Додавання нового товару
    elif model == 'new':
        tovar_dod()
        print(Fore.LIGHTGREEN_EX,'Товар успішно додано', Fore.RESET)
    #Консультант
    elif model == 'consult':
        print(Fore.LIGHTGREEN_EX,'Ось номер консультанта: +380 66 374 0302',Fore.RESET)
    #Кінець програми
    elif model == 'break':
        print(Fore.RED,'Ви вийшли з програми', Fore.RESET)
        break
    #Видалення з кошика
    elif model == 'nobasket':
        print(f'Цей товар {basket} ви додали до кошика')
        n= input('Введіть назву товару який хочете видалити з кошика\n>>>>>')
        basket.remove(n)
        print(f'Ось товар який залишився {basket}')
    elif model == 'Iphone':
            model_tel = input('У нас є:\nIphone 12 Pro Max\nIphone 13 Pro Max\nIphone 14 Pro Max\nIphone 15 Pro Max\n'
                              'iPhone X\niPhone 11\niPhone 12\niPhone 8\n>>>>>>')
            if model_tel == 'Iphone 12 Pro Max':
                display_info(model_tel, '6.7 ", 2778x1284 (19.5:9), 458 ppi, 60 Гц', '256 ГБ, ОЗУ 6 ГБ', 'Apple A14.',
                             '4 модуля, 12 МП, + 12 МП',
                             'fullHD 60 к/с, ultraHD 4K, оптическая стабилизация, стабилизация матрицей',
                             '3687 мАч', '228 г', 23000)
                bask(model_tel)
            elif model_tel == 'Iphone 13 Pro Max':
                display_info(model_tel, '6.7 ", 2778x1284 (19.5:9), 458 ppi, 120 Гц', '128 ГБ, ОЗУ 6 ГБ', 'Apple A15.',
                             '4 модуля, 12 МП, + 12 МП',
                             'fullHD 60 к/с, ultraHD 4K, оптическая стабилизация, стабилизация матрицей',
                             '4352 мАч', '240 г', 31000)
                bask(model_tel)
            elif model_tel == 'Iphone 14 Pro Max':
                display_info(model_tel, 'OLED', '128 Гб', 'Apple A16 Bionic', '48 Мп 12 Мп, 12 Мп',
                             'Wi-Fi. Дo Спутникова система',
                             '4323 mAh', '240 г', 38000)
                bask(model_tel)
            elif model_tel == 'Iphone 15 Pro Max':
                display_info(model_tel, '6,1 дюйма', 'LTPO Super Retina XDR.', 'А17 pro.', '48 мп', '48 и 12 Мп',
                             ' 4441 mAh', '250 г.', 59000)
                bask(model_tel)
            elif model_tel == 'iPhone X':
                display_info(model_tel, '5.8", 2436x1125', '64/256 ГБ', 'Apple A11 Bionic', 'Дві 12 МП', '4K 60 к/с',
                             '2716 мАч', '174 г', 7000)
                bask(model_tel)
            elif model_tel == 'iPhone 11':
                display_info(model_tel, '6.1", 1792x828', '64/128/256 ГБ', 'Apple A13 Bionic', 'Дві 12 МП', '4K 60 к/с',
                             '3110 мАч', '194 г', 11000)
                bask(model_tel)
            elif model_tel == 'iPhone 12':
                display_info(model_tel, '6.1", 2532x1170', '64/128/256 ГБ', 'Apple A14 Bionic', 'Дві 12 МП',
                             '4K 60 к/с', '2815 мАч', '164 г', 16000)
                bask(model_tel)
            elif model_tel == 'iPhone 8':
                display_info(model, '4.7", 1334x750', '64/256 ГБ', 'Apple A11 Bionic', 'Одна 12 МП', '4K 60 к/с',
                             '1821 мАч', '148 г', 5000)
                bask(model_tel)

    elif model == 'Airpods':
        model_airpods = input('У нас є: \nAirPods Pro\nAirPods Pro Generation 2\nAirPods Max\n>>>>>>')
        if model_airpods == 'AirPods Pro':
             display_info(model_airpods, 'Bluetooth', '4 ГБ', 'Apple H1', 'Динамічні адаптивні враження', 'Двобічні мікрофони', '5 годин слухання музики','5.4 г', 4000)
             bask(model_airpods)
        elif model_airpods == 'AirPods Pro Generation 2':
                display_info(model_airpods, 'Bluetooth', '4 ГБ', 'Apple H2', 'Динамічні адаптивні враження', 'Двобічні мікрофони', '6 годин слухання музики',
                             '5.4 г', 10999)
                bask(model_airpods)
        elif model_airpods == 'AirPods Max':
                display_info(model_airpods, 'Bluetooth', 'Відсутній', 'Apple H1', 'Відсутній', 'Відсутній', '20 годин слухання музики',
                             '384 г',18999)
                bask(model_airpods)
    elif model == 'Macbook':
        model_mac = input('У нас є:\nMacBook Pro\nMacBook Air\n>>>>>>')
        if model_mac == 'MacBook Pro':
                display_info(model_mac, '13.3", 2560 x 1600', '256 ГБ SSD', 'Apple M1', 'Відсутній', 'Відсутній', '58.2 Вт*год', '1.4 кг', 47999)
                bask(model_mac)
        elif model_mac == 'MacBook Air':
                display_info(model_mac, '13.3", 2560 x 1600', '256 ГБ SSD', 'Apple M1', 'Відсутній', 'Відсутній', '49.9 Вт*год', '1.29 кг', 30999)
                bask(model_mac)

    elif model == 'Ipad':
        model_ipad = input('У нас є: \nIpad Mini\n ipad Pro\n>>>>>')
        if model_ipad == 'Ipad Mini':
                display_info(model_ipad, '8.3", 2266x1488', '64/256 GB', 'Apple A15 Bionic', '8 МП', '1080p','Li-Ion 19.3 Вт*год', '293 г', 25000)
                bask(model_ipad)
        elif model_ipad == 'ipad Pro':
                display_info(model_ipad, '12.9", 2732 x 2048', '256 ГБ', 'Apple M1', '12 МП', '4K', '10,090 мАч', '682 г', 45999)
                bask(model_ipad)
    elif model == 'Apple Watch':
        model_watch = input('У нас є: \nApple Watch 4\nApple Watch 5\nApple Watch 6\nApple Watch 7\nApple Watch 8\n>>>>>>')
        if model_watch == 'Apple Watch 4':
                display_info(model_watch, '40/44 мм', 'Відсутній', 'Apple S4', 'Відсутній', 'Відсутній', 'Відсутній', '30 г', 4000)
                bask(model_watch)
        elif model_watch == 'Apple Watch 5':
                display_info(model_watch, '40/44 мм', 'Відсутній', 'Apple S5', 'Відсутній', 'Відсутній', 'Відсутній', '30 г', 5000)
                bask(model_watch)
        elif model_watch == 'Apple Watch 6':
                display_info(model_watch, '40/44 мм', 'Відсутній', 'Apple S6', 'Відсутній', 'Відсутній', 'Відсутній', '30 г', 6000)
                bask(model_watch)
        elif model_watch == 'Apple Watch 7':
                display_info(model_watch, '41/45 мм', 'Відсутній', 'Apple S7', 'Відсутній', 'Відсутній', 'Відсутній', '32 г', 8000)
                bask(model_watch)
        elif model_watch == 'Apple Watch 8':
                display_info(model_watch, '41/45 мм', 'Відсутній', 'Apple S8', 'Відсутній', 'Відсутній', 'Відсутній', '32 г', 13000)
                bask(model_watch)
    else:
            print(Fore.RED,'Будь ласка, попробуйте ще раз!',Fore.RESET)

