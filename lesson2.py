# parol = int(input('Ведите пароль'))

# if parol == 2008:
#     print('Успешный вход')
# else:
#     print('Неверный пароль')

# nums = [1, 2, 3, 4, 5, 6, 7, 8, ]

# for x in nums:
#     print (x)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, ]

# for num in nums:
#     print(num, end=' ')

# lst = [[1], 2, '3', {4}, 's', 32,]

# print((lst+[lst]).index(lst))

# spisok1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# spisok2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# for obshiy in (spisok1 + spisok2):
#     print(obshiy, end=' ')


	

# a = [7, 6, 5, 1, 2, 3, 9, 8, 4]
# avg = (max(a) + min(a)) / 2
# items = [i + 1 for i, v in enumerate(a) if v > avg]
# print('Кол-во эл-тов', len(items))
# print('Номера', *items)

# lst = [1, 2, 3, 4, 5, 6, 7]
# avg = sum(lst) / len(lst)

# for num in lst:
#     if num > avg:
#         print(num)


# strings = ["apple", 'banana', 'pear', 'watermelon']
# longest = ''

# for string in strings:
#     if len(string) > len(longest):
#         longest = string

# print(longest)



# num = [1, 2, 3, 4, 5, 6, 7]
# max_index = 0
# for i in range(0, len(num)):
#     if num[i] > num[max_index]:
#         max_index = i

# print(max_index)

# s = 'hello'
# reversed_char = ''
# for char in s:
#     reversed_char = char + reversed_char

# print(reversed_char)


# n1 = [1, 2, 3, 4, 5]
# n2 = [3, 4, 5, 6, 7]

# result = []

# for num in n1:
#     if num in n2:
#         result.append(num)

# print(result)


# nu = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for elem in nu:
#     if elem not in unique:
#         unique.append(elem)

# print(unique)



# d = {"a": 1, "b": 2, "c": 3}
# total = 0
# for value in d.values():
#     total += value

# print(total)


# lst = [1, 2, 3, 4, 5]
# result = []

# for i in lst:
#     result.append(i ** 2)

# print(result)


# lst = ['a', 'b', 'c']
# result = ','.join(lst)
# print(result)\



# lst = [1, 2, 3, 1, 1, 4, 5]
# target = 1
# count = 0

# for num in lst:
#     if num == target:
#         count +=1

# print(count)

# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 4, "c": 5, "d": 6}
# common_keys = []

# for key in d1:
#     if key in d2:
#         common_keys.append(key)

# print(common_keys)

# l = [1, 2, 3, 4, 5, 6]
# target = 3
# result = []

# for num in l:
#     if num >= target:
#         result.append(num)

# print(result)
# Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.



# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get)[-3:]
# print(result)



