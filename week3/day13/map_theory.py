""" map(), filter(), reduce(), zip(), lambda() """

# 1) map(function, iterable object)

# numbers_str = ['1', '2', '3', '4', '5']
# numbers_int = list(map(int, numbers_str))
# print(numbers_int)


# 2) lambda параметр: функция с параметром

# numbers = [1, 2, 3, 4, 5]
# double_numbers = list(map(lambda x: x * 2, numbers))
# print(double_numbers)


# 3) filter(function, iterable object)

# strings = ['Makers', 'MAKERS', 'BOOTCAMP', 'bootcamp']
# upper_strings = list(filter(lambda word: word.isupper(), strings))
# print(upper_strings)


"""
print()
input()
int()
str()
bool()
list()
dict()
set()
tuple()
frozenset()
len()
sum()
min()
max()
sorted()
"""

""" 1) map(func, iterable object) """

# 1.1) через цикл
# list_str = ['1', '2', '3', '4', '5']
# list_int = []
# for i in list_str:
#     list_int.append(int(i))
# print(list_int)

# 1.2) через map
# numbers_str = ['1', '2', '3', '4', '5']
# numbers_int = list(map(int, numbers_str))
# print(numbers_int)

# 1.3) Аннотация типов
# def capital(word: str) -> str:
#     return word.title()
# list_names = ['john', 'alice', 'sam', 'rain']
# new_list = list(map(capital, list_names))
# print(new_list)

# 1.4)
# def dollars_to_soms(dollars: int) -> int:
#     return f'{round(dollars * 84,8)} soms'
# dollars = [100, 50, 25, 90, 65]
# soms = list(map(dollars_to_soms, dollars))
# print(soms)

""" 2) lambda параметр: функция с параметром - анонимная функция """
# 2.1)
# print((lambda x: x ** 2)(11))

# 2.2)
# square = lambda x: x ** 2
# print(square(11))

# 2.3)
# print((lambda x, y, z: x + y + z)(1, 2, 3))


"""3) lambda сочетание с map"""
# 3.1)
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = [7, 8, 9]
# new_list = list(map(lambda x, y, z: x + y + z, list_1, list_2, list_3))
# print(new_list)

# 3.2)
# *
# num_list = [2, 6, 8, 7, 9, 1, 4]
# num_list2 = []
# for i in num_list:
#     num_list2.append(i * 2)
# print(num_list2)

# **
# num_list2 = [i * 2 for i in num_list]
# print(num_list2)

# ***
# num_list2 = list(map(lambda i: i * 2, num_list))
# print(num_list2)


""" 4) filter """
# 4.1)
# names = ['john', 'alice', 'amber', 'rain', 'sam', 'alan']
# filtred_names = list(filter(lambda name: name.startswith('a'), names))
# print(filtred_names)

# 4.2)
# numbers = [4, 5, 6, 2, 8, 11, 9, 12, 15, 17, 18]
# filtered_numbers = list(filter(lambda number: number % 3 == 0, numbers))
# print(filtered_numbers)

# 4.3)
# dict1 = [{'subject': 'python', 'point': 89},
#          {'subject': 'javascript', 'point': 92},
#          {'subject': 'python', 'makers': 100}]
# dict_new = list(filter(lambda x: x['subject'] == 'python', dict1))
# print(dict_new)

# 4.4)
# users = [{'username': 'Alice123', 'comments': ['I love it, Good!']},
#          {'username': 'Sam45', 'comments': []},
#          {'username': 'John', 'comments': []},
#          {'username': 'Rain', 'comments': ['I like it!!!',]}]

# active_users = list(filter(lambda x: x.get('comments', None), users))
# inactive_users = list(filter(lambda x: not x.get('comments', None), users))
# print(f'These users are active: {active_users}')
# print(f'These users are inactive: {inactive_users}')

# 4.5)
names = ['Alice', 'Sandra', 'Molly', 'Tim']
greetings = list(map(lambda name: f'Welcome, {name}', filter(lambda x: len(x) >= 5, names)))
print(greetings)


""" 5) reduce(func, iterable object) """

# 5.1)
# import functools

# numbers = [1, 2, 3, 4]
# sum_ = functools.reduce(lambda x,y: x + y, numbers)
# print(sum_)


# 5.2)
# numbers = [78, 56, 2, -9, 0, 3555, 6789, 2, 356]
# max_ = functools.reduce(lambda a, b: a if a > b else b, numbers)
# print(max_)

# 5.3)
# from functools import reduce

# numbers = [5, 6, 8, 1, 2]
# multiply = reduce(lambda x, y: x * y, numbers)
# print(multiply)


""" 6) zip() """
# 6.1)
# list_a = [1, 2, 3, 4, 5]
# list_b = ['a', 'b', 'c', 'd', 'e']
# list_c = ['makers', 'bootcamp', 'hello', 'world', 'zip']
# zipped_list = list(zip(list_a, list_b, list_c))
# zipped_tuple = tuple(zip(list_a, list_b, list_c))
# print(zipped_list)

# unzipped = list(zip(*zipped_list))
# print(unzipped)

# list_num, list_let, list_str = list(zip(*zipped_list))
# print(list_num)
# print(list_let)
# print(list_str)

# 6.2)
# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']
# zipped_dict = dict(zip(list_1, list_2))
# print(zipped_dict)


""" 7) enumerate() """
# print(dir(__builtins__))

# 7.1)
# seasons = ['spring', 'winter', 'autumn', 'summer']
# enumerated_seasons = list(enumerate(seasons))  # set, tuple, dict
# print(enumerated_seasons)

# enumerated_seasons_1 = list(enumerate(seasons, start=5))
# print(enumerated_seasons_1)

""" 8) abs, all, any, ascii, ord, chr, divmod """
# # abs
# negative = -123
# absolute = abs(negative)
# print(absolute)

# # all
# list_of_zero = [1, 0, 0, 0]
# is_true = all(list_of_zero) 
# print(is_true) # False

# # any
# list_of_zero = [1, 0, 0, 0]
# is_true_any = any(list_of_zero) 
# print(is_true_any) # True


# ascii
# list_1 = ['makers', 'мэйкерс', 23, 0, '$*']
# list_2 = ascii(list_1)
# print(list_2)

# ord
# print(ord('b')) # 98
# print(chr(98)) # b

# divmod
# a = 15
# b = 7
# print(divmod(a, b))
