""" Task 1 """

# def generate_password(param1, param2):
#     import random
#     random_list = random.sample(range(1, 10), k=7)
#     random_list = [str(i) for i in random_list]
#     password = param1 + param2 + ''.join(random_list)
#     # print(password)
#     return password

# def get_info(name = input('Enter your name: '),
#             last_name = input('Enter last name: ')):
#     password = generate_password(param1 = name, param2 = last_name)
#     return password

# print(get_info())


""" Task 2 """

# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def division(a, b):
#     return a / b

# def result(param):
#     return param

# def get_data(action):
#     num1 = int(input('Enter 1st number: '))
#     num2 = int(input('Enter 2nd number: '))

#     dictionary = {'+': add(num1, num2),
#                   '-': substract(num1, num2),
#                   '*': multiply(num1, num2),
#                   '/': division(num1, num2)}

#     some_result = dictionary[action]
#     return result(some_result)

# action = input('Select action from list below: + - * /' + '\n')
# print(get_data(action))


""" Task 3 """
# # с использованием kwargs
# def make_icecream(name, size, **kwargs):
#     print(f'Your {name} icecream {size} size')

#     if kwargs:
#         print(kwargs)
#         print('Your toppings: ')
#         for value in kwargs.values():
#             print('\t' + value)

# make_icecream(name='chocolate', size='medium', topping1='peanuts', topping2='coconut')

# # с использованием args
# def make_icecream(name, size, *args):
#     print(f'Your {name} icecream {size} size')

#     if args:
#         print(args)
#         print('Your toppings: ')
#         for value in args:
#             print('\t' + value)

# make_icecream('chocolate', 'medium', 'peanuts', 'coconut')
