# Task 1

# list_len = int(input('Enter list length: '))
# list_ = []
# for i in range(list_len):
#     element = input('Enter element: ')
#     print(element)
#     list_.append(element)
# print(list_)


# Task 2

# data = [
#     ['uluk777', 'qwerty'],
#     ['timurrr', '123445'],
#     ['aliya', 'helloworld'],
# ]
# users = []
# for user in data:
#     username = user[0]
#     users.append(username)
# print(users)
# a = 3
# while a > 0:
#     chel = input('Enter username: ')
#     if chel in users:
#         print('This user already exists')
#     else:
#         password = input('Set your password: ')
#         data.append([chel, password])
#     a -= 1
#     print(data)


# from collections import deque
# list_ = deque(['apple', 'orange', 'peach'])
# list_.appendleft('cherry')
# print(list_) # => deque(['cherry', 'apple', 'orange', 'peach'])
# list_.popleft()
# print(list_) # => deque(['apple', 'orange', 'peach'])