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

# """ тернарный оператор """
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     print('Сообщение длиннее 10')
# else:
#     print('Сообщение короче 10')

# msg = input('Введите сообщение ')

# res = 'Сообщение длиннее 10' if len(msg) > 10 else 'Сообщение короче 10'
# print(res)


# house = {
#     "color": "white",
#     "category": "elite",
#     "rooms": 4,
#     "warmness": True
# }
# deleted_key = house.pop('category')
# print(house)
# print(deleted_key)

# deleted_pair = house.popitem()
# print(house)
# print(deleted_pair)

# del house['rooms']
# print(house)

# house.clear()
# print(house)


# my_set = {1, 'string', 2, 'a', 'b', 3}
# print(my_set)

# my_set2 = {'h', 'k', 'a', 'b'}
# print(my_set2)

# my_set = {1, 2, 3, 4}
# print(my_set)

# empty_set = {}
# print(type(empty_set))

# real_empty_set = int()
# print(type(real_empty_set))

# class_a = {'Aktan', 'Aygul', 'Mayrash', 'Artyom'}
# class_b = {'Malik', 'Aygul', 'Eldos', 'Aktan'}

# inter = class_a.intersection(class_b)
# print(class_a & class_b)
# print(inter)

# diff = class_a.difference(class_b)
# diff2 = class_b.difference(class_a)
# print(class_a - class_b)
# print(diff)
# print(diff2)

# print(class_a.union(class_b))
# print(class_a | class_b)


fruits = {'apple', 'banana', 'kiwi', 'tangerin'}
vegetables = {'carrot', 'potato', 'tomato', 'apple'}

# fruits.intersection_update(vegetables)
# print(fruits)

# vegetables.difference_update(fruits)
# print(vegetables)

# fruits.update(vegetables)
# print(fruits)

# a = {1, 2, ('a', 'b')} # TypeError
# print(a)

# my_unique_set = {True, False, 1, 0, 'string', (1, 2)}
# print(my_unique_set)

# passport = {'name': 'Oomat', 'Last_name': 'Maksatbekov', 'age': 16, 'gender': 'M'}

# print(passport['name'])
# print(passport['Last_name'])
# print(passport['gender'])
# print(passport['age'])

# my_dict2 = dict(name='Oomat', age=16)
# print(my_dict2)

# my_dict3 = dict([('name', 'Vasya'), ('age', 23)])
# print(my_dict3)

# my_dict4 = dict.fromkeys(['a', 'b', 'c', 'd', 'key'], 10)
# print(my_dict4)

# print(human)

# human = {
#     'name': 'oomat',
#     'last_name': 'maksatbekov',
#     'age': 52,
#     'friends': ['niga', 'hefor1', 'nefor2', 'pod kabluk'],
#     'age': '16'
    
# }
# print(human)

# car = {
#     "marka": "Toyota",
#     "model": "Camry",
#     "color": "black",
#     "volume": 3.2,
#     "year": 2012
# }

# print(car['marka'])
# # print(car['kuzov'])

# print(car.get('marka'))
# print(car.get('kuzov')) # None
# print(car.get('kuzov', 'Такого ключа нет!')) # 'Такого ключа нет!'

# print(car.setdefault('year'))
# print(car.setdefault('kuzov', 'Sedan'))
# print(car)

# house = {
#     "color": "white",
#     "category": "elite",
#     "rooms": 4,
#     "warmness": True
# }

# house['area'] = '30x40'
# # print(house)
# house.update({'floor': 3, 'door': 'wooden'})
# print(house)

# claer 

# slovari = {1, 2, 3, 'oomat'}
# slovari.clear()
# print (slovari)

# 

# slovari = {1, 2, 3, 'oomat'}
# slovari = slovari.copy()
# print(slovari.copy())

# copy

# my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
# my_dict_copy = my_dict.copy()
# my_dict = {'kiwi': 1}
# print(my_dict_copy)

# classmethod dict.fromkeys(seq[, value])

# keys = ['a', 'b', 'c']
# my_dict = dict.fromkeys(keys) 
# print(my_dict)
# default_value_dict = dict.fromkeys(keys, 996) 
# print(default_value_dict)

#get(key[, default])

# a = {'one': 1, 'two': 2, 'three': 3}
# print(a.get('one'))
# print(a.get('four'))

# items

data = {'one': 1, 'two': 2, 'three': 3}

for key, value in data.items():
    print(key, value)