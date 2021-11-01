# task-1

# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#         return func
#     return wrapper
    
# @call_function   
# def first():
#     print('hello world')
#     return 'hello world'
# first()

#--------------------------------------------------------------------------------------------

# task-2

# from datetime import datetime

# def func_start_time(func):
#     def wrapper():
#         start = datetime.now()
#         print(f"Функция запущена {start.strftime('%d.%m.%Y %H:%M')}")
#         func()
#         return func
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()

#--------------------------------------------------------------------------------------------

# task-3

# def make_bold(func):
#     def wrapper():
#         print('<b>')
#         func()
#         print('</b>')
#     return(wrapper)

# def make_italic(func):
#     def wrapper():
#         print('<i>')
#         func()
#         print('</i>')
#     return(wrapper)

# def make_underline(func):
#     def wrapper():
#         print('<u>')
#         func()
#         print('</u>')
#     return(wrapper)

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     print('Hello world')
#     return 'Hello world'

# hello()

#--------------------------------------------------------------------------------------------

# task-4

# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         time_request = end - start
#         print(f'Время выполнения: {time_request} секунд')
#     return wrapper

# @benchmark 
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')

# fetch_webpage()

#--------------------------------------------------------------------------------------------

# task-5
# version 5-1

# users = {
#     'jean': 'white_pheonix',
#     'thanos': 'infinite_gems',
#     'scarlet': 'red_witch',
# }

# def validate_password(func):
#     def wrapper(**kwargs):
#         username = kwargs.get('username')
#         password = kwargs.get('password')
#         if username in users and password == users.get(username):
#             func(kwargs.get('username'), kwargs.get('password'))
#         elif not username in users:
#             print('Username is not defined')
#         elif not password == users.get(username):
#             print('Password is invalid')
#     return(wrapper)

# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')

# login(username='scarlet', password='red_witch')

#--------------------------------------------------------------------------------------------

# task-5
# version 5-2

# users = {
#     'jean': 'white_pheonix',
#     'thanos': 'infinite_gems',
#     'scarlet': 'red_witch',
# }

# def validate_password(func):
#     def wrapper(username, password):
#         if username in users and password == users.get(username):
#             func(username, password)
#         elif not username in users:
#             print('Username is not defined')
#         elif not password == users.get(username):
#             print('Password is invalid')
#     return(wrapper)

# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')

# login('scarlet', 'red_witch')

#--------------------------------------------------------------------------------------------

# task-6

# def is_admin(func):
#     def wrapper(dict):
#         func(dict)
#         if dict.get('is_admin') == True:
#             print(f"Доступ разрешен {dict.get('username')}")
#         else:
#             print(f"Доступ запрещен {dict.get('username')}")
#     return wrapper

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})

#--------------------------------------------------------------------------------------------

# task-7

# url = 'https://www.mywebsite.com/'

# def route(func):
#     def wrapper(path):
#         path = url + path
#         print(func(path))
#         # print(path)
#     return wrapper

# @route
# def get_page(path):
#     return path
 
# get_page('about/')
# get_page('products/')

#--------------------------------------------------------------------------------------------

# task-8

# name_format = [('Leo', 'Nimoy', 40, 'M'),
#             ('Carrie', 'Fisher', 35, 'F'),
#             ('Harrison', 'Ford', 38, 'M')]

# def sort_names(func):
#     def wrapper(person):
#         person = sorted([(x[2], x[0], x[1], x[-1]) for x in person])
#         print(person)
#         print(func(person))
#     return wrapper

# @sort_names
# def prefix_name(person):
#     person = [f"Mr. {x[1]} {x[2]}" if x[-1] == 'M' else f"Ms. {x[1]} {x[2]}" for x in person]
#     return person

# prefix_name(name_format)

#--------------------------------------------------------------------------------------------

# task-9

# tp_list = ['0777987456', '0555123456', '0770369852']

# def get_full_number(func):
#     def wrapper(list_):
#         list_ = [f"+996 {''.join(list(x)[1:4])} {''.join(list(x)[4:])}" for x in list_]
#         # print(list_)
#         print(func(list_))
#     return wrapper

# @get_full_number
# def sort_phone_nums(list_):
#     # list_.sort()
#     # list_str = '#'.join(list_)
#     list_ = '#'.join(sorted(list_))
#     # print(list_)
#     return list_
 
# sort_phone_nums(tp_list)

#--------------------------------------------------------------------------------------------

# task-10

# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper_inner(num):
#             if correct_type == type(num): 
#                 func(num) 
#             else:
#                 print('Неверный тип данных :(') 
#         return wrapper_inner
#     return wrapper
 
# @type_check(int)
# def func1(num):
#     print(num*2)
 
# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})