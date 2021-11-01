# def hello_makers():
#     print('Hello, Makers!')

# hello_makers()
# print(type(hello_makers))


# 1 хранить функции в переменных

# makers = hello_makers
# makers()
# print(id(makers))
# print(id(hello_makers))


# 2 определить функции внутри другой функции

# def outer_func():
#     def inner_func():
#         print('Hello, Makers')
#     inner_func()

# outer_func()


# 3 Передавать функции в качестве аргумента и возвращать их из других функции

# def main_func(func):
#     print(f'Я получил функцию {func} в качестве аргумента')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers!')

# print(main_func(hello_makers))


"""
4 ДЕКОРАТОРЫ

Декораторы называют функциями высшего порядка, так как декораторы принимают в аргументы декорируемую функцию и 
возвращают функцию в качестве результата работы(в return).

Синтаксис декораторов выглядит данным образом:

def имя_декоратора(функция): 
  def функция_обертка(): 
       # код дополняющий функцию 
       # может быть вызов функции() 
       # здесь может быть код после вызова функции  
  return функция_обертка  
Наш декоратор принимает в аргументы функцию, зачем же тогда нам нужна еще одна внутренняя функция-обертка?

Суть декораторов состоит в том чтобы изменить поведение функции, не изменяя саму функцию, т.е декоратор 
принимает функцию, обрабатывает внутри и в конечном итоге должен возвратить обработанную функцию. Именно для 
возвращения измененной функции нам нужна функция-обертка.


Декораторы.
К функции можно применять неограниченное количество декораторов. В этом случае порядок применения декораторов 
будет иметь значение. Декоратор который находится ближе к функции будет выполняться первее.

К примеру:

@check_the_speed 
@check_is_true 
def my_func(): 
  return True 
в начале функцию обработает декоратор @check_is_true, который возвратит обработанную функцию my_func, затем к 
результату работы данного декоратора применится декоратор @check_the_speed.


Декораторы.
Внутри декоратора можно прописать дополнительный код как до вызова функции так и после. Помним, что внутри 
функции работает любой код написанный до ключевого слова return.
В такой конструкции:

import time 
def decorator(func): 
    def wrapper(): 
        print(time.time()) 
        func() 
        print('Закончил работу') 
    return wrapper  
в начале распечатается время print(time.time) - здесь используется еще один модуль для работы с временем time, 
который также нужно импортировать.

Затем, запускается функция func(), декоратор будет ждать окончания работы func(), и только когда в func() 
запустится весь код, сработает print('Закончил работу')


Другой, важной задачей внутренней функции-обертки является работа с аргументами декорируемой функции. К примеру, 
мы должны применить декоратор к такой функции:

@decorator 
def func(arg1, arg2): 
   return arg1 + arg2 
Мы знаем что сама функция func попадет в качестве аргумента в наш декоратор:

def decorator(func): 
   ... 
так как, внутри декоратора есть функция-обертка, аргументы arg1 и arg2 декорируемой функции не потеряются, а попадут 
в обертку, после чего мы сможем обработать как саму функцию, так и аргументы:

def decorator(func): 
   def wrapper(arg1, arg2):  
   #здесь аргументы могут называться как угодно x, y и.т.п 
       try: 
           func(arg1, arg2) 
       except Exception: 
           print('Аргументы должны быть одного типа') 
   return wrapper 

@decorator 
def func(a, b): 
   return a + b 

func('строка',2) 

можем добавить конструкцию try-except, которая попытается запустить функцию func(arg1,arg2), так как в Python можно 
сложить только числа с числами или склеить строки со строками, то в except словим исключение и добавим 
сообщение 'Аргументы должны быть одного типа'.


Все методы и свойства аргументов декорируемой функции доступны также внутри декоратора.
К примеру, если аргументами являются строки, то будут доступны все методы - isupper(), count(), type(), срезы по 
индексу str[3:5] и.т.д.
Рассмотрим данный пример, где нам нужно написать декоратор проверяющий является ли список - аргумент функции, пустым:

@decorator 
def func(list): 
  return list 

func([]) 
так как аргумент list попадает в нашу функцию-обертку, а у всех списков есть такое свойство как len(), возвращающий 
нам длину списка, можем проверить с помощью if...else является ли длина списка больше нуля:

def decorator(func): 
  def wrapper(args): 
      if len(args) > 0: 
            func(args) 
      else: 
            print('Список не должен быть пустым') 
  return wrapper

теперь, наш декоратор запустит функцию func только в том случае, если длина списка больше нуля, т.е список состоит 
из одного и более элементов.

Помимо обработки исключений и if...else, в декораторах можно реализовать list, dictionary и set comptehensions. 
Напишем декоратор который проверит аргументы функции и вернет только те, что имеют значение True:

def decorator(func): 
  def wrapper(arg): 
      return [x for x in arg if x != False] 
  return wrapper 

возвращаем ключевым словом return список сгенерированный выражением [x for x in arg if x != False]:

которое возвращает каждый элемент x для каждого элемента x в списке, попадающий в переменную arg внутренней 
функции обертки-wrapper, если x не равно False.

Проверим декоратор на данной функции:

@decorator 
def func(list): 
   return list

print(func([1, False, 0, -2, True])) 
получим результат:

[1, -2, True] 
так как 0 у нас приравнивается к значению False, он не включен в конечный список.


Помимо функции, декораторы могут принимать дополнительные аргументы. Для того чтобы использовать дополнительные аргументы, 
внутри декоратора нужно написать еще одну функцию-обертку.

К примеру, у нас будет декоратор который будет запускать декорируемую функцию, только в том случае если он получит строку 
'start' в качестве аргумента:

def decorator(dec_arg): 
   def wrapper(func): 
       def wrapper2(func_arg): 
             if dec_arg == 'start': 
                 func(func_arg) 
             else: 
                 print('функция не запущена') 
       return wrapper2 
  return wrapper 
здесь, сам декоратор ловит аргумент декоратора dec_arg, функция-обертка wrapper получает декорируемую функцию func, 
вторая обертка - wrapper2 ловит аргумент функции func - func_arg.

Проводим проверку, является ли аргумент декоратора dec_arg строкой 'start', если да запускаем функцию func(func_arg), 
если же нет, возвращаем сообщение print('функция не запущена').

Проверим декоратор на данной функции:

@decorator('start') 
def func(word): 
   print(word)

func('Hello!') 
получим в результате:

Hello! 
"""


# example-1 
# def func1():
#     print("I'm called inside other function")

# def func2(func):
#     print("I'll do somthing before func calling")
#     func()

# def func3():
#     print('Hello makers !!!')

# func2(func3)

# example-2
# def decorator(func):
#     print("Я - функция-декортаор")
#     def wrapper():
#         print("Я - функция-обертка")
#         print("Вызываем обернутую функцию")
#         func()
#         print("Выхожу из обертки")
#         return func
#     return wrapper

# @decorator
# def hello_makers():
#     print("Hello, Makers")
# print(hello_makers())

# @decorator
# def hello_bootcamp():
#     print("Hello, Bootcamp")
# hello_bootcamp()


# example-3
# def check_password(func):
#     def wrapper(parameter):
#         return func(parameter).strip()
#     return wrapper

# @check_password
# def get_info(param: str) -> str:
#     return param

# param = input("Enter your info: ")
# print(get_info(param))

# @check_password
# def get_email():
#     email = input("Enter email: ")
#     return email
# print(get_email())



""" 4 sandwich """
# def bread(func):
#     def wrapper(*args):
#         print("</-----\>")
#         func(*args)
#         print("</_____\>")
#     return wrapper

# def ingredients(func):
#     def wrapper(*args):
#         print('#tomato#')
#         func(*args)
#         print("--salad--")
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(*fillers):
#     for filler in fillers:
#         print(filler)

# get_sandwich('--ham--', "**sausages**", '&ketchup&', 'cheese', 'mayo')


# example-5

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'See what I got: {args}')
#         print(f'See what I got: {kwargs}')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func_without_params():
#     print("I'm a poor func without params")

# func_without_params()

# @decorator
# def func_with_params(name, last_name):
#     print("I'm a happy func with params")
#     print(f"Hello, {name} {last_name}")

# func_with_params('Sam', last_name='Garcia')


""" 6 """

# from requests.api import get

# def benchmark(iters: int) -> int:
#     def actual_decorator(func):
#         import time
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 func_call = func(*args, **kwargs)
#                 end = time.time()
#                 total = total + (end - start)

#             print(f'Average complete time: {total / iters}')
#             return func_call
#         return wrapper
#     return actual_decorator


# @benchmark(iters=10)
# def get_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     # return webpage.text

# print(get_webpage(url='http://yandex.ru'))


#KISS
#DRY
#SOLID