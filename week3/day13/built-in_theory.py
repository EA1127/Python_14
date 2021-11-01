# Task 1
# from math import sqrt
# lst_ = [4, True, 'makers', 36, 25, 64, 9, False, 81, 49, 100]
# new_lst = list(map(lambda x: round(sqrt(x)), filter(lambda y: type(y) == int, lst_)))
# print(new_lst)


# Task 2
# lst_ = [{"name": 'Alice', "point": 89},
#         {"name": 'John', "point": 59},
#         {"name": 'Sam', "point": 100},
#         {"name": 'Alice', "point": 45}]

# lst_2 = list(filter(lambda x: x["point"] < 60, lst_))
# names = list(map(lambda x: x['name'], lst_2))
# points = list(map(lambda x: x['point'], lst_2))
# zipped_list = list(zip(names, points))

# expelled_list = list(map(lambda x: f'You are to be expelled {x[0]}', zipped_list))
# print(zipped_list)
# print(expelled_list)


# Task 3
# import functools
# list_letters = ['m', 'a', 'k', 'e', 'r', 's', '-', 'b', 'o', 'o', 't', 'c', 'a', 'm', 'p']
# str_ = str(functools.reduce(lambda x, y: x + y, list_letters))
# print(str_)
