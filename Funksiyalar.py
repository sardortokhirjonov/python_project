#                       Def deine so'zidan olingan bo'lib aniqlamoq degan ma'noni anglatadi

#                      RETURN printni qaytaradi va NONE qaytarmaydi print o'rniga RETURN qo'yiladi

# def salom_ber():
#     print("assalomu aleykum")

# # lis = range(100)
# # for i in lis:
# #     print(i)

# def hello():
#     print("good morning")
# print(hello())


# def salom_ber():
#     print("assalomu aleykum")
# print(salom_ber())


# def salom_ber(ism, familya, yosh):
#     print(f"Assalomu aleykum {ism.title()} {familya.title()}ning yoshi {yosh} da")
# ism = "Sardor"
# ism1 = "Vali"
# familya = "Tohirjonov"
# familya1 = "Aliyev"
# yosh = 15
# yosh1 = 14
# print(salom_ber(ism, familya, yosh))
# print(salom_ber(ism1,familya1, yosh1))



# def salom_ber(ism, familya, yosh):
#    return(f"Assalomu aleykum {ism.title()} {familya.title()}ning yoshi {yosh} da")
# print(salom_ber(yosh=15, familya="Tohirjonov", ism="sardor",))


# def kvadrat(x, y = 2):
#     s = x ** y
#     print(s)
# print(kvadrat(4))




#                                                       Uy ishi

#           1

# def tugilgan_yilini_sorash(ismi, yoshi):
#     tugilgan_yili = 2023 - yoshi
#     return(f"Assalomu aleykum {ismi.title()}ning yoshi {yoshi} da tug'ilgan yili {tugilgan_yili}")


# ismi = input("Ismingizni kiriting: ")
# yoshi = int(input("yoshingizni kiriting: "))
# print(tugilgan_yilini_sorash(ismi, yoshi))

#           2

# def kvadrat_va_kub():
#     son_kirit2 = int(input("Son kiriting va men kvadratga oshiraman: "))
#     son_kirit3 = int(input("Son kiriting va men kubga oshiraman: "))
#     son_kvadrati = son_kirit2 ** 2
#     son_kubi = son_kirit3 ** 3
#     print(f"sonning kvadrati {son_kvadrati} \nsonning kubi {son_kubi}")
# print(kvadrat_va_kub())

#           3

# def son_juf_yoki_toq():
#     son = int(input('son kiriting: '))
#     if son % 2 == 0:
#         a = f"Siz kiritgan son {son} juft son."
#     else:
#         a = f"Siz kiritgan son {son} toq son."
#     return a
# print(son_juf_yoki_toq())

#           4

# def son_katta_kichik():
#     son = int(input('1-son kiriting: '))
#     son1 = int(input('2-son kiriting: ')) 
#     if son > son1:
#         print("1-son katta")
#     elif son < son1:
#         print("2-son katta")
#     elif son == son1:
#         print("sonlar o'zaro teng")
# print(son_katta_kichik())

#                                                                                                           08.11.2023
#                                                       Mavzu: 2-dars Funksiyalar

#           1

# def son_katta_kichik():
#     son = int(input('1-son kiriting: '))
#     son1 = int(input('2-son kiriting: ')) 
#     son2 = int(input('3-son kiriting: ')) 
#     if son > son1 and son > son2 or son == son1 and son == son2 or son == son1 and son > son2 or son > son1 and son == son2:
#         print(f"siz kiritgan 1-son {son} katta")
#     elif son < son1 and son1 > son2 or son1 == son and son1 == son2:
#         print(f"siz kiritgan 2-son {son1} katta")
#     elif son < son2 and son1 < son2 or son2 == son and son2 == son1:
#         print(f"siz kiritgan 3-son {son2} katta")
#     elif son == son1 == son2:
#         print("sonlar o'zaro teng")
# son_katta_kichik()

#           2

# def orta_arifmetika():
#     son1 = int(input("1-son kiriting: "))
#     son2 = int(input("2-son kiriting: "))
#     son3 = int(input("3-son kiriting: "))
#     son4 = int(input("4-son kiriting: "))
#     summma = (son1 + son2 + son3 + son4) // 4
#     print(summma)
# orta_arifmetika()

#                                               hohlagancha input qo'shish

# def arifmetik(n):
#     summa = 0 
#     for i in range(n):
#         son = int(input(f"{i + 1} sonni kiriting: "))
#         summa += son
#     print(summa / n)
# arifmetik(4)


#                                               Uy ishi 
#           1

# def geometrik_arifmetik(n):
#     summa = 0 
#     for i in range(n):
#         son = int(input(f"{i + 1} sonni kiriting: "))
#         summa += son
#     print(summa / n)
# geometrik = int(input("Son kiriting: "))
# geometrik_arifmetik(geometrik,4)

#           2

# def perimetr():
#     print("Assalomu aleykum \nsiz menga son kiritasiz va men uni sizga perimetirini aniqlab beraman !!!")
#     shakl = int(input("shakl turi 4 dan 6 sonigacha bo'lishi lozim \n4ta burchakli:  \n5ta burchakli:  \n6ta burchakli: "))
#     if shakl == 4 or shakl == 5 or shakl ==6:
#         print(f"siz kiritgan shaklning perimetri: {(shakl +shakl) * 2} ga teng")
#     elif shakl == 3:
#         print(f"uzur siz kiritgan son uchburchak perimetri!!! ")
#     else: 
#         print("Uzur siz kiritgan sondan perimetr aniqlay olmadik!!! ")
# perimetr()

#           3

# def yuzasi():
#     print("Assalomu aleykum \nsiz menga son kiritasiz va men uni sizga yuzasini aniqlab beraman !!!")
#     shakl = int(input("shakl turining yuzasini aniqlashingiz mukin: "))
#     if shakl:
#         print(f"siz kiritgan shaklning yuzasi: {shakl * 2 } ga teng")
#     else: 
#         print("Uzur siz kiritgan sondan yuzasini aniqlay olmadik!!! ")
# yuzasi()



#                                                                                                                       10.11.2023

#                           Mavzu:   Takrorlash

# n = int(input("Nechta son kiritasiz:"))
# def juft_va_toq_sonlar(n):
#     list_ = []
#     index = 1
#     for i in range(1, n+1):
#         son = int(input(f"{i}-sonni kiriting: "))
#         index += son
#         if son % 2 == 0:
#             list_.append(son)
#     print(list_)
# juft_va_toq_sonlar(n)




#                                       Uy ishi

# UY ISHI
# 1. Ro'yxatdan birinchi va ohirgi elementni chiqaring:
# harflar = ['d','a','s','t','u','r','c','h','i']

# 2. Ro'yxat boshidan 4, ohiridan 4 elementni qirqib, ekranga chiqaring
# harflar = [50,70,30,20,90,10,50]

# 3. Foydalanuvchi siz belgilagan formatda bir qancha mahsulotlarni kiritsin. 
# So'ng siz shulardan birinchi va ohirini chiqaring

# 4. ['olcha', 'olma', 'nok', 'anor'] shu yerdan olcha va olma o'rniga bodring va 
# sabzi qiymatiga o'zgartiring. Asl va o'zgargan ro'yxatni ekranga chiqaring:

# 5. Bizda ['olma', 'nok'] bozorlik ro'yxati berilgan. Foydalnuvchi yana 
# bir muhim mahsulotni kiritadi, uni muhim bo'lgani uchun ro'yxat 
# boshiga kiritamiz:


#           1

# harflar = ['d','a','s','t','u','r','c','h','i']
# print(f"ro'yxatdagi 1-ma'lumot {harflar[0]} ga teng \nro'yxatdagi 9-ma'lumot {harflar[8]} ga teng")

#           2

# harflar = [50,70,30,20,90,10,50]

#           3

# n = input("marhamat 10ta mahsulot nomini kiritng: ")
# index = 0
# for i in range(n, n + 1):
#     son = input(f"{i}-sonni kiriting: ")









# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop().title()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])       # bahola(talabalar[:]) bu bizga nusxa olib beradi

# print(baholar)
# print(talabalar)
    

# def yigindi(*sonlar):      
#     print(yigindi(1, 2, 45, 35, 46, 78))
# sonlar = [0] + [1]


#                               sonlarni bir biriga qo'shish
# def yigindi(*sonlar):
#     yigindi = 0
#     for i in sonlar:
#         yigindi = yigindi +  i
#     return yigindi
# print(yigindi(2, 2, 45, 35, 46, 78))

#                                sonlarni aylantirish
# def yigindi(*sonlar):
#     yigindi = 0
#     for i in sonlar:
#         print(i)
#     return yigindi
# print(yigindi(2, 45, 35, 46, 78)) 


# def yigindi(*sonlar):
    # yigindi = 0  
    # for i in sonlar:
    #     print(i)
    # return sum(sonlar)

# print(yigindi(2, 45, 35, 46, 78, )) 

# def yigindi(y, x, *sonlar):
#     y = y ** x
#     sonlar = sonlar ** x
#     return y , sonlar 

# print(yigindi(2, 45, 35, 46, 78))





# def yigindi(y, x, *sonlar):
#     return y + x + sum(sonlar)
# print(yigindi(2, 45, 35, 46, 78))


# def ortadagi_son(*sonlar):
#     return sonlar[1]
# print(ortadagi_son(846, 192, 389))



# def ortadagi_son(*sonlar):
#     a = int(input("1-sonni kiriting: "))
#     b = int(input("2-sonni kiriting: "))
#     c = int(input("3-sonni kiriting: "))
#     return sonlar[1]







# def ortadagi_son(*sonlar):
#     if [1] > [2] > [3]:
#         return("siz kiritgan 1-son katta")
#     if [1] < [2] > [3]:
#         return("siz kiritgan 2-son katta")
#     if [1] < [2] < [3]:
#         return("siz kiritgan 3-son katta")
#     return sonlar
# print(ortadagi_son(389, 192, 846))  

 
  
    



# def ortadagi_son(*sonlar):
#     if [2] < [1] > [3]:
#         return(f"siz kiritgan 1-son katta"[1])
#     elif [1] < [2] > [3]:
#         return(f"siz kiritgan 2-son katta"[2])
#     elif [1] < [3] > [2]:
#         return(f"siz kiritgan 3-son katta"[3])
#     return sonlar
# print(ortadagi_son(846, 192, 389))












#           Funksiyalarda ismini va yoshini so'rab yilini chiqaruvchi misol 

# def F_I_O_and_Age():
#     familya = str(input("familyangizni kiriting: ").title())
#     name = str(input("ismingizni kiriting: ").title())
#     age = int(input("yoshingizni kiriting: "))
#     hozir = 2023 - age
#     parol = int(input("parolingizni kiriting \nparol esa 8ta harf yoki so'zdan iborat bo'lsin :"))
#     print(" ")
#     if parol ==len(8):
#         parol == '********'
#     return(f"{familya} {name} \n{age} yoshdasiz \nsiz esa {hozir}-yilda tug'ilgansiz")
# print(F_I_O_and_Age())


