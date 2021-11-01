""" --1-- """
# dict_ = {}
# dict_1 = dict()
# print(type(dict_))
# print(type(dict_1))

""" --2-- """
# my_dict = {"name": 'Sam', "last_name": 'White', "age": 23}
# print(my_dict)

""" --3-- """
# my_dict = dict(a1=1, b2=2, c3=3)
# print(my_dict)
# # или
# my_dict2 = {'a1': 1, 'b2': 2, 'c3': 3}
# print(my_dict2)

""" --4-- превращение списка/кортежа в словарь: """
# my_list = [['m', 1], ['a', 2], ['k', 3], ['e', 4], ['r', 4], ['s', 5]]
# my_list1 = (('m', 1), ('a', 2), ('k', 3))
# my_dict = dict(my_list)
# my_dict1 = dict(my_list1, a1=1, b2=2, c3=3)
# print(my_dict)
# print(my_dict1)

""" --5-- """
# dict_ = {1: "Makers", '2': True, False: []}
# print(dict_)
# dict_ = {[]: "Makers"} # ERROR ключ не может быть изменяемым типом данных

""" --6-- """
# dict_ = {1: "Makers", '2': True, False: []}
# print(dict_)
# OrderedDict

""" --7-- получение элемента по ключу """
# dict_ = {'Tom': 'black',
#         'Alice': 'yellow',
#         'Sam': 'green'}
# print(dict_['Alice']) # yellow
# print(dict_['Sam']) # green

""" --8-- изменение элемента """
# dict_ = {'Tom': 'black',
#         'Alice': 'yellow',
#         'Sam': 'green'}
# dict_['Alice'] = 'pink' # изменили значение элемента
# dict_['Rain'] = 'red' # расширили словарь еще на одну пару ключ:значение
# print(dict_)

""" --9-- методы словарей """
""" get(key, None) """
# my_dict = {1: 'Tom', 2: 'John', 3: 'Alice'}
# print(my_dict.get(1))
# print(my_dict.get(4, 'no such key in my dict'))
# print(my_dict[4])

""" clear() """
# my_dict = {1: 'Tom', 2: 'John', 3: 'Alice'}
# print(my_dict)
# my_dict.clear()
# print(my_dict) # из памяти словарь не удалется он просто очистился

""" copy() """
# my_dict = {1: 'Tom', 2: 'John', 3: 'Alice'}
# my_dict2 = my_dict.copy()
# my_dict[2] = 'Emma'
# print(my_dict)
# print(my_dict2)

""" pop(key, default) """
# dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
# deleted = dict_.pop('weight') # при этом возвращается значение удаленного ключа
# deleted1 = dict_.pop('age', 'NO SUCH KEY!!') # если нету ключа можно в дефоулт передать сообщение
# print(dict_)
# print(deleted)
# print(deleted1)

""" popitem() - рандомно удаляет пару ключ:значение """
# dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
# deleted_pair = dict_.popitem()
# print(dict_)
# print(deleted_pair)

""" setdefault(key, default) """
# dict_ = dict(a=1, b=2, c=3)
# print(dict_)
# # print(dict_.setdefault('a'))
# print(dict_.setdefault('d', 5))
# print(dict_)

""" update() """
# dict1 = {1: 'Tom', 2: 'Alice'}
# dict2 = {3: 'Bob', 4: 'Ann'} 
# dict1.update(dict2) # если хоть один ключ 2го словаря будет похож на ключ 1го, то значение этого ключа в 1м словаре перезаписыватеся
# print(dict1)
# print(dict2)

""" fromkeys(sequience , value), по дефолту value = None  """
# numbers = list('makers')
# new_dict = dict.fromkeys(numbers, 'Makers') # {'m': 'Makers', 'a': 'Makers', 'k': 'Makers', 'e': 'Makers', 'r': 'Makers', 's': 'Makers'}
# print(new_dict)


""" 10 Перебеор элементов словаря"""
"""items(),  keys(),  values()"""
# dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
# print(dict_.items())  # возвращается список внутри которого кортежи с парой ключ:значение словаря
# print(dict_.keys())  # возвращается список внутри которого ключи словаря
# print(dict_.values())  # возвращается список внутри которого значения словаря

# contacts = {
#         'Alice': '+996555666777',
#         'John': '+996777888999',
#         'Emma': '+996770111222'
# }

# for key, val in contacts.items():
#     print(f'Name: {key}, tel: {val}')

# for key in contacts.keys():
#     print(f'Name: {key}')

# for val in contacts.values():
#     print(f'tel: {val}')

# nested_dict = {
#     'Makers': {
#         'Aibek': 23,
#         'Adilet': 27,
#         'Aidai': 21,
#         'Nurbek': {
#             'age': 18,
#             'status': 'M',
#             'weight': 77
#         }
#     }
# }
# print(nested_dict['Makers']['Nurbek']['age'])



"""" создать словарь"""

# dict_ = dict(zip([1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']))
# print(dict_)