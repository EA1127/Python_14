# 1) -----
# def get_makers():
#     string = 'Makers'
#     print(string)
#     return string
# get_makers()

# 2)-----
# def double():
#     number = int(input('enter number: '))
#     print(number * 2)
#     return number * 2
# double()

# 3)----
# def add(a, b):
#     result = a + b
#     print(result)
#     return result

# num1 = input()
# num2 = input()
# add(num1, num2)

"""
def name_of_function():
    some_code
    return variable

name_of_function()
"""
# 4)----
# def function():
#     print('The function is called')

# function()  # ничего не возвращает
# print(function())

# 5)----
# def function():
#     print('The function is called')
#     return 'Makers'

# function()  # возвращает 'Makers'
# print(function())

# 6)----
# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# substract()
# print(substract())

# ---- функции есть объекты первого класса (можно присваивать ее к переменным)
# variable = substract()
# print(variable)

# ---- функции можно передавать ее в структуры данных
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, substract()]
# print(list_)

# 7) ----- функции в другой функции
# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# def function():
#     print('Im calling substract function')
#     variable = substract()
#     return variable

# print(function())

# 8) ----- функция в качестве аргументов (другой функции)
# def multiply(a, b):
#      return a * b

# num1 = 70
# num2 = 10
# num3 = 2
# print(multiply(num1, num2))
# print(num1)
# print(num2)

# 9) ------
# def welcome(name, last_name):
#     return f'Welcome, {name} {last_name}'

# name = input()
# last_name = input()
# a = input()
# b = input()
# print(welcome(name, last_name))
# print(welcome(a, b))

# 10)
# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     print(list_vowels)
#     result = ''.join(list_vowels)
#     return result

# my_word = input('Enter the word: ')
# print(get_vowels(get_word(my_word)))


# 11) ------позиционные и именнованные аргументы
# def info(name="Sam", age=19):
#     return f'{name} is {age} years old.'

# print(info(age = 19, name = 'Sam'))
# print(info(age=23, name='Alice'))
# print(info('John', age=29))
# print(info(name='John', 29)) # Error


# 12) ---------
# def test_func(n1=2, n2=9):
#     return n1 + n2

# print(test_func(n1=5, n2=35))

# 13) ---------
# def create_profile(name, age, image='default.jpg'):
#     return name, age, image

# print(create_profile(name='Rain', age=30, image="flower.png"))


""" *args  **kwargs """
# 14) 

# def func(required, *args, **kwargs):
#     print(required)

#     if args:  # True
#         print(args) # создает множество позиционных элементов

#     if kwargs:
#         print(kwargs) # создает словарь с именнованными аргументами

# func('Makers', 'bootcamp', 'Python', name='Rain', age=33)

# 15)
# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)

# # many()
# many(1, 2, 3, 4, 5, name='bill', job='coder')