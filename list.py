# a = ['apple','cherry','banana']
# b = []
# for i in a:
#     if 'a' in i:
#         b.append(i)
# print(b)

# a = [1,2,1.4]
# a.sort(reverse=True)
# print(a)


#                                                       Uy ishi 
#           1

# num = int(input('son kiritin: '))
# if num % 2 == 0:
#     print('son musbat natija esa ',num + 1)
# else:
#     print('son manfiy',num)

#           2

# num = int(input('son kiritin: '))
# if num % 2 == 0:
#     print('son musbat natija esa ',num + 1)
# else:
#     print('son manfiy',num - 2)

#           3

# num = int(input('son kiritin: '))
# if num % 2 == 0:
#     print('son musbat natija esa ',num + 1)
# elif num % 2 !=0:
#     print('son manfiy',num - 2)
# else:
#     print('son nolga teng natijasi esa ',num == 10)

#           4

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# if a % 2 == 0:
#     print('a son musbat')
# if b % 2 == 0:
#     print('b son musbat')
# if c % 2 == 0:
#     print('c son musbat')
# elif a % 2 != 0:
#     print('A son manfiy')
# elif b % 2 != 0:
#     print('B son manfiy')
# elif c % 2 != 0:
#     print('C son manfiy')

#           5

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# if a % 2 == 0:
#     print('a son musbat')
# if b % 2 == 0:
#     print('b son musbat')
# if c % 2 == 0:
#     print('c son musbat')
# if a % 2 != 0:
#     print('A son manfiy')
# if b % 2 != 0:
#     print('B son manfiy')
# if c % 2 != 0:
#     print('C son manfiy')

#           6

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a > b :
#     print(f'1-son katta', a)
# elif a < b :
#     print(f'2-son katta', b)

#           7                                             

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a > b and a < b:
#     print(a,b)
# else:
#     print('Xato')


#            8                                                

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a > b:
#     print('1-son', a)
# if a < b:
#     print('2-son',b)
# if a > b:
#     print('2-son', b)
# if a < b:
#     print('1-son',a)

#           9                                   

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a > b:
#     print(a , b)
# if b > a:
#     print(b + a)

#           10

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a != b:
#     print(a + b)
# elif a == b:
#     print(0)
# else:
#     print("ma'lumot xato")

#           11

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# if a != b and a > b or a < b:
#     print(a) and (b)
# elif a == b:
#     print(0)
# else:
#     print("ma'lumot xato")

#           12

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# k = a > b > c
# s = a < b < c
# if a > b > c:
#     print(k)
# elif a < b < c:
#     print(s)
# else:
#     print('Ma`lumot xato')

#           13

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# k = a > b > c
# s = a < b > c
# if a > b > c:
#     print(k)
# elif a < b > c:
#     print(s)
# else:
#     print('Ma`lumot xato')

#           14

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# k = a > b > c
# s = a < b > c
# i = k > s
# o = k < s
# if a > b > c:
#     print(k)
# elif a < b < c:
#     print(s)
# elif k > s:
#     print(i)
# elif k < s:
#     print(o)
# else:
#     print('Ma`lumot xato')

#           15


# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# yigindi = a + b + c
# kattasi = max(a, b, c)
# print(f'3 ta sonning yig`indisi {yigindi}ga teng')
# print(f'shu sonlarning kattasi {kattasi}ga teng')

#           16

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# yigindi = a + b + c
# kattasi = max(a, b, c)
# print(f'shu sonlarning kattasi {kattasi}ga teng')

#           17

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# if a < b < c or a > b > c:
#     a *=2
#     b *=2
#     c *=2
#     print(f'sonlarni ikkilantirilgandagi holati \n{a} \n{b} \n{c}')
# else:
#     a *=-1
#     b *=-1
#     c *=-1
#     print(f'sonlarni ishorasi o`zgargan holati \n{a} \n{b} \n{c}')

#           18

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# if a == b or a != b:
#     print(f'a ni tartib raqami {a}')
# elif b == c or b != c:
#     print(f'b ni tartib raqami {b}')
# elif c == a or c != a:
#     print(f'c ni tartib raqami {c}')

#           19

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# d = int(input('4-sonni kiritin: '))
# if a == b or a != b:
#     print(f'a ni tartib raqami {a}')
# elif b == c or b != c:
#     print(f'b ni tartib raqami {b}')
# elif c == d or c != d:
#     print(f'c ni tartib raqami {c}')
# elif d == a or d != a:
#     print(f'd ni tartib raqami {d}')

#           20

# a = int(input('1-sonni kiritin: '))
# b = int(input('2-sonni kiritin: '))
# c = int(input('3-sonni kiritin: '))
# k = a - b
# h = b - c
# s = c - a
# d = b - a
# f = c - b
# e = a - c
# if a - b and b - a:
#     print('a va b orasidagi masofa ', k)
# if b - c and c - b:
#     print('b va c orasidagi masofa ', h)
# if c - a and a - c:
#     print('c va a orasidagi masofa ', s)

#           21

# x = int(input('x-sonni kiritin: '))
# o = int(input('o-sonni kiritin: '))
# y = int(input('y-sonni kiritin: '))
# if o * x or o * y:
#     print(f'bu sonlar kordinata o`qida yotadi {x} {o} {y}')
# else:
#     print(0)

#           22

# x = int(input('x-sonni kiritin: '))
# o = int(input('o-sonni kiritin: '))
# y = int(input('y-sonni kiritin: '))
# if o / x or o / y:
#     print(f'bu sonlar kordinata o`qida yotmaydi {x} {o} {y}')
# else:
#     print('bu sonlar kordinata o`qida yotadi')





