""" try except - ошибки и исключение в python """

# исключение - проблема в логике работы в коде
# ошибка - проблема в написании/синтексисе кода
# исключение можно выловить и обработать. Ошибки - нельза

# a = 10
# b = 20
# NameError 

# 10 / 0
# ZeroDivisionError

# names = {'Misha': 20, 'Nur': 30}
# names['Azamat']
# KeyError

# list_ = [1, 2, 3]
# list_[5]
# IndexError

# num = 10
# num += 'string'
# TypeError

# int(10) ok
# int(10.0) ok
# int('20') ok
# int('hello') ValueError
# ValueError

# string = 'hello world'
# string.append('b')
# AttributeError

# import wrong_module
# ModuleNotFoundError
# from math import wrong_func
# ImportError

# contacts = {
#     'Valera': 996774888333,
#     'Adilet': 996887993002
# }
# contacts['Zaynab']
# print('Hello')
# print(1 + 1)

# trt except - конструкция для обработки исключений

# try:
#     contacts = {
#         'Valera': 996774888333,
#         'Adilet': 996887993002
#     }
#     contacts['Zaynab']
# except:
#     print('Нет токого имени')

# print('Hello')
# print(1 + 1)


# try:
#     print('Hello')
#     # 10 / 0
#     print('world')
# except:
#     print('что то пошло не так')
# else:
#     print('try отроботал без ошибок')
# finally:
#     print('я отрабатываю в любом случае')

# nums = [1, 2, 3, 4]
# try:
#     a= nums [-1]
#     nums[10]
# except IndexError:
#     print('возникла ошибка')

# try:
#     print(c)
#     10/0
#     'string'.extend()
# except(NameError, ZeroDivisionError):
#     print('нет токого имени или деление на ноль')
# except AttributeError:
#     print('нет такого атрибута')
Exception

# try:
#     print(m)
# except Exception as Error:
#     print(Error)


# try:
#     код, который потенциально вызвать исключение
# except:
#     блок кода, который сработает, если в try было вызвано исключение
# else:
#     выполняется если в try не было исключений
# finally:
#     выполняется в любом случае

# raise - ключевое слово для поднятия/вызова ошибок
# money = 0
# if money == 0:
#     raise ValueError('недостаточно денег на карте')

# try:
#     raise Exception('My error')
# except Exception:
#     print('error obrabotana')
# finally:
#     print('programa zafershena')


# try:
#     for i in range(10)
#         print(i)
# except SyntaxError:
#     print('неправильно написан код')


# contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# try:
#     name = input('Введите имя ').title()
#     contacts[name]
# except KeyError:
#     print('Нет такого имени')


# contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# name = input('Введите имя ').title()
# if name not in contacts:
#     print('Нет такого имени')
# else:
#     contacts[name]
















































































