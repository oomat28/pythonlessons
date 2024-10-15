""" List, Loops: for, while """

# list
# list() (Списки) - коллекция элементовю. Изменяемыйб упорядоченныйб индеуксируемй, итерируемый, тип данных.Используется для хранение данных

# Элементами списка могут быть любые типы данных

list_with_all_data_types = [1, 'String', True, False, None, [1,2], {'a':10}, {1,2}, ('a',1 ,'b')]


list_of_numbers = [1, 2, 3, 4, 5, [6, 7]]


# a = [1, 2, 3]
# # print('До', a)
# # a.append(4)
# # print('После', a)

# a.insert(4, 0.5)
# print(a)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# new_list = list1 + list2
# print(new_list)


""" замена элементов """
letters = ['a', 'b', 'c', 'd']
letters[3] = 'g'
# print(letters)

""" уддаление элементов """
letters = ['a', 'b', 'c', 'd']
letters.pop(2)
# print(letters)

letters = ['a', 'b', 'c', 'd']
deleted_el = letters.pop(2)
# print(deleted_el)
letters.pop()
# print(letters)

letters = ['a', 'a', 'b', 'c', 'd']
letters.remove( 'a')
# print(letters)



# letters.clear()
# print(letters)



# del letters[1]
# print(letters)


""" сортировка и копирование списка """

nums = [1, 2, 3, 4]
nums_copy = nums.copy()
nums_copy2 = nums[:]



# nums = [1, 2, 3, 4]
# nums2 = nums
# nums2.append(5)
# print(nums2)
# print(nums)
# print(nums is nums2)




nums_list = [8, 6, 10, 5]
nums_list.sort()
nums_list.sort(reverse=True)
# print(nums_list)


names = ['Kolya', 'Baimurat', 'Ivan', 'Alexandr']
# new_names = sorted(names)
# print(new_names)


nums_list.reverse()
# print(nums_list)

""" циклы """

# Цикл - многократное выпоолнение определенного участка кода

# иТЕРРИРУЕМЫЙ объект - объект, к которому можно применитть цикл

# 1) for
# nums_list = [1, 2, 3, 4, 5]
# for nums in nums_list:
#     print(nums)

# for - цикл,  который перебирает каждый элемент в итерируемом объекте и работает до тех пор, пока эти элементы не закончатся
# for элемент in итерируемый_об:
# тело цикла
# string = 'Hello world'
# for letter in string:
#     print(letter)

# new_nums = []
# for num in range(1, 21):
#     if num % 2 == 0:
#         new_nums.append(num)

# print(new_nums)


list_of_lists = [[1, 2, 3], ['Katya', 'Masha', 'Sanya'], [4, 5, 6]]

# for list_ in list_of_lists:
#     for element in list_:
#         print(element)


# for element in list_of_lists[-1]:
#     print(element)



# while - условие 
# while - цикл, который работает до тех пор, пока условие возвращает True

import time

# counter = 0
# while counter < 5:
#     print(counter)
#     print('Hellow world')
#     counter += 1
#     time.sleep(1)



# while True:
#     print('Hello world')

# CTRL + C - остановка бесконечного цикла/процесса

# msg = input('Введите сообщение или stop: ')
# while msg != 'stop':
#     print(f'Ваше сообщение\n{msg}')
#     msg = input('Введите сообщение или stop: ')


# while True:
#     msg = input('Сообщение или stop: ')
#     if msg == 'stop':
#         print('цикл остановлен')
#         break
#     print(msg) 



# break - оператор для остановки цикла
# contine - начинает цикл заново, пропуская остальное тело цикла

# a = 'Privetik'
# b = ''
# for letter in a:
#     if letter == 'i':
#         continue
#     b += letter

# print(b)

""" else в циклах """
nums = range(0, 101, 2)
result = 0
for num in nums:
    if num == 50:
        break
    result += num
else:
    print(result)




