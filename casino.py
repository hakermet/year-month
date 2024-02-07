
# def s():
#     a = input('Введіть прізвище\n>>>>')
#     q=input('В рядок чи в стовпець\n>>>>>')
#     if q == 'рядок':
#         with open('s.txt','w',encoding='utf-8') as c:
#             c.write(a)
#         print('file append')
#     if q == 'стовпець':
#         with open('ghj.txt', 'w', encoding='utf-8') as h:
#             for x in a:
#                 h.write(x + '\n')
#                 print(x)
#
# def d():
#     with open('s.txt', 'r', encoding='utf-8') as b:
#         b.read()
#
# s()
# d()
# def write_to_file(sp,filenme='input.txt'):
#     with open('s.txt','w',encoding='utf-8') as c:
#         for i in sp:
#             c.write(str(i )+ '\n')
#
# def calculation(filenme='input.txt'):
#     c=[]
#     dod=1
#     suma=0
#     try:
#         with open('s.txt', 'r', encoding='utf-8') as b:
#              c=b.read().splitlines()
#             print(c)
#         for i in range(len(c)):
#             if i%2 ==0:
#                 dod *=c[i]
#             else:
#                 suma+=c[i]
#     except:
#         print('error')
# def number():
#     try:
#         user=list(map(float,input('Введіть 10 чисел').split(' ')))
#         if len(user)==10:
#
#             write_to_file(user)
#             calculation()
#
#     except:
#         print('error')
#     else:
#         print('Данні успішно додано')
#
# if __name__ == '__main__':
#     number()
# def file():
#     try:
#         with open(filename,'r',encoding='utf-8') as x:
#            content= x.read()
#         print(content)
#         # with open('read1.txt','w',encoding='utf-8') as a:
#         #     for a in :
#         #       a.write()
#     except Exception as error:
#         print(error)
# def write(data):
#     try:
#         with open(filename, 'r', encoding='utf-8') as x:
#             content = x.read()
#         print(content)
#         # with open('read1.txt','w',encoding='utf-8') as a:
#         #     for a in :
#         #       a.write()
#     except Exception as error:
#         print(error)
# file()
