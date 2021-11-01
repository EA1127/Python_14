""" NOT 1) Дан список в котором хранится строка. Разрежьте его на две равные части 
(если длина строки нечетная, то длина первой части должна быть на один символ больше). 
Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой, 
результат запишите в новый список и выведите на экран. """

# name_of_list = ['makers_bootcamp']
# a = []
# len_1 = len(name_of_list[0]) // 2 + 1 # => 8
# if len(name_of_list[0]) % 2 > 0:
#     a.insert(1, name_of_list[0][0:len_1]) # => 'makers_b'
#     a.insert(0, name_of_list[0][len_1:]) # => 'ootcamp'
# else:
#     a.insert(1, name_of_list[0][0:len_1-1]) # => 'makers_'
#     a.insert(0, name_of_list[0][len_1-1:]) # => 'bootcamp'
# # print(a)
# new_list = list(a[0]) + list(a[1])
# print(new_list)


""" 2) """
# list_ = ['makers', 'bootcamp']
# list_1 = [list_[1], list_[0]]
# print(list_1)

""" 3) """
# set_1 = {1, 2, 3, 4, 5, 6, 7}
# set_2 = {6, 8, 9, 11, 4, 5}
# print(set_1.intersection(set_2))

""" 4) """
# Tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# Timur = {'OchakKebab0', 'FreshBox'}
# Aleksandr = {'FreshBox', 'KFC'}
# Elina = Tilek & Timur & Aleksandr
# print(Elina)

""" NOT 5) Создайте словарь где ключами будут фрукты, а значением их цены. 
Удалите те элементы, значение которых будет чётным."""

# fruits = {'apple': 55, 'orange': 100, 'peach': 65, 'banana': 40}
# for key,val in (fruits.copy()).items():
#     if val % 2 == 0:
#         fruits.pop(key)
# print(fruits)


""" 6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений."""
# fruits = {'apple': 55, 'orange': 100, 'peach': 65, 'banana': 40}
# print(sum(fruits.values()))

""" NOT 7) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты."""
dict_ = {num: num**2 for num in range(1, 11)}
print(dict_)

""" NOT 8) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. """
# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}

my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
dict_ = {key: val1 for key,val in my_dict.items()
for key1,val1 in my_dict[key].items()}
print(dict_)

""" 9) Дан словарь. Попытайтесь получить значение по ключу.
Обработайте ошибку, возникающую в том случае, если такого ключа нет."""

# try:
#     dict_ = {'apple': 55, 'orange': 100, 'peach': 65, 'banana': 40}
#     print(dict_['lemon'])
# except KeyError:
#     print('Такого ключа не существует')
# else:
#     print(dict_['lemon'])

""" NOT 10) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике.
Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"""

# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)
