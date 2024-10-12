""" Условные выражения (if-else-elif) """#

# bool() - Неизменяемый тип данныхб которым имеет всего 2 значение : True False

# 10 > 2 # True
# < - меньше
# > - больше
# <= - Меньше или ровно

# >= - Больше или ровно
# != неравенсто
# == - равенство

# print(25 == 23) # False
# print(25.0 == 25) # True
# print('яблоко' > 2)# Type Erore

# print(bool(2))# Truer
# print(bool(-2))# True


# print(bool('it'))# Truer
# print(bool(''))# False

# bool([]) # false
# bool({}) # false
# bool(set()) # false
# bool(None) # false

# """  if else """

# num = 15
# if num > 20:
#     print('num больше 20')
# else:
#     print('num  Не больше 20')


# temp  = 40

# if temp < 20:
#     print('холодно')
# else:
#     if temp < 30:
#         print('тепло')
#     else:
#         if temp > 35:
#             print('жарко') 

# """ elif """
# temp = 40
# if temp < 20:
#     print('холодно')
# elif temp < 30:
#     print('тепло')
# elif temp > 35:
#     print('жарко')
# else:
#     print('еверная температура')

# mark =input ('Введите оценки от 1 до 5')
# if mark.isdigit():
#     mark = int(mark)
#     msg = ''
#     if mark == 5:
#         msg = 'Ты молодец'
#     elif mark == 4:
#         msg = 'хорошо'
#     elif mark == 3:
#         msg = 'так себе'
#     elif mark == 2:
#         msg = 'плохо'
#     elif mark == 1:
#         msg = 'очень плохо'

#     print(msg)

# """ and, or, not """

# age = 12
# if age >= 18 and age < 28:
#     print('Входите')
# else:
#     print('Входа нет')

""" and, or, not """
# age = 18
# if age >= 18 and age < 28:
#     print('Входите')
# else:
#     print('Входа нет')

# False # False
# True # True
# False and False # False
# True and True # True
# False and True # False
# True and False # False

# False or False # False
# True or True # True
# False or True # True
# True or False # True

# not True # False
# not False # True

# (False or True) and (False and False) # False

""" is, ==, in """

# a = [1,2,3]
# b = [1,2,3]

# print(a is b)
# print(a == b)

# string = 'Hello world'
# print('world' in string)

""" тернарный оператор """
msg = input('Введите сообщение ')
if len(msg) > 10:
    print('Сообщение длиннее 10')
else:
    print('Сообщение короче 10')

msg = input('Введите сообщение ')

res = 'Сообщение длиннее 10' if len(msg) > 10 else 'Сообщение короче 10'
print(res)

