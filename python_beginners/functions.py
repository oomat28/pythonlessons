""" functions  - функции """

def add_and_divide(x):
    print(x + 20 / 5)

# add_and_divide(10)
# add_and_divide(20)
# add_and_divide(30)

# функция -  именнованый блок кода, которы принимает какие либо значение, совершает над ними определенные действие и возврощяет результат их действие

# def prt():
#     print('hello world ')

# prt()

# def add2(num, num2):
#     result = num + num2
#     return result

# print(add2(2, 5))


# def func():
#     print('this is func')
#     return 

# def имя_функции(параметры):
#     тело функции

# имя_функции(аргументы)

# параметры - локальные переменные для функции, объявляются при создании функции

# аргументы - это значения для функции при вызове. Аргументов может быть столько, сколько параметров у функции

# return - ключевое слово, которое служит для возвращения результата выполнения функции. Является точкой выхода из функции


def sum_nums_from_list(nums):
    counter = 0
    for num in nums:
        counter += num
    return counter

sum_nums_from_list([1, 2, 3])


def annotated_sum(list_of_nums: list) -> int:
    """ Складывает все числа из списка """
    counter = 0
    for num in list_of_nums:
        counter += num
    return counter

annotated_sum([1, 2, 3, 4, 5])

# параметры бывают 2 типов:
# 1) обязательное
# 2) необязательное

def sub(x, y):
    return x - y

# sub(1) # TypeError
# sub(1, 2) # -1 
    
def sub2(x, y=10):
    return x -y 

# print(sub2(20)) #10
# print(sub2(50, 20)) #30

# def wrong_params(x=5, y):
#     pass

# def good_params(a, b, c, d, e=10, f=20):
#     pass

# аргументы бывают 2 типов:
# 1) именованные
# 2) позиционные

# pow(10, 20)
# pow(exp=10, base=10)


# add2(10, 20 , 30)
# add2(num3=10, num2=50, num1=25)
# add2(num3=120, 120, 20) # Error
# add2(10, 20, num3=50) # Ok


""" args, kwargs - arguments, keword arguments """

# *args - кортеж позиционных аргументов
# ** kwargs - словарь именнованых аргументов


def func(*args, **kwargs):
    print(args, '<- args')
    print(kwargs, '<- kwargs')

func()    

