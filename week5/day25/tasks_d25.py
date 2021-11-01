# task-1

a = '12342342345'
# print(len(a)) # 11

b = [1,['a',5,6],2,3,4,5]
# print(len(b)) # 6

c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# print(len(c)) # 3

list_ = [a, b, c]
# print(list_) 
for i in list_:
    print(len(i))

#----------------------------------------------------

# task-2

class Dog:

    def voice(self):
        voice = 'Гав'
        return voice
    
class Cat:

    def voice(self):
        voice = 'Мяу'
        return voice

rex = Dog()
barsik = Cat()

def to_pet(animal):
    print(animal.voice())
    return animal.voice()

to_pet(barsik)
to_pet(rex)

#----------------------------------------------------

# task-3

class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'

class Employee(Person):

    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status

    def get_info(self):
        return f'{super().get_info()}, я работаю в компании {self.work} на должности {self.status}'

class Student(Person):

    def __init__(self, name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course

    def get_info(self):
        return f'{super().get_info()}, я учусь в {self.university} на {self.course} курсе'
        
person = Person('Иван', 'Петров')
employee = Employee('Иван', 'Петров', 'Рога и копыта', 'директор')
student = Student('Иван', 'Петров', 'КГТУ', 3)

def get_human_info(human):
    print(human.get_info())
    return(human.get_info())

get_human_info(employee) 
get_human_info(student) 
get_human_info(person)


#----------------------------------------------------

# task-4

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    
    @abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length**2

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

triangle = Triangle(5, 5)
square = Square(5)
circle = Circle(10)

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area())


#----------------------------------------------------

# task-5 NOT PASSED!!!

class OS:
    version = 'A'
    
    def copy(self, text):
        self.text = text
        return f'скопирован текст "{text}"'
    
class Windows(OS):
    def __init__(self, version):
        self.version = version
        
    def copy(self, text):
        return f'{super().copy(text)} горячими клавищами CTRL + C'
    
class MacOS(OS):
    def __init__(self, version):
        self.version = version
    
    def copy(self, text):
        return f'{super().copy(text)} горячими клавищами COMMAND + C'
    
class Linux(OS):
    def __init__(self, version):
        self.version = version
        
    def copy(self, text):
        return f'{super().copy(text)} горячими клавищами CTRL + SHIFT + C'
        
win = Windows('360-21')
mac = MacOS('2019')
lin = Linux('Ubuntu-2020')

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))


#----------------------------------------------------

# task-6

class Language:

    def __init__(self, level, type):
        self.level = level
        self.type = type

class Python(Language):
    def __init__(self, level, type):
        super().__init__(level, type)

    def write_function(self, func_name, arg):
        self.func_name = func_name
        self.arg = arg
        return f'def {func_name}({arg}):'

    def create_variable(self, var_name, value):
        self.var_name = var_name
        self.value = value
        return f'{var_name} = {value}'

class JavaScript(Language):
    def __init__(self, level, type):
        super().__init__(level, type)

    def write_function(self, func_name, arg):
        self.func_name = func_name
        self.arg = arg
        return f'function {func_name}({arg}) {{     }};'

    def create_variable(self, var_name, value):
        self.var_name = var_name
        self.value = value
        return f'let {var_name} = {value};'
        
py = Python('1', 'str')
print(py.write_function('get_code', 'a'))
print(py.create_variable('name', 'John'))

js = JavaScript('1', 'str')
print(js.write_function('validate', 'form'))
print(js.create_variable('password', 'john@123'))

#----------------------------------------------------

# task-7

class Money:

    def __init__(self, country, symbol):
        self.country = country
        self.symbol = symbol

class Dollar(Money):
    rate = 84.80

    def __init__(self, country, symbol):
        super().__init__(country, symbol)

    def exchange(self, amount):
        self.amount = amount
        return f"{self.symbol} {amount} равен {amount*Dollar.rate} сомам"

class Euro(Money):
    rate = 98.40
    
    def __init__(self, country, symbol):
        super().__init__(country, symbol)

    def exchange(self, amount):
        self.amount = amount
        return f"{self.symbol} {amount} равен {amount*Euro.rate} сомам"

d = Dollar('USA', '$')
print(d.exchange(100))

e = Euro('EU', '€')
print(e.exchange(80))
#----------------------------------------------------

# task-8  NOT DONE!!

"""
Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. 
У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, 
Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, 
принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.

Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. 

Например, если возраст earth_age равен 20:

на Венере ваш возраст составляет 11842 дней
на Юпитере ваш возраст составляет 5326080 часов
на Меркурии ваш возраст составляет 82 лет

"""
