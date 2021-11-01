# task 1
"""Создайте функцию add, которая будет принимать 2 числа, 
складывать их и возвращать результат сложения."""
# def add(x, y):
#     return x + y
# num1 = 2
# num2 = 3
# add(num1, num2)
# print(add(num1, num2))


# task 2
"""
Создайте функцию get_string_length() которая будет принимать строку. 
Функция должна возвращать длину этой строки.
"""
# def get_string_length(string_):
#     return len(string_)
# string_ = 'hello'
# get_string_length(string_)
# print(get_string_length(string_))


# task 3
"""
Создайте функцию: get_type() которая принимает два обязательных параметра. 
Задача этой функции выводить тип принятых аргументов.
"""
# def get_type(x, y):
#   print(type(x))
#   print(type(y))
# x = 5
# y = 's'
# # get_type(x, y)
# print(get_type(x, y))


# task 4
"""
Создайте функцию divide() которая должна принимать 
2 числа и возвращать результат их деления.
"""
# def divide(x, y):
#     return(x / y)
# x = 5
# y = 10
# divide(x, y)
# print(divide(x, y))


# task 5
"""
Создайте переменную dict_ в котором будет хранится словарь.
Затем создайте функцию def dictionary() которая принимает этот словарь. 
Пройдитесь по dict_ циклом и распечатайте все его ключи внутри функции.
"""
# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# def dictionary(dict_):
#     for key in dict_.keys():
#         print(key)

# dictionary(dict_)     


# task 6
"""
Создайте переменную num = 6. Затем создайте функцию check()
которая принимает переменную num в качестве аргумента check(num)
и возвращает "It is odd number", если это число нечетное и "It is even number" 
если переданное число четное. Пример:

print(check(num)) 
Вывод:
It is even number 
"""
# num = 6
# def check(num):
#     if num % 2 != 0:
#         result = 'It is odd number'
#     else:
#         result = 'It is even number'
#     return result
# print(check(num))


# task 7
"""
Создайте функцию: is_palindrome() которая будет принимать строку и проверить является ли она палиндромом.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. 
Например, число 101; слова "кок", "топот", "комок" и т.д.)
Функция должна возвращать True или False. Пробелы и регистр учитывать нужно.

Пример:
print(is_palindrome('довод')) 
Вывод
True 
"""
# word = 'bob'
# def is_palindrome(word):
#     if word.lower() == word[::-1].lower():
#         return True
#     else:
#         return False
# print(is_palindrome(word))


# task 8
"""
Создайте функцию max_num()
которая принимает от пользователя два числа. 
Она должна сравнить эти числа между собой и вернуть максимальное значение.

Пример:
print(max_num(10, 12)) 
Вывод:
12 
"""
# def max_num(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# a = 10
# b = 12
# print(max_num(a, b)) 


# task 9
"""
Создайте функцию: multiply_list()
которая принимает список чисел и возвращает их произведение.

Пример:
print(multiply_list([1, 2, 3, 4, 5, 6])) 
Вывод:
720 
"""
# list_ = [1, 2, 3, 4, 5, 6] 
# def multiply_list(list_):
#     count = 1
#     for i in list_:
#         count *= i
#     return(count)
# print(multiply_list(list_)) 


# task 10
"""
Создайте функцию sum_digits()
которая принимает целое число и возвращает сумму всех его цифр.

Пример:
print(sum_digits(105)) 
Вывод:
6 
"""
# num = 777
# def sum_digits(num):
#     lst_ = list(str(num))
#     lst_1 = []
#     for i in lst_:
#         i = int(i)
#         lst_1.append(i)
#     return sum(lst_1)

# print(sum_digits(num))
