"""" 1-Генераторы списков"""
""" 1-Теория """
""" 1.1-обычный способ"""
# even_nums1 = []
# for i in range(50):
#     if i % 2 == 0:
#         even_nums1.append(i)
# print(even_nums1)

""" 1.2-генератор списка"""
# even_nums2 = [i for i in range(50) if i % 2 == 0]
# print(even_nums2)


"""" 2-Генераторы словарей"""
# my_dict = {1: 'a', 2: 'b', 3: 'c'}
# my_dict = {val:key for key,val in my_dict.items()}
# print(my_dict)

""" 2- Практика """
""" lists """
# # 1 for
# list_ = []
# for num in range(1, 21):
#     list_.append(num * 2)
# print(list_)

# # 2 list comprehension
# list_ = [num * 2 for num in range(1, 21)]
# print(list_)

# # 3
# list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
# invitation = ['You are invited ' + name for name in list_users]
# print(invitation)

# # 4
# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)

# # 5
# strings = ['1998', '2001y', '2008year', '2020']
# list_ = [year for year in strings if year.isdigit()]
# print(list_)

# # 6
# list_ = ['Rain', 'John', 'Alice', 'Sam']
# list_ = [len(name) for name in list_]
# print(list_)

# # 7
# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [num if num < 0 else num ** 2 for num in list_]
# print(list_)

# # 8
# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x ** 2 for x in list_ if x % 2 == 0]
# print(list_)

# # 9
# # через comprehaension
# names = ['raychel', 'john', 'peter', 'jessica', 'bill', 'steven', 'steven123', 'sandy45', 'james']
# filtered_names = [
#     x + 'MAKERS'
#     if len(x) >= 5
#     else x + 'makers'
#     for x in names
#     if x.isalpha()
#     ]
# print(filtered_names)

# # через цикл
# names = ['raychel', 'john', 'peter', 'jessica', 'bill', 'steven', 'steven123', 'sandy45', 'james']
# filtered_names = []
# for x in names:
#     if x.isalpha():
#         if len(x) >= 5:
#             result = x + "MAKERS"
#             filtered_names.append(result)
#         else:
#             result = x + "makers"
#             filtered_names.append(result)
# print(filtered_names)

# # 10
# john = {'name': 'John', 'age': 22}
# raychel = {'name': 'Raychel', 'age': 23}
# peter = {'name': 'Peter', 'age': 17}

# users = [john, raychel, peter]
# ages = [user.get('age', None) for user in users]

# bigger = 0
# smaller = 0
# count = 0

# for age in ages:
#     if age >= 18:
#         bigger += 1
#     else:
#         smaller += 1
#     count += 1

# bigger = bigger * (100/count)
# smaller = smaller * (100/count)

# print(f'Процент пользователей с возрастом больше 18: {round(bigger)} процента')
# print(f'Процент пользователей с возрастом меньше 18: {round(smaller)} процента')

# # 11

# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]
# ]

# uncompress = [n for row in matrix for n in row]
# uncompress = []
# for row in matrix:
#     for n in row:
#         uncompress.append(n)
# print(uncompress)

# # 12
# from datetime import datetime

# start = datetime.now()
# print(start)
# list_ = []
# for i in range(100000):
#     list_.append(i)

# list_ = [i for i in range(100000)]
# print(datetime.now() - start)

"""" 2-Генераторы словарей"""
# # 13
# dict_abc = {'a': 1, 'b': 2, 'c': 3}
# dict_123 = {key: value for key, value in dict_abc.items()}
# dict_123 = {value: key for key, value in dict_abc.items()}
# dict_123 = {key: value + 2 for key, value in dict_abc.items()}
# dict_123 = {key.upper(): value + 2 for key, value in dict_abc.items()}
# print(dict_123)

# dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -7}
# new_dict = {key.upper(): value ** 3 for key, value in dict_abc.items() if value > 0}
# print(new_dict)

# # 14
# a = {'fruits':
#     {'apple': 100, 'orange': 60},
#     'vegetables':
#     {'cucumber': 28, 'tomato': 63}
#     }
# b = {key: {inner_k: inner_v + 3 for inner_k, inner_v in value.items()} for key, value in a.items()}
# print(b)

"""" 3-Генераторы множеств"""
# # 15
# list_ = [-2, 4, -5, 3, 8, -2, 3, 7]
# set_ = {num * 2 for num in list_ if num > 0}
# print(set_)

# # 16
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# new = {value ** 2 for value in dict_.values()}
# new1 = {key.upper() for key in dict_.keys()}
# print(new)  # возвратится множество
# print(new1)  # возвратится множество