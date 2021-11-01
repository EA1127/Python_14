""" 1. SET - МНОЖЕСТВА """

# empty_set = set()
# empty_dict = {}
# print(type(empty_set))
# print(type(empty_dict))

# a = {'makers', 5, 9, True, False}
# print(type(a))
# print(a)
# b = set('makers')
# print(b)
# c = set(range(1, 10, 2))
# print(c)

# my_set = {'hello', 1, False}  
""" во множество нельзя поместить список, словарь, и другое множество!!! """
""" Множества хранят только НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ, а сами множетсва относятся к ИЗМЕНЯЕМЫМ """
# print(my_set)

""" Сравнение множеств!"""

# set1 = {1, 5, 3, 9, 0}
# set2 = {9, 1, 5, 3 ,8}
# set3 = {1, 5, 1, 3, 3, 8 ,8, 9, 9}
# print(set1 == set2)
# print(set3 == set2)
# print(set3) # выйдет без дубликатов!!

# my_set = {True, 1, 1.0}
# print(my_set)


# set3 = {1, 5, 1, 3, 3, 8 ,8, 9, 9}
# print(len(set3)) # 5 (убирает дубликаты, остаются только уникальные)


# guests = {'Tom', 'Sam', 'John', 'Tom'}
# print(len(guests))  # 3

"""2. МЕТОДЫ МНОЖЕСТВА"""
""" 2.1 метод add(item)"""
# guests = {'Tom', 'Sam', 'John', 'Emily'}
# print(guests)
# guests.add('Rain')
# print(guests)
# guests.add('Tom')
# print(guests)

""" 2.2 метод update(item or set)"""
# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = {6, 7, 8}

# numbers1.update(numbers2)
# numbers1.update({"Tom", "Emma"})
# print(numbers1)
# print(numbers2)

""" 2.3 метод  remove(item), discard(item), pop()"""
# guests = {'cat', 'ben', 'alice', 'eddy'}
# guests.remove('alice')
# guests.remove('john') # при удалении несуществующего элемента выдаст ошибку
# print(guests)

# guests.discard('alice')
# guests.discard('john') # при удалении несуществующего элемента не выдает ошибку
# print(guests)

# guests.pop() # Каждый раз удаляется какой то один элемент рандомно
# print(guests)

""" 2.4 метод clear() """
# guests = {'Cat', 'Ben', 'Alice', 'Eddy'}
# print(id(guests))
# guests.clear()
# print(guests)
# print(id(guests)) # объект guests  все еще есть в памяти

""" 2.5. метод  copy() """
# guests = {'Cat', 'Ben', 'Alice', 'Eddy'}
# guests2 = guests.copy()
# guests.add('Rain')
# print(guests)
# print(guests2)

""" 2.6. метод  intersection() или & """
# music_students = {'Sam', 'Alice', 'Kate', 'Ben', 'John', 'Tom'}
# art_students = {'Rachel', 'Sam', 'John', 'Cathrine', 'Tom'}
# it_students = {'Sam', 'Tom'}
# print(music_students.intersection(art_students))
# # or
# print(music_students & art_students)
# print(music_students & art_students & it_students)

# print(music_students) # метод не изменяет множетсво
# print(art_students) # метод не изменяет множетсво

""" 2.7 метод union() или | - объединяет без дубликатов """
# music_students = {'Sam', 'Alice', 'Kate', 'Ben', 'John', 'Tom'}
# art_students = {'Rachel', 'Sam', 'John', 'Cathrine', 'Tom'}
# it_students = {'Sam', 'Tom', 'Emma'}

# print(music_students.union(art_students))
# # or
# print(music_students | art_students | it_students)

""" 2.8 метод difference() или -   - возвращает разные элементы первого множества """
# music_students = {'Sam', 'Alice', 'Kate', 'Ben', 'John', 'Tom'}
# art_students = {'Rachel', 'Sam', 'John', 'Cathrine', 'Tom'}
# print(music_students.difference(art_students))
# print(art_students.difference(music_students))
# or
# print(music_students - art_students)
# print(art_students - music_students)


""" 2.9 метод symmetric_difference() - возвращает непересекающиеся элементы множеств """
# music_students = {'Sam', 'Alice', 'Kate', 'Ben', 'John', 'Tom'}
# art_students = {'Rachel', 'Sam', 'John', 'Cathrine', 'Tom'}
# print(music_students.symmetric_difference(art_students))

""" 2.10 метод isdisjoint() - возвращает  True  если нет пересекающиеся элементы """
# numbers1 = {1, 2, 3, 4}
# numbers2 = {7, 5, 6}
# print(numbers1.isdisjoint(numbers2)) # True

""" 2.11 метод issuperset(), issubset() """
# a = {1, 2, 3, 4, 5}
# b = {3, 5}
# print(a.issuperset(b)) # True
# print(b.issuperset(a)) # False
# print(a.issubset(b)) # False
# print(b.issubset(a)) # True

""" 2.12 метод  intersection_update() изменяет множетсво оставив пересекающиеся элементы множеств """
# numbers1 = {1, 2, 3, 4}
# numbers2 = {2, 5, 1}
# numbers1.intersection_update(numbers2)
# print(numbers1)

""" 2.13 метод  differenc_update() изменяет множество возвращая разные элементы 1го множества """
# numbers1 = {1, 2, 3, 4, 5, 6}
# numbers2 = {5, 2, 7, 8}
# numbers1.difference_update(numbers2)
# print(numbers1)

""" 2.14 метод symmetric_difference_update() изменяет множество возвращая непересекающиеся элементы множеств"""
# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = {6, 9, 0, 2 ,4}
# numbers1.symmetric_difference_update(numbers2)
# print(numbers1)
# print(numbers2)


""" 3. Замореженные множества -  frozenset()"""

# my_frozenset = frozenset('makers')
# my_frozenset2 = frozenset('makerbootcamp')
# # my_frozenset.add('b') # ERROR
# print(type(my_frozenset))
# # print(dir(frozenset))
# print(my_frozenset.intersection(my_frozenset2))
# # my_frozenset.intersection_update(my_frozenset2) # ERROR
# print(my_frozenset)

""" 3. Кортежи и их методы -  tuple() - упорядоченный неизменяемый тип"""
# # (), tuple()
# my_tuple = ('Alice', 3, True, False, [1, 2])
# my_tuple1 = 'Alice', 3, True, False, [1, 2] #  можно и так
# my_tuple3 = ('makers',) # если кортеж содержит 1 элемент после него ставится запятая, если нет то это будет считаться string
# my_tuple4 = tuple('Makersboot')
# print(type(my_tuple))
# print(type(my_tuple1))
# print(my_tuple4)

# my_tuple = (1, 4, 2, 7, 5)
# print(my_tuple[1])
# print(my_tuple[-1])
# print(my_tuple[1:-1])
# print(my_tuple)

# print(dir(tuple))


""" method    count()"""
# my_tuple = (1, 4, 4, 7, 4, 2)
# print(my_tuple.count(4))

"""method    index()"""
# my_tuple = (1, True, 'makers', 9.5)
# print(my_tuple.index('makers'))

""" Функции кортежей"""
# len(), max(), min(), sum()
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


""" Изменяемость списка внутри кортежа"""
# my_tuple = (1, True, ['hello', 'makers'])
# my_tuple[-1][0] = 'bootcamp'
# print(my_tuple)

# a = ()
# b = ()
# print(a is b) # True (a и b ссылаются на один и тот же участок памяти (но со списками это не работает))

""" Перебор множетсв и кортежей"""
# my_tuple = ('Alice', 'Sam', 'Cat', 'John')
# for name in my_tuple:
#     print(f'Welcome, {name}')

# my_set = {1, 2, 3, 4, 5, 6}
# for num in my_set:
#     print(num ** 3)


""" Цикл while"""

"""while логическое выражение 
     тело
   блок кода"""
# users = {'Alice', 'John', 'Carly', 'Bob'}
# while users:
#     users.pop()
#     print(users)
# print('program is finished')

# while True:
#     print('This is loop')

""" break, continue"""

# while True:
#     word = input('Enter the word: ')
#     if word.lower() == "exit":
#         break
#     elif not word:
#         print('Type anything!')
#         continue
#     else:
#         print(word[::-1])
# print('thanx program is finished!')

# money = 1000
# while money > 0:
#     n = int(input('How much money did you spend: '))
#     if n > money:
#         print('you do not have enough money')
#         break
#     money -= n
#     print(f'you have {money} soms left')

# print('You dont have money')
