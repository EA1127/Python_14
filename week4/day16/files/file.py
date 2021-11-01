# file1 = open('makers.txt', 'r')
# print(file1.read())


"""
r - read
r+ - read + write
w - write
w+ - read + write
a  - append (дозаписывает)
a+ - append + read

x - write (если файла нет, елсли файл есть генерируется исключение)

b - открытие файла в двоичном режиме (binary)
t - открытие файла в текстовом режиме (text)
rt -> r
rb -> rb

"""
# 1)
# file1 = open('makers.txt', 'r')
# data = file1.read()
# data = file1.read(10)
# print(data)
# print(type(data))

# 2)
# seek()

# print(file1.read(10))
# file1.seek(10)
# print(file1.read())
# file1.seek(15)
# print(file1.read())
# file1.seek(0)
# print(file1.read())

# 3)
# readline()

# file1 = open('makers.txt', 'r')
# print(file1.readline())
# print(file1.readline())
# for line in file1:
#     print(line)

# 4)
# readlines()

# list_ = file1.readlines()
# list_ = [line.replace('\n', '') for line in list_]
# print(list_)
# for line in list_:
#     print(line)

# 5)
# write(),
# file2 = open('bootcamp.txt', 'w')
# file2 = open('bootcamp.txt', 'a')
# print(file2.write('Makers' + '\n'))


# file2 = open('bootcamp.txt', 'w')
# file2.write("It's such a beatiful day today" + '\n')
# file2.write("Today is my DAY" + '\n')

# 6)
# writelines()
# file2 = open('bootcamp.txt', 'w')
# list_zens = ["Beautiful is better than ugly.",
#             "Explicit is better than implicit.",
#             "Simple is better than complex.",
#             "Readability counts."]
# list_zens = [zen + '\n' for zen in list_zens]
# print(list_zens)
# file2.writelines(list_zens)
# dict_ = {'name': 'Makers', 'hello': 'world'}
# file2.writelines(dict_)

#  7)
# режим a
# file3 = open('files.txt', 'a')
# list_zens = ["Beautiful is better than ugly.",
#             "Explicit is better than implicit.",
#             "Simple is better than complex.",
#             "Readability counts."]
# list_zens = [zen + '\n' for zen in list_zens]
# file3.write('Zens of python:' + '\n')
# for zen in list_zens:
#     file3.write(zen)


# 8) with
# file3 = open('files.txt', 'a')
# list_zens = ["Beautiful is better than ugly.",
#             "Explicit is better than implicit.",
#             "Simple is better than complex.",
#             "Readability counts."]
# list_zens = [zen + '\n' for zen in list_zens]
# file3.write('Zens of python:' + '\n')
# for zen in list_zens:
#     file3.write(zen)

# file3.close()
# print(file3.closed)

# with open('files.txt', 'r+') as my_file:
#     print(my_file.read())
#     my_file.write('Additional string')

# with open('files.txt', 'w+') as my_file:
#     print(my_file.read())
#     my_file.write('Additional string')

# my_file.write('Hello world')
# print(my_file.closed)


""" 9) МОДУЛИ """
# math, random, datetime

# import math (стандартная библиотека)

# pypi.org: (сторонние библиотеки)

# import math
# from math import *
# from math import pi as P

# import calendar
# from calendar import weekheader as week


# 9.1) создание модуля

import square
print(square.circle(5))

from square import circle, triangle, rectangle

circle_area = circle(8)
triangle_area = triangle(9, 6)
rectangle_area = rectangle(3, 4)

print(circle_area, triangle_area, rectangle_area)

