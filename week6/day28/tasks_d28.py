# task-1

# class Auto:
#     def ride(self): 
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 

#-------------------------------------------

# task-2

# class RadioMixin:
#     def play_music(self, title):
#         print(f"Песня называется {title}")

# class Auto(RadioMixin):
#     def ride(self): 
#         print('Riding on a ground')

# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# obj = Auto()
# obj = Boat()
# obj = Amphibian()

# obj.play_music('Hello')
# obj.play_music('Rolling in the deep')
# obj.play_music('Sky Fall')


#-------------------------------------------

# task-3

# class Clock:
#     def current_time(self):
#         from datetime import datetime
#         now_ = datetime.now().strftime("%H:%M:%S")
#         print(now_)
    

# class Alarm:
#     def on(self):
#         pass

#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включен')


# clock = AlarmClock()

# clock.current_time() 
# clock.alarm_on()


#-------------------------------------------

# task-4  NOT PASSED!!!

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend
#         self.count_code_time = Coder.count_code_time

#     def coding(self, time):
#         self.count_code_time += time

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#         self.count_code_time = Coder.count_code_time


#     def coding(self, time):
#         self.count_code_time += time

#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

# class FullStack(Backend, Frontend):
#     pass

# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'JavaScript')
# c = FullStack('Senior', 'Python and JS')

# a.coding(12)
# a.coding(12)
# b.coding(45)
# b.coding(45)
# c.coding(17)
# c.coding(17)

# print(a.get_info())
# print(b.get_info())
# print(c.get_info())

# print(FullStack.mro())


#-------------------------------------------

# task-5

# class Square:

#     def __init__(self, side):
#         self.side = side
    
#     def get_area(self):
#         return int(self.side**2)

# class Triangle:

#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return int(self.height*self.base/2)

# class Pyramid(Triangle, Square):
#     def get_volume(self):
#         return int(1/3*self.side**2*self.height)

# square = Square(5)
# triangle = Triangle(5, 3)
# pyramid = Pyramid(6, 9)

# print(square.get_area())
# print(triangle.get_area())
# print(pyramid.get_area())


#-------------------------------------------

# task-6  NOT DONE!!

# class CreateMixin:
#     def create(self,task,key):
#         ToDo.todos[key]=task
#         return print(ToDo.todos)
    
# class DeleteMixin:
#     def delete(self,key):
#         b = ToDo.todos.get(key)
#         ToDo.todos.pop(key)
#         return f'удалили {b} задачу'

# class UpdateMixin:
#     def update(self,key,value):
#         ToDo.todos[key] = value
#         return print(ToDo.todos) 

# class ReadMixin:
#     def read(self):
#         return print({k: v for k, v in sorted(ToDo.todos.items(), key = lambda item: item[1])})

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    
#     todos = {}
    
#     def init(self):
#         pass
    
#     def set_deadline(self,date):
#         from datetime import datetime
#         d2 = datetime.now()
#         d1 = datetime.strptime(d2, "%Y-%m-%d")
#         d3 = datetime.strptime(date, "%Y-%m-%d")
#         return abs((d3 - d1).days)
 
# obj = ToDo()
# print(obj.set_deadline('2021-12-31'))
# obj.create('Pomoi posudu suka',1)
# obj.create('Hello Pidor',5)
# obj.create('Pomoi sebya',3)
# print(obj.delete(3))
# obj.update(5, 'Privet')
# obj.read()

#------------------------------------------
# 1)
# from datetime import datetime, date
# d1 = datetime.strptime("01.02.2017", "%d.%m.%Y")
# d2 = datetime.strptime("01.03.2017", "%d.%m.%Y")
# print((d2 - d1).days)

# 2)
# import datetime
# deadline = datetime.date(2021, 10, 31)
# today = datetime.date.today()
# print(deadline)
# print(today)
# days_ = (deadline - today).days
# print(days_)
#-------------------------------------------

# task-7 NOT DONE!!!

"""
Напишите класс Game, с помощью которого можно создать объекты-игры, у объектов должны быть атрибуты:

- type - тип игры
- name - название игры,
- extensions соответсвующий пустому списку - [].

У класса должны быть методы:

1. get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:
Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. 
Где Minecraft - это название игры, берется из атрибута name объекта.

2. get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами, 
если же список extensions пуст, возвращайте сообщение:
"Нет подключенных расширений"

Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.

У миксина должно быть два метода:

1. add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:
"Добавлено новое расширение Multiverse-Core для игры Minecraft. "
где Multiverse-Core это строка - название расширения

2. remove_extension, удаляющий расширение по названию, и возращающий строку в формате:
"Multiverse-Core был отключен от Minecraft."

Если же такого расширения нет в списке должна возвращаться строка:

"Такого экстеншна нету в списке."

"""



