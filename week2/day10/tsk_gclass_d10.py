# Task 1

# try:
#     num1 = input('Enter anything: ')
#     num2 = input('Enter anything: ')
#     result = int(num1) + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)

# Task 2

# dict_ = {1: 'rain_1234', 2: 'emma1127', 3: 'alice777'}
# dict_ = {value: key for key, value in dict_.items()}
# print(dict_)

# try:
#     username = input('Enter useranme: ')
#     ID = dict_[username]
#     print(ID)
# except KeyError:
#     print('There is no such username in database')
# else:
#     print(f'Welcome, {username}!')
# finally:
#     print('Thank you!')

# Task 3

# try:
#     age = int(input('Enter your age: '))
#     if age <= 0:
#         raise Exception('Negative numbers or zero not acceptable!')
# except ValueError:
#     print('Enter integer, not string')
# else:
#     print(f'Your age: {age}')