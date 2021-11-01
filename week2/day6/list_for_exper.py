""" 1-Списки списков """
# users = [ 
# ["Tom", 29], 
# ["Alice", 33], 
# ["Bob", 27] 
# ]
# print(users[0]) # ["Tom", 29] 
# print(users[0][0]) # Tom  
# print(users[0][1]) # 29 


# users = [ 
# ["Tom", 29], 
# ["Alice", 33], 
# ["Bob", 27] 
# ]

# user = list() 
# user.append("Bill") 
# user.append(41)
# print(user)

# users.append(user) 
# print(users[-1])
# print(users)

# users[-1].append("+79876543210")
# print(users[-1])
# print(users)

# users[-1].pop(0)
# print(users[-1])
# print(users)

# users[-1].pop(0)
# print(users[-1])
# print(users)

# users.pop(-1)

# users[0] = ["Sam", 18] 
# print(users)

# for user in users: 
#     for item in user: 
#         print(item, end =" | ")


""" 2- Генератор списков """
# # новичок
# numbers = [1,2,3,4,5]
# squares = []
# for number in numbers:
#     squares.append(number*number)
# print(squares)

# # map()
# numbers = [1,2,3,4,5]
# squares = list(map(lambda x: x*x, numbers))
# print(squares)

# # генератор списка
# numbers = [1,2,3,4,5]
# squares = [number*number for number in numbers]
# print(squares)

""" 3-Филтрация списков """
# # новичок
# numbers = [1,2,3,4,5] 
# numbers_under_4 = [] 
# for number in numbers: 
#     if number < 4: 
#         numbers_under_4.append(number)
# print(numbers_under_4)

# # функция filter()
# numbers = [1,2,3,4,5] 
# numbers_under_4 = list(filter(lambda x: x < 4, numbers))
# print(numbers_under_4)

# # генератор списка
# numbers = [1,2,3,4,5] 
# numbers_under_4 = [number for number in numbers if number < 4]
# print(numbers_under_4)

"""4-Одновременное использование map и filter """
# # новичок
# numbers = [1,2,3,4,5] 
# squares = [] 
# for number in numbers: 
#     if number < 4: 
#         squares.append(number*number) 
# print(squares)

""" функции  map() и filter() """
# numbers = [1,2,3,4,5]
# squares = list(map(lambda x: x*x, filter(lambda x: x < 4, numbers)))
# print(squares)


# генератор списка
# Синтаксис генератора списков: [element for variable(s) in list if condition]

# numbers = [1,2,3,4,5]
# squares = [number*number for number in numbers if number < 4]
# print(squares)


"""5- Выражения-генераторы"""
"""Отличие их от генераторов списков состоит в том, что они не загружают в память список целиком,
а создают generator object, и в каждый момент загружен только один элемент списка. Конечно, если
вы хотите использовать список для чего-нибудь, это не особо поможет. Но если вы просто передаете
его куда-нибудь, где нужен любой итерируемый объект (цикл for, например), стоит использовать функцию
генератора. Выражения-генераторы имеют такой же синтаксис, как генераторы списков, но вместо квадратных
скобок используются круглые:"""

# numbers = (1,2,3,4,5) # мы стремимся к эффективной работе, поэтому используем кортеж вместо списка
# squares_under_10 = (number*number for number in numbers if number*number < 10) # squares_under_10 - generator object 
# for square in squares_under_10:
#     print(square)

"""Выражения-генераторы достаточно заключить в одни круглые скобки. Например, в случае, если вы
вызываете функцию с одним аргументом, можно писать так: """
# some_function(item for item in list)



""" 6- Свёртка списка """
"""Под этим понятием подразумевается применение функции к первым двум элементам списка, 
а затем к получившемуся результату и следующему элементу, и так до конца списка.
Можно реализовать это через цикл for:"""

# numbers = [1,2,3,4,5] 
# result = 1
# for number in numbers: 
#     result *= number
# print(result)

"""A можно воспользоваться встроенной функцией reduce, принимающей в качестве 
аргументов функцию от двух параметров и список:"""

# from functools import reduce
# numbers = [1,2,3,4,5] 
# result = reduce(lambda a,b: a*b, numbers)
# print(result)


""" 7 - Прохождение по списку: range, xrange и enumerate - xrange не работает!!! """ 
"""встроенная функция  range() возвращает индексы списка указанной длины:"""
# strings = ['a', 'b', 'c', 'd', 'e']
# for index in xrange(len(strings)):
#     print(index)
# for index in range(len(strings)):
#     print(index)

"""встроенная функция  enumerate(), которая возвращает итератор для пар индекс - значение:"""
# strings = ['a', 'b', 'c', 'd', 'e']
# for index, item in enumerate(strings): 
#     print(index, item)
      # или
# for i in strings:
#     print(strings.index(i), i)

""" 8 - Проверка всех элементов списка на выполнение условия:"""

"""Функция any(): Допустим, нам надо проверить, выполняется ли условие хотя бы для одного элемента. 
Для этого исп-ся функция any(), которая прервется и вернет True, как только найдет элемент, удовлетворяющий условию.
Генератор вычисляет только необходимые в данный момент значения, а any принимает их по очереди:"""

# numbers = [1, 10, 100, 1000, 10000] 
# if any(number < 10 for number in numbers): 
#     print ('Success')

"""Функция all(): Аналогично, может возникнуть задача проверки, что все элементы удовлетворяют условию. 
Есть более простой путь — встроенная функция all. Легко догадаться, что она прекращает проверку после первого элемента, 
не удовлетворяющего условию. Эта функция работает абсолютно аналогично предыдущей:"""

# numbers = [1,2,3,4,5,6,7,8,9] 
# if all(number < 10 for number in numbers): 
#     print ('Success!')


""" 9 - Группировка элементов нескольких списков: """
""" zip(): Встроенная функция zip используется для сжимания нескольких списков в один. 
Она возвращает массив кортежей, причем n-й кортеж содержит n-е элементы всех массивов, 
переданных в качестве аргументов:"""

# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3]
# squares = [1, 4, 9]
# zipped_list = list(zip(letters, numbers, squares))
# print(zipped_list)
# # [('a', 1, 1), ('b', 2, 4), ('c', 3, 9)] 

"""Эта функция часто используется как итератор для цикла for."""