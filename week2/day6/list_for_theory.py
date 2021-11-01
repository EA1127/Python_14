""" 1- Пустые списки"""

# numbers1 = [] # создаем пустой список
# numbers2 = list() # создаем пустой список
# print(type(numbers1))
# print(type(numbers2))

# numbers4 = [1, 2, 3, 4]
# print(type(numbers4))
# numbers5 = list(numbers4)
# numbers6 = list(['makers', 'bootcamp', True, 56])
# print(type(numbers5))
# print(numbers5)
# print(numbers6)

# numbers1 = [7, 7, 7, 7, 7, 7]
# numbers2 = [7] * 6
# print(numbers1)
# print(numbers2)

""" 2- function - range() """
#1. range(end)
# numbers = list(range(10))
# print(numbers)
# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2. range(start, end)
# numbers = list(range(1, 10))
# print(numbers)
# => [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3. range(start, end, step)
# numbers = list(range(1, 10, 2))
# print(numbers)
# => [1, 3, 5, 7, 9]
# numbers = list(range(10, 0, -1))
# print(numbers)
# => [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] перевернутый список


""" 3- Сочетание цикла for и range()"""
# for i in range(1, 11):
#     print(i ** 2)
# => только вертикально запринтиться: 1 4 9 16 25 36 49 64 81 100

""" 4- Сравнение списков"""
# numbers1 = [1, 2, 3, 4, 5, 11]
# numbers2 = [1, 2, 3, 4, 5, 9, 100, 34, 1000]
# print(numbers1 > numbers2)
# => True (берется длина короткого списка и сравнивается с тем же элементами второго списка)

""" 5 """
# numbers1 = [1, True, 'Makers', 3.5, (1, 2), ['hello']]
# print(numbers1)
# => [1, True, 'Makers', 3.5, (1, 2), ['hello']]

""" 6 -Индексация """
# numbers = [1, True, 'Makers', 3.5, (1, 2), ['hello']]
# print(numbers[0]) # 1
# print(numbers[1]) # True
# print(numbers[2]) # 'Makers'
# print(numbers[3]) # 3.5
# print(numbers[-1]) # 'hello'
# print(numbers[-2]) # (1, 2)

# print(numbers[8]) # IndexError

"""7- Изменение списка """
# numbers = [1, True, 'Makers', 3.5, (1, 2), ['hello']]
# numbers[3] = 'Bootcamp'
# numbers[-1] = {1: 'a'} # словарь
# print(numbers)
# => [1, True, 'Makers', 'Bootcamp', (1, 2), {1: 'a'}]

"""8- Перебор элементов списка"""
# users = ['Alice', 'Sam', 'Carly']
# for user in users:
#     print(f'Hello {user}')
# => вертикально: Hello Alice   Hello Sam   Hello Carly

# for letter in 'Makers':
#     print(letter.upper())
# => вертикально: M A K E R S

"""9- МЕТОДЫ СПИСКОВ"""
"""9/1- append(element)"""
# users = ['Alice', 'Cat', 'Bily']
# user = 'Bob'
# users.append(user)
# print(users)  # => ['Alice', 'Cat', 'Bily', 'Bob']
# users.append('Emma')
# print(users) # => ['Alice', 'Cat', 'Bily', 'Bob', 'Emma']
# print(users[-1]) # => 'Emma'

# guests = []
# list_length = int(input('Enter number of guests: '))
# for i in range(list_length):
#     guest = input('Enter guest name: ')
#     print(guests)
#     guests.append(guest)
# print(guests)

# Enter number of guests: 3
# Enter guest name: emil
# []
# Enter guest name: kuba
# ['emil']
# Enter guest name: tala
# ['emil', 'kuba']
# ['emil', 'kuba', 'tala']

"""9/2- extend(list) """
# users1 = ['Alice', 'Sam']
# users2 = ['Bob', 'Tom']
# users1.extend(users2) # => ['Alice', 'Sam', 'Bob', 'Tom']
# users2.extend(['John', 'Aibek']) # => ['Bob', 'Tom', 'John', 'Aibek']
# print(users1)
# print(users2)
# print(users1 + users2) # => ['Alice', 'Sam', 'Bob', 'Tom', 'Bob', 'Tom', 'John', 'Aibek']

""" 9/3- insert(index, element) """
# users = ['John', 'Lenny', 'Andy', 'Ann']
# users.insert(1, 'Emma') # => ['John', 'Emma', 'Lenny', 'Andy', 'Ann']
# print(users)

""" 9/4- remove(element) - принимает только 1 аргумент, и удаляет только первое вхождение данного элемента """
# users = ['John', 'Ann', 'Andy', 'Ann']
# users.remove('Ann') # => ['John', 'Andy', 'Ann']
# print(users)
# if 'Sam' in users:
#     users.remove('Raychel') # => ['John', 'Andy', 'Ann']
# else:
#     print(users)

""" 9/5-  clear() """
# users = ['John', 'Billy', 'Andy', 'Ann']
# print(id(users))
# users.clear() # => []
# print(users)
# print(id(users))

# del users
# print(users)

""" 9/6.- index(element) """
# my_list = ['hello', 'makers', True, 6]
# print(my_list.index('makers'))

""" 9/7.- pop(index), default - pop(-1) по умолчанию удаляет последний элемент"""
# numbers = [1, 2, 3, 4, 5]
# num = numbers.pop(1) # => 2
# num2 = numbers.pop() # => 5
# print(numbers) # => [1, 3, 4]
# print(num)
# print(num2)

""" 9/8-  count(element) """
# numbers = [2, 4, 2, 2, 6, 7, 8, 2, 2]
# users = ['Ann', 'Sam', 'Jane', 'Ann', 'Ann']
# print(numbers.count(2)) # => 5
# print(users.count('Ann')) # => 3


""" 9/9.- sort(), sort(key=len)"""
# users = ['Alice', 'Tom', 'Cattie', 'Ann', 'Rain']
# users.sort() # => ['Alice', 'Ann', 'Cattie', 'Rain', 'Tom']
# print(users)
# users.sort(key=len) # => ['Ann', 'Tom', 'Rain', 'Alice', 'Cattie']
# print(users)

""" 9/10- reverse()"""
# users = ['Alice', 'Tom', 'Cattie', 'Ann', 'Rain']
# users.reverse() # => ['Rain', 'Ann', 'Cattie', 'Tom', 'Alice']
# print(users)

""" 9/11- copy()"""
# users1 = ['Tom', 'Bob', 'Anita']
# users2 = users1.copy() # => ['Tom', 'Bob', 'Anita']
# users2.append('Jean') # => ['Tom', 'Bob', 'Anita', 'Jean']
# print(users1)
# print(users2)
# print(id(users1)) # => 140052470918848
# print(id(users2)) # => 140052470018112


"""10- Functions of lists"""

"""len() - длина листа """
# numbers = [1, 2, 3, 4, 8, 0, 0, -3, -7]
# print(len(numbers)) # => 9

""" max(), min() """
# numbers = [4, 1, 6, 8, 9, 11, -7]
# print(max(numbers)) # => 11
# print(min(numbers)) # => -7

""" sum() """
# numbers = [4, 1, 6, 8, 9, 11, 7]
# print(sum(numbers)) # => 46

""" sorted() """
# numbers = [4, 1, 6, 8, 9, 11, 7]
# print(sorted(numbers)) # => [1, 4, 6, 7, 8, 9, 11]
# numbers2 = sorted(numbers)
# print(numbers) # => [4, 1, 6, 8, 9, 11, 7]
# print(numbers2) # => [1, 4, 6, 7, 8, 9, 11]


"""11- Срезы """

# my_list = [1, 2, 3, 4, 5, 7, 9, 11, 6]
# # list[x:y]
# print(my_list[1:4]) # => [2, 3, 4]
# my_list = my_list[1:4]
# print(my_list) # => [2, 3, 4]

# # # list[x:y:z] 
# print(my_list[2:-1:2])


""" 12- Вложенные списки"""

# users = [
#     ['Tom', 23],
#     ['Bob', 34],
#     ['Emi', 19]
# ]

# print(users[0])
# print(users[1])
# print(users[2])

# print(users[0][0][1])
# print(users[1][0])
# print(users[2][0])

# for list_ in users:
#     for element in list_:
#         print(element, end = ' | ')
#     print()

"""
Tom | 23 |
Bob | 34 |
Emi | 19 |
"""