"""
*
JSON.

JSON, или JavaScript Object Notation - это формат для обмена данными.

Несмотря на то, что в названии присутствует слово JavaScript, 
JSON является абсолютно независимым от языка программирования.

Поэтому, с помощью данного формата можно обмениваться информацией с любым языком программирования, 
например передавать данные языка С на Java, либо с Perl на Python, с C# на JavaScript и.т.д.

JSON формат основан на двух структурах данных:

- Коллекция пар ключ/значение, в Python это словарь
- Упорядоченный список значений, в Python это список

Аналоги этих двух структур данных существуют почти во всех языках программирования, поэтому JSON может 
легко переводить данные сохраненные в этих структурах из одного языка в другой.

Допустим, у нас есть JSON файл - file.json, в которой хранится JSON строка, и нам нужно перевести данную 
строку в формат понятный Python.

Для этого существует два метода:

load(), десериализует файл, т.е принимает целый файл и переводит его из формата JSON в формат Python

loads(), десериализует строку, т.е принимает строку из файла и переводит ее из формата JSON в формат 
Python(для использования loads(), придется сперва прочитать строку методом read)

Для нашего примера подходит второй метод:

with open('file.json', 'r') as f: 
     result = json.loads(f.read()) 
     
Чтобы считать строку, в начале открыли файл file.json в режиме чтения r, файл обозначили переменной f.

Затем, считали содержимое файла f методом read() и передали в метод json.loads().

Результат сохранили в переменную result.


**

Процесс перевода Python объектов в формат JSON, называется сериализацией.

Для этого используют два метода:

dump(), записывает Python объекты в файл JSON, первым аргументом принимает название Python объекта, 
а вторым переменную обозначающую наш файл:
import json
      
obj = {'1': 'makers', '2': 'bootcamp'}      
with open("example.json", "w") as my_file:
   json.dump(obj, my_file)

Создали и открыли файл "example.json" для записи режимом w, обозначили наш файл переменной my_file.

Используя, метод dump(), мы сохранили словарь Python obj в нашем файле в перемнной my_file.

В результате, в нашей рабочей папке появится файл example.json, содержимое которого будет выглядеть 
данным образом:

{"1": "makers", "2": "bootcamp"} 

dumps(), сериализует Python объект в JSON строку, первым аргументом принимает название Python объекта, 
а вторым именованным аргументом количество отступов - indent:
import json 
     
obj = {'1': 'makers', '2': 'bootcamp'}        
json_obj = json.dumps(obj, indent=4)  
print(json_obj) 

используя метод dumps(), передали словарь Python и количество отступов 4, затем распечатали результат, 
в терминале получим:

{ 
 "1": "makers", 
 "2": "bootcamp" 
}
Заметьте, что в Python можно использовать одинарные кавычки, при переводе словаря в JSON формат,
 кавычки заменились на двойные.
 
"""


# 1-JSON
"""
JavaScript Object Notatin - это текстовый формат для хранения и обмена данными

JSON - осуществляет сериализацию и десериализацию данных

Сериализация - трансформация данных в серию байтов для хранения или передачи по сети.
Десериализация - это противоположный процесс декорирования данных

"""

# 2 - dump(), dumps()

# import json
# my_dict = {
#     "name": "Makers",
#     "format": "Bootcamp"
# }

# with open('Makers.json', 'w') as my_file:   # dump() -> сохранение данных в файл
#     json.dump(my_dict, my_file)

# json_string = json.dumps(my_dict)  # dumps() -> сериализация данных
# print(json_string)


# 3 - load() -> превращать кодированные данные json в объекты Python
# десериализация

# with open('Makers.json') as my_file:
#     python_obj = json.load(my_file)
#     print(python_obj)


# 4 - loads() -> принимает json строку и возвращает словарь
# десериализация

# string = '{"name": "Makers", "format": "Bootcamp"}'
# python_dict = json.loads(string)
# print(python_dict)


"""  ------------------------ ПРАКТИКА -------------------------- """

""" 1) JSON: dump(), dumps() сериализация"""

# import json

# info = {
#     "name": "Alice",
#     "age": 79,
#     "book": "Chamber of Secrets"
# }

# # with open('info.json', 'w') as my_file:    # сериализовали данные в словарь в фале info.json
# #     json.dump(info, my_file)

# json_object = json.dumps(info)   # cериализует Python объект в json объект и не создает файл
# print(json_object)
# print(type(json_object))   # это json объект -> строка:  <class 'str'>




""" 2) JSON: load(), loads() десериализация"""


# import json

# 1- load()

# with open('info.json') as my_file:
#     python_object = json.load(my_file)
#     print(python_object)
#     print(type(python_object))   # <class 'dict'>

# python_object['name'] = 'John'
# print(python_object)

# with open('info.json', 'w') as my_file:
#     json.dump(python_object, my_file)    # поменяли имя "Alice" на "John" в файле info.json


# 2- loads()

# json_str = '{"name": "Alice", "age": 79, "book": "Chamber of Secrets"}'
# python_object = json.loads(json_str)

# print(json_str)
# print(type(json_str))   # <class 'str'>

# print(python_object)
# print(type(python_object))  # <class 'dict'>

# python_object.update({'color': 'yellow'})
# print(python_object)



""" 3) ПРИМЕР  """

import json

with open('HarryPotterBooks.json') as my_file:
    dictionary = json.load(my_file)
    # print(dictionary)
    # print(type(dictionary))  # <class 'dict'>
    data = dictionary['books']
    # print(data)
    for book in data:
        book['author'] = 'J.K.Rowling'

    print(dictionary)

with open('HarryPotterBooks.json', 'w') as my_file:
    json.dump(dictionary, my_file)
