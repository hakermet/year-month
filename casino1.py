import random
import time
from colorama import Fore
while True:
    l = []
    l_1 = []
    x = 0
    rules=input(
                  '1.грати в Black Jack \n'
                  '2.грати в чорне\червоне \n')
    if rules == '1':
        print('Ви граєте в гру під назвою Black Jack')
        user_cash = int(input('Введіть ваш бюджет----->'))
        if user_cash >= 100:
            print('Ваш бюджет дозволяє вам зіграти в гру')
        if user_cash < 100:
            print('Ваш бюджет не дозволяє вам зіграти в гру')
            print('Казино для вас закрито')
            break
        if x == 0:
            print('Гра почалась')
            stavka = int(input('На яку ставку граєте?--------->'))
            if stavka > user_cash:
                print('Ваш бюджет---->',user_cash)
                continue
            user = random.randint(1,11)
            l.append(user)
            print('Ви',user)
            user_1 = random.randint(1,11)
            l_1.append(user_1)
            print('Крупи',user_1)
            x += 1
            slovo=input('Якщо берете----->+ ')
            for slovo in '+':
                 user = random.randint(1, 11)
                 l.append(user)
                 print('Ви',sum(l))
                 if x:
                  user_1 = random.randint(1, 11)
                  l_1.append(user_1)
                  print('Крупи', sum(l_1))

            if l < l_1:
                      print('Ви програли')
                      user_cash-=stavka
                      print('Ваш бюджет----->', user_cash)
            if  user_1 > 21 > user:
                print('Ви виграли')
                user_cash+= stavka * 2
                print('Ваш бюджет----->', user_cash)
                vuvod=input('Вивести гроші так or ні-------->')
                if vuvod == 'так':
                    vuvod_1=input('Введіть данні карти')
                    vuvod_2=input('Введіть пін код')
                    if vuvod_1 != 17:
                              if vuvod_2 != 5:
                                  time.sleep(5)
                                  print('Транзакція обробляється...')
                                  print('Транзакція пройшла успішно')
                    else:
                     print('Неправильно введені данні')
                if vuvod == 'ні':
                    print('')
            if l == l_1:
                user_cash += stavka
                print('Нічия ')
                print('Ваш бюджет----->', user_cash)
            if l > l_1:
                      print('Ви виграли')
                      user_cash+=stavka * 2
                      print('Ваш бюджет----->',user_cash)
                      vuvod = input('Вивести гроші так or ні')
                      if vuvod == 'так':
                          vuvod_1 = input('Введіть данні карти')
                          vuvod_2 = input('Введіть пін код')
                          if vuvod_1 != 17:
                              if vuvod_2 != 5:
                               print(time.sleep(5),'Транзакція обробляється...')
                               print('Транзакція пройшла успішно')
                          else:
                           print('Неправильно введені данні')
            if user > 21 >user_1:
                user_cash -= stavka
                print('Ваш бюджет----->', user_cash)
                print('Ви програли')
            elif user_cash == 0:
                break
    if rules == '2':
        print('Ви граєте в гру під назвою чорне\червоне')
        print('Гра почалась')
        baza =int(input(f'Вибери на яку фішку ти ставиш----> 1)червона або 2)чорна \n'
                     f'------->'))
        user_cash = int(input('Введіть ваш бюджет\n'
                              '----->'))
        stavka = int(input('На яку ставку граєте?\n'
                           '--------->'))

        if baza == 1:
            s = random.randint(1, 2)
            if s == 1:
                print(s)
                user_cash += stavka * 2
                print('Ти виграв')
                print('Ваш бюджет---->', user_cash)
            if s == 2:
                print(s)
                print('Ти програв')
                user_cash -=stavka
                print('Ваш бюджет---->', user_cash)
                print('Спробуй ще раз')
        if baza == 2:
            s = random.randint(1, 2)
            if s == 2:
                print(s)
                user_cash += stavka * 2
                print('Ти виграв')
                print('Ваш бюджет---->', user_cash)

            if s == 1:
                print(s)
                user_cash -= stavka
                print('Ти програв')
                print('Ваш бюджет---->', user_cash)
                print('Спробуй ще раз')


















