# --- task 1 ---
# a = {'x': 1, 'y': 2, 'z': 1}
# list_ = list(a.keys())
# print(list_[0])

# --- task 2 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.pop('a'))
# print(a)

# --- task 3 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# b = {'f': 55}
# a.update(b)
# print(a)

# --- task 4 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# --- task 5 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.keys())

# --- task 6 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# --- task 7 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# for key in a.keys():
#     print(key)

# --- task 8 ---
# a = {'a': 1, 'b': 2, 'c': 1}
# for val in a.values():
#     print(val)

# --- task 9 ---
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# c = {}
# for key, val in a.items():
#     if val % 2 == 0:
#         c.setdefault(key, 2)
# print(c)
# b.update(c)  
# print(b)

# --- task 10 --- !!!!!!!!!!!!!!???????????????????????
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for key, val in a.items():
#     if val != None:
#         b.setdefault(key, val)
# # print(b)
# a = b
# print(a)

# --- task 11 ---
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# b = {}
# for key, val in a.items():
#     val = val / 5
#     b.setdefault(key, val)
# a = b
# # print(b)
# print(a)


# --- task 12 ---
# 1-вариант (пропустило)
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# for key, val in (a.copy()).items():
#     if val % 2 == 0:
#         a.pop(key)
# print(a)

# 2-вариант (пропустило)
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# if a['apple'] % 2 == 0:
#     a.pop('apple')
# if a['orange'] % 2 == 0:
#     a.pop('orange')
# if a['banana'] % 2 == 0:
#     a.pop('banana')
# print(a)

# 3-вариант (без методов удаления - не прошло)
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = {}
# for key, val in a.items():
#     if val % 2 != 0:
#         b.setdefault(key, val)
# a = b
# print(a)

# 4-вариант (без методов удаления - не прошло)
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = dict()
# for key, val in a.items():
#     if val % 2 != 0:
#         b.update({key: val})
# a = b
# print(a)


# --- task 13 ---
# a = {'a': 1, 'b': 2, 'c': 3}
# b = dict()
# for key, val in a.items():
#     b.update({val: key})
#     # b.setdefault(val, key)
# print(b)


# --- task 14 ---
# a = {'a': 3, 'b': 2}
# list_values = a.values()
# # print(list_values)
# print(sum(list_values))


# --- task 15 ---
# a1 = dict({'d1': 7, 'd2': 9, 'd3': 11})
# a2 = {'d1': 7, 'd2': 9, 'd3': 11}
# a3 = dict(d1 = 7, d2 = 9, d3 = 11)
# print(a1)
# print(a2)
# print(a3)

# a1 = {}
# a2 = dict()
# a3 = dict.fromkeys(('4', '5'), 2)  # {'4': 2, '5': 2}
# print(a3)

# Extra task 1:
# вариант-1
# d = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for i in list(d.values()):
#     result = result * i
# print(result)

# вариант-2
# nums = {'a': 10, 'b': 9, 'c': 3}
# d = list(nums.values())
# result = (d[0]) * d[1] * d[2]
# print(result)


# Extra task 2 - пропустило:
# # вариант-1
# string = "pythonist"
# dict_ = {}
# for i in string:
#     amount = string.count(i)
#     dict_.update({i: amount})
# print(dict_)

# # вариант-2 - пропустило:
# string = "pythonist"
# lst_str = list(string)
# # print(lst_str)
# lst_num = []
# for i in string:
#     amount = string.count(i)
#     lst_num.append(amount)
# # print(lst_num)
# lst_zipped = list(zip(lst_str, lst_num))
# # print(lst_zipped)
# dict_ = dict(lst_zipped)
# print(dict_)

# Extra task 3
# school = {'a': 28, 'b': 33, 'c': 25, 'd': 27}
# school['a'] = 31
# school.update({'e': 22})
# school.pop('c')
# total = sum(school.values())

# print(school)
# print(total)
