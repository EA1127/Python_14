"""Особенности работы со Строками"""
# string1 = "Makers45%*"
# string2 = 'Bootcamp'
# print(string1, string2)

"""Ковычки внутри ковычек"""
# string3 = "Makers's Bootcamp"
# print(string3)

# sentence = "John said: 'I can code'"
# print(sentence)

# sentence = 'I love Maker\'s Bootcamp'
# print(sentence)

"""Перенос строки"""
# string = "Dear friend,\n\nWelcome to Makers Bootcamp!\nEnjoy your time here with us!"
# print(string)

"""Присваивание значения к строке с переносом, вывод тоже с переносом"""
# string = """Dear friend, 
# Welcome to Makers Bootcamp! 
# Enjoy your time here with us!"""
# print(string)

"""Строки коменты"""
# """ 
# This are docs
# """

"""Присваивание значения к строке с переносом, вывод без переноса"""
# string = 'This is a very long string.\
#  The length of String in Python should not be more than 79 symbols.\
#  Remember this'
# print(string)

"""Перенос с табуляцией"""
# languages = 'Languages:\n\t'
# description = 'Python: backend language\n\t JavaScript: frontend language'
# print(languages, description)

# loop = 'for i in range(5):\n\tprint(i)'
# print(loop)

""" Вертикальная табуляция"""
# sentence = 'Helllo\vMakers\vBootcamp'
# print(sentence)

""" Сырые строки, (отключение механизмов экранирования: \n перенос, \t табуляция, \r перенос на начало) """
# url = r'https://kaktus/\news\topics/\read'
# print(url)

""" Конкатенация """
# string1 = 'Makers'
# string2 = 'Bootcamp'
# print(string1 + string2)
# print('I study at ' + string1 + ' ' + string2)

# num1 = '6'
# num2 = '7'
# result = num1 + num2
# print(result)

# string = "makers"
# print((string + ' ') * 4)

""" Функция len(string) """
# string = 'Makers Bootcamp'
# print(len(string))

# length = len('John   ')
# print(length)

# sentence = 'Strings are ordered'
# print(sentence[0])
# print(len(sentence))

""" работа со срезами строк """
string = 'Makers bootcamp'
# print(string[:3])
# part_string = string[:3]
# print(part_string)
# print(string[2:-2])
# print(string[:])

# print(string[::-1])  # pmactoob srekaM
# print(string[::-2])  # pato rkM
# print(string[::2])  # Mkr otap
# print(string[3:5:2])  # e
# print(string[2::3])  # ksocp

# word = 'dream'
# word = 'c' + word[1:]
# print(word)

""" МЕТОД==> find(string) возвращает -1 если не находит"""
# string = 'Makers Bootcamp Boot'
# print(string.find('Boot'))  # 7 (элемент по индексу слева)
# # rfind(string)
# print(string.rfind('Boot')) # 16 (элемент по индексу справа)

""" МЕТОД==> index(string) rindex(string) возвращает exception """
# string = 'Makers Bootcamp Boot Boot Boot camp'
# print(string.index('camp'))  # 11 (индекс 1ой буквы слева)
# print(string.rindex('camp'))  # 31 (индекс 1ой буквы справа)

""" МЕТОД==> replace(pattern, replace_pattern, quantity of replacing patterns(или ничего)) """
# string = 'makers bootcamp makecamp'
# print(string.replace('camp', 'ROCK', 1))  # makers bootROCK makecamp
# print(string)

""" МЕТОД==> split(symbol) --> list """
# string = 'Makers Boot*camp'
# print(string.split('*'))   # ['Makers Boot', 'camp']
# full_name = input('Enter name and lastname: ').split(',')  
# print(full_name) # ввод (ema, ava) -> ['ema', 'ava']
# name = full_name[0] 
# last_name = full_name[-1] 
# print(name) # ema
# print(last_name) # ava


""" МЕТОД==> isdigit(), isalpha(), isalnum(), islower(), isupper() """
""" МЕТОД==> isspace(), istitle() """
# string = '12345'
# print(string.isdigit())  # True

# string = 'qwerty'
# print(string.isalpha())  # True

# string = 'qwert11'
# print(string.isalnum())  # True

# string = 'Qwert11'
# print(string.islower())  # False

# string = 'QWERTY'
# print(string.isupper())  # True

# string = '\n   '
# print(string.isspace())  # True

# string = 'Makers Bootcamp'
# print(string.istitle())   # True


""" МЕТОД==> upper(), lower() """
# string = 'Makers'
# print(string.upper()) # MAKERS
# print(string.lower()) # makers
# print(string)  # Makers


""" МЕТОД==> startswith(),  endswith() """
# string = "#I love Makers"
# print(string.startswith('#'))  # True
# print(string.endswith('ers'))  # True

""" МЕТОД==> join(list) """
# list_ = ['m', 'a', 'k', 'e', 'r', 's']
# print('$'.join(list_))    # m$a$k$e$r$s

""" МЕТОД==> capitalize(), title() """
# string = "bootcamp makers"
# print(string.capitalize()) # Bootcamp makers
# print(string.title()) # Bootcamp Makers

""" МЕТОД==> count(pattern) """
# string = 'Makers Bootcamp'
# print(string.count('a'))   # 2
# print(string[:6].count('a'))  # 1


""" МЕТОД==> lstrip(), rstrip(), strip() """
# password = '  qwerty    '
# print(password.lstrip())  #qwerty___
# print(password.rstrip())  #__qwerty
# print(password.strip())   #qwerty 

""" МЕТОД==> partition(pattern) --> tuple """
# string = 'Hello lovely Makers Bootcamp'
# print(string.partition('Makers'))  # ('Hello lovely ', 'Makers', ' Bootcamp')
# print(string.partition('Mkers'))   # ('Hello lovely Makers Bootcamp', '', '')

""" МЕТОД==> swapcase() """
# string = "CamelCase"  
# print(string.swapcase())  # cAMELcASE

""" МЕТОД==> zfill(width) """
# string = 'makers'
# print(string.zfill(10))  # 0000makers

""" МЕТОД==> ljust(width, fillchar), rjust(width, fillchar) """
# string = 'makers'
# print(string.ljust(10, '$'))  # makers$$$$
# print(string.rjust(11, '*'))  # *****makers


""" Форматирование строк """
""" cпособ-1. % """
# name = input()
# last_name = input()
# age = int(input())
# some_variable = "Welcome, %s %s, age %d" % (name, last_name, age)
# print(some_variable)  # Welcome, emil avazov, age 27

""" способ-2. МЕТОД==> format()"""
# name = input()
# last_name = input()
# var_ = 'Hi {} {}!'.format(name, last_name)
# var_1 = 'Hi {0} {1}!'.format(name, last_name)
# print(var_) # Hi emil ava!
# print(var_1) # Hi emil ava!

""" способ-3. f'' """
# name = input()
# last_name = input()
# age = input()
# variable = f'Hello {name} {last_name}\nYour age is {age}'  
# variable2 = f'Hello {name} {last_name}\nYour age is {int(age)-2}'

# print(variable)
# # Hello emil avazov
# # Your age is 27

# print(variable2)
# # Hello emil avazov
# # Your age is 25





