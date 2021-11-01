# --- task 1 ---
# list_ = [i for i in range(1, 101)] 
# print(list_)

# --- task 2 ---
# list_ = [n for n in range(1, 51) if n % 2 != 0]
# print(list_)

# --- task 3 ---
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [n for n in list_ if n % 2 == 0 and n > 0]
# print(int_list)

# --- task 4 ---
# list_ = [n**2 for n in range(1, 26)]
# print(list_)

# --- task 5 ---
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(n) for n in str_list]
# print(int_list)

# --- task 6 ---
# list_ = [x*x if x % 2 == 0 else x for x in range(1, 11)]
# print(list_)

# --- task 7 ---
# list_ = [True if x % 2 == 0 else False for x in range(1, 11)]
# print(list_)

# --- task 8 ---
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']
# new_list = ['shoter' if len(x) < 4 else 'longer' for x in list_name]
# print(new_list)

# --- task 9 ---
# dict_ = {num: num**2 for num in range(1, 11)}
# print(dict_)

# --- task 10 ---
# n = int(input())
# dict_ = {x: x**2 for x in range(1,501) if x % n == 0}
# print(dict_)

# --- task 11 ---
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key: list(range(1,val + 1)) for key,val in a.items()}
# print(dict_)

# --- task 12 ---
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {key : 'even' if val % 2 == 0 else 'odd' for key, val in dict_.items()}
# print(a)

# --- task 13 ---
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [num for num in string_.split(' ') if num.isdigit()]
# print(list_)

# --- task 14 !!!!!---
# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }
# a = {key: key1 for key,val in dict_.items() for key1,val1 in dict_[key].items() if val1 == max(dict_[key].values())}
# print(a)


# --- task 15 ---
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}

# dict_ = {key: val1 for key,val in my_dict.items() for key1,val1 in my_dict[key].items()}
# print(dict_)


# Extra task 1: - не принят (баг в платформе)
# import random
# list_ = [round(x/2) for x in range(1, random.randint(0, 11)) if x % 2 == 0]
# print(list_)


# Extra task 2: - решен / принят
# dict_ = {1: 'hello', 2: 'makers', 3: 'bootcamp', 4: 'courses'}
# new_dict = {key: len(val) if key % 2 == 0 else (len(val))**3 for key,val in dict_.items()}
# print(new_dict)



# Extra task 3:

""" Создайте 2 сета из 10 рандомных элементов(необходимо использовать random), 
затем объедините их, и если их длинна меньше 20, то вы должны вывести сообщение типа 
'В этом сете было 3 повторения, его длинна составляет 17', 3 это количество элементов, 
которые были не уникальны, необходимо использовать set comprehension, на этапе создания сетов"""

# import random

# set1 = {num for num in random.sample(range(1, 20),10)}
# # print(set1)
# set2 = {num for num in random.sample(range(1, 20),10)}
# # print(set2)
# # print(set1.intersection(set2))
# set1.update(set2)
# # print(set1)
# if len(set1) < 20:
#     print(f'В этом сете было {20 - len(set1)} повторений, его длинна составляет {len(set1)}')