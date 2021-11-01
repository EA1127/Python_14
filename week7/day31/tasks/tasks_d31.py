"""
Задание 1

Вам даны два файла task1.json и task1.py.

В task1.json хранятся определенные данные, 
вам нужно прочитать данный файл, 
затем сохранить содержимое в переменной python_obj.

После, откройте файл task1.py и запишите туда 
содержимое переменной python_obj.

"""
# import json

# with open('task1.json', 'r') as f:
#     json_obj = f.read()
#     python_obj = json.loads(json_obj)
     
# with open('task1.py', 'w') as pythonfile:
#     pythonfile.write(str(python_obj))

# # print(python_obj)
# # print(type(python_obj))


"""
Задание 2

В task2.json хранятся данные в формате JSON.

Напишите программу Python которая будет считывать 
данные с файла и сохранять их в переменной json_obj.

Затем, преобразуйте это обьект в объект Python и 
запишите результат в переменную python_obj.
"""

# import json

# with open('task2.json', 'r') as f:
#     json_obj = f.read()
#     python_obj = json.loads(json_obj)

#     # print(python_obj)
#     # print(type(python_obj))



"""
Задание 3
Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.

Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.

Ввод должен быть:

python_obj = None  
#ваш остальной код 
print(json_obj)  
Вывод:

null 
"""

# import json

# python_obj = None
# json_obj = json.loads(python_obj)
# print(json_obj)


"""
Задание 4
В переменной json_obj сохраните JSON объект "null", затем преобразуйте данный JSON объект в объект Python и сохраните в переменной python_obj. После распечатайте содержимое переменной python_obj.

Ввод должен быть:

json_obj = "null"  
#ваш остальной код 
print(python_obj) 
а вывод:

None
"""

# import json

# json_obj = None
# python_obj = json.dumps(json_obj)
# print(python_obj)