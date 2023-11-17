#                                               1

# n = int(input("Nechta son kiritasiz:"))
# def juft_va_toq_sonlar(n):
#     list_ = []
#     for i in range(1, n+1):
#         son = int(input(f"{i}-sonni kiriting: "))
#         if son % 2 == 0:
#             list_.append(son)
#     print(list_)
# juft_va_toq_sonlar(n)

#                                                2

# n = int(input("Nechta son kiritasiz:"))
# def juft_va_toq_sonlar(n):
#     for i in range(1, n+1):
#         son = int(input(f"{i}-sonni kiriting: "))
#         if son % 2 == 0:
#             print(f"siz kiritgan son {son + 1} ga teng")
#         else:
#             print(f'siz kirtgan son {son - 2} ga teng')
#     return()
# juft_va_toq_sonlar(n)

#                                                3

# n = int(input("Nechta son kiritasiz:"))
# def juft_va_toq_sonlar(n):
#     for i in range(1, n+1):
#         son = int(input(f"{i}-sonni kiriting: "))
#         if son % 2 == 0:
#             print(f"siz kiritgan son {son + 1} ga teng")
#         elif son % 2 != 0:
#             print(f'siz kirtgan son {son - 2} ga teng')
#         elif son == 0:
#             print(f"siz kiritgan son no'la teng bo'lgani uchun son 10 ga almashadi {son == 10}")
#     return()
# juft_va_toq_sonlar(n)

#                                               4

# def katta_kichik():
#     son1 = int(input("1-sonni kiriting: "))
#     son2 = int(input("2-sonni kiriting: "))
#     if son1 > son2:
#         print(f"siz kiritgan 1-son katta {son1}")
#     elif son1 < son2:
#         print(f"siz kiritgan 2-son katta {son2}")
#     return(f"siz kirtgan sonlar:", son1, son2)
# print(katta_kichik())

#                                               5

# def kichkinasi_qoshilishi():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     if a > b:
#         print(a + b)
#     elif b > a:
#         print(b - a)
#     return(f"siz kirgan son {a} ga tengligi uchun sonlar qo'shildi" or f"siz kiritgan son {b} ga tengligi uchun ayirildi")
# print(kichkinasi_qoshilishi())

#                                               6

# def teng_yoki_tengemas():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     if a != b and a > b or a < b :
#         print(a) and (b)
#     elif a == b:
#         print(0)
#     else:
#         print("ma'lumot xato")
#     return(f"siz kiritga sonlar", a, b)
# print(teng_yoki_tengemas())

#                                               7

# def ucta_sonni_taqqoslash():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     k = a > b > c
#     s = a < b < c
#     if a > b > c:
#         print(k)
#     elif a < b < c:
#         print(s)
#     else:
#         print('Ma`lumot xato')
# ucta_sonni_taqqoslash()

#                                               8

# def taqqoslash():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     k = a > b > c
#     s = a < b > c
#     i = k > s
#     o = k < s
#     if a > b > c:
#         print(k)
#     elif a < b < c:
#         print(s)
#     elif i:
#         print(i)
#     elif o:
#         print(o)
#     else:
#         print('Ma`lumot xato')      
# taqqoslash()

#                                               9

# def uchata_sonni_taqqoslash_va_yigindisi():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     yigindi = a + b + c
#     kattasi = max(a, b, c)
#     return(f'3 ta sonning yig`indisi {yigindi}ga teng', f'shu sonlarning kattasi {kattasi}ga teng')
# print(uchata_sonni_taqqoslash_va_yigindisi())

#                                               10

# def sonlarning_ikkilantirilgan_holati():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     if a < b < c or a > b > c:
#         a *=2
#         b *=2
#         c *=2
#         return(f'sonlarni ikkilantirilgandagi holati \n{a} \n{b} \n{c}')
#     else:
#         a *=-1
#         b *=-1
#         c *=-1
#         return(f'sonlarni ishorasi o`zgargan holati \n{a} \n{b} \n{c}')
# print(sonlarning_ikkilantirilgan_holati())

#                                               11

# def sonlarni_tartiblangan_holati():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     if a == b or a != b:
#         return(f'a ni tartib raqami {a}')
#     elif b == c or b != c:
#         return(f'b ni tartib raqami {b}')
#     elif c == a or c != a:
#         return(f'c ni tartib raqami {c}')
# print(sonlarni_tartiblangan_holati())

#                                               12

# def sonlar_orasidagi_masofa():
#     a = int(input('1-sonni kiritin: '))
#     b = int(input('2-sonni kiritin: '))
#     c = int(input('3-sonni kiritin: '))
#     k = a - b   
#     h = b - c
#     s = c - a   
#     d = b - a
#     f = c - b
#     e = a - c
#     if a - b and b - a:
#         return('a va b orasidagi masofa ', k)
#     if b - c and c - b:
#         return('b va c orasidagi masofa ', h)
#     if c - a and a - c:
#         return('c va a orasidagi masofa ', s)
# print(sonlar_orasidagi_masofa())

#                                               13

# def kordinata_oqi():
#     x = int(input('x-sonni kiritin: '))
#     o = int(input('o-sonni kiritin: '))
#     y = int(input('y-sonni kiritin: ')) 
#     if o * x or o * y:
#         return(f'bu sonlar kordinata o`qida yotadi {x} {o} {y}')
#     else:
#         return(0)
# print(kordinata_oqi())

#                                               14

# def korinata_oqida_yotadi_yoki_yotmaydi():
#     x = int(input('x-sonni kiritin: '))
#     o = int(input('o-sonni kiritin: '))
#     y = int(input('y-sonni kiritin: '))
#     if o / x or o / y:
#         return(f'bu sonlar kordinata o`qida yotmaydi {x} {o} {y}')
#     else:
#         return('bu sonlar kordinata o`qida yotadi')
# print(korinata_oqida_yotadi_yoki_yotmaydi())

#                                               15

# def perimetri_va_yuzasi():
#     a = int(input('1-son kiriting: '))
#     b = int(input('2-son kiriting: '))
#     c = int(input('3-son kiriting: '))
#     c = (a **2 + b ** 2) ** (1/2)
#     p = a + b + c
#     return(f'gipatezuda{c} \nperimetri{p}')
# print(perimetri_va_yuzasi())


#                                















































































































#mashina avto salonlar

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}") 