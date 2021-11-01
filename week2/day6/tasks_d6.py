# #1
# name_of_friends = ['Alice', 'Bob', 'Danny', 'Sam', 'Jane']
# for name in name_of_friends:
#     print(name)

# #2
# labels = ['Bugatti', 'Lamborgini', 'Aston Martin', 'MClaren', 'Ferrari']
# for brand in labels:
#     print(f'I like brand {brand}')

# #3
name_of_list = ['makers_bootcamp']
# print(len(name_of_list[0]))
# new_list = []
a = []
len_1 = len(name_of_list[0]) // 2 + 1 # => 8
if len(name_of_list[0]) % 2 > 0:
    a.insert(1, name_of_list[0][0:len_1]) # => 'makers_b'
    a.insert(0, name_of_list[0][len_1:]) # => 'ootcamp'
else:
    a.insert(1, name_of_list[0][0:len_1-1]) # => 'makers_'
    a.insert(0, name_of_list[0][len_1-1:]) # => 'bootcamp'
# print(a)
new_list = list(a[0]) + list(a[1])
# for i in a[0]:
#     new_list.append(i)
# for i in a[1]:
#     new_list.append(i)
print(new_list) # => ['o', 'o', 't', 'c', 'a', 'm', 'p', 'm', 'a', 'k', 'e', 'r', 's', '_', 'b']

# # 4
# list_ = ['makers', 'bootcamp']
# # new_list = [list_[-1], list_[0]]
# new_list = list_[::-1]
# print(new_list)

# # 5
# suitcase = []
# suitcase.append('coat')
# suitcase.append('jeans')
# suitcase.append('t-shirt')
# suitcase.append('docs')
# suitcase.append('medicine')
# suitcase.pop()
# suitcase.insert(0, 'wisky')
# print(suitcase)


# # 6
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# nums_ = []
# for i in nums:
#     if i < 5:
#         nums_.append(i)
# print(nums_)

# # 7
# nums = input()
# list_ = nums.split(',')
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# # 8
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)

# # 9
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     elif i % 2 != 0:
#         new_list.append('нечетное')
# print(new_list)

# # 10 
# list_ = list(range(20))
# print(list_)

# # 11
# list_ = list(range(0, 101, 2))
# print(list_)

# 12
# list1 = [2, 4, 5, 6, 7, 8, 9]
# list2 = [5, 6, 7, 8, 2, 11, 22]
# list1.extend(list2)
# # print(list1)
# print(sum(list1))

# 13
# 1-когда числа в строчном формате - прошел
# nums = input()
# list_s = nums.split(',')
# list_ = []
# for i in list_s:
#     list_.append(i)
#     list_.sort()
# print(list_)

# 2-когда числа в строчном формате
# nums = input()
# list_ = nums.split(',')
# list_.sort()
# print(list_)

# 3-когда числа в integer
# nums = input()
# list_s = nums.split(',')
# list_ = []
# for i in list_s:
#     list_.append(int(i))
#     list_.sort()
# print(list_)

# 14
# # мой вариант - не прошел
# list_ = [3, 2, 1]
# for i in list_:
#     a = list_.count(i)
# print('yes' if a > 1 else 'ERROR')

# list_ = [3, 2, 1]
# print('yes' if len(list_) != len(set(list_)) else 'ERROR')

# list_ = [3, 2, 1]
# if len(list_) != len(set(list_)):
#     print('yes')
# else:
#     print('ERROR')

# # 15
# list_ = []
# for i in range(54, 9184):
#     list_.append(i) if i % 5 == 0 else None
# print(list_)