# Циклы while, for

# a = 15
# b = 30
# c = 17

# while a < 23:
#     print(a)
# while b > c:
#     print(b, c)

# while a < 7:
#     if a == 5:
#         print(a)
#     a = a + 1
#бесконечный цикл получился




#range генератор последовательностей

# for i in range(10):
#     print(i)
# #Выведет цифры от 0 до 9
#
# for i in 'Hello':
#     print(i)
# #Выведет Hello но только в столбик



# for i in range(1,10):
#     if i == 5:
#         print(i)
#     else:
#         print("Unknown number")


# цикл while может быть бесконечным, цикл for нет



# i = 0
# while i < 10:
#     print(i ** 2)
#     i += 1





# pass_inst = 'qwerty'
# pass_user = ''
#
# while pass_inst != pass_user:
#     pass_user = input("Введите пароль: ")
#
# print("success login")

# print("Hello")
#
# n = 20
# i = 1
# while i <= n:
#     if i % 3 ==0:
#         print(i)
#     i += 1
# #Ответ 3 6 9 12 15 18
#
#
# n = 20
# i = 1
# while i < n and i < 10:
#     if i % 3 == 0:
#         print(i)
#     i += 1



# s = 0
# d = 1
#
# while d != 0:
#     d = int(input())
#     if d % 2 == 0:
#         continue
#     s += d
#     print('s= ', s)



# a = 0
# while True:
#     a = int(input('number: '))
#     if a == 10:
#         break



for i in 'hello':
    print(i)



for i in range(1,10,2):
    print(i)
# 2 - это шаг


for i in range(10):
    print(i)



for i in range(10):
    print(i ** 2)


for i in 'hello':
    print(i)


a = 'hello\nword'
print(a)
# \n - перенос строки



# i=1
# d=20
# for i in range(d):
#     print(i)


# a =['dsfg', 2, '100', 120]
# for i in a:
#     print(i)



# isdigit - состоит ли строка только из цифр
a =['dsfg', "2", '10', '120', 'dssdfs']
for i in a:
    if i.isdigit():
         print(int(i) ** 2)
    else:
          print('is not digit')

# Ответ:
# is not digit
# 4
# 100
# 14400
# is not digit



print('123'.isdigit())
# true

print('1223skjdsj'.isdigit())
# false






a =['dsfg', "2", '10', '120', 'dssdfs', 'jsbdhjbGYTXRG', 'GFFDhhgffhh']
for i in a:
    if i.isdigit():
         print(int(i) ** 2)
    else:
        if i == i.lower():
            print(i.capitalize())
        else:
          print('is not digit')

# ответ
# Dsfg
# 4
# 100
# 14400
# Dssdfs
# is not digit
# is not digit





# for i in range(-50,51):
#     if i % 13 == 0 or i ** 2 == 100:
#         print(f'Happy number: {i}')
#     elif i % 40 == 0:
#         print(i*1/2)
#     else:
#         print('not happy number')






# l = [1,-345,456,1,-23,456,23]
# print(max(i))



# l = [1,-345,456,1,-23,456,23, 67]
# b = 0
#
# for x in l:
#     if x > b:
#         b = x
#
# print(b)
#
#
# for item in l:
#     if item > b:
#         b = item
# print(b)




if 5 % 3 ==0:
    print('lol')
