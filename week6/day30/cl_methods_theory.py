"""
Методы класса, экземпляра и статические методы.

* 
При работе с классами в Python, различают три вида методов:

методы экземпляра - все те методы которые мы создавали для работы с объектом от класса.
Методы экземпляра класса принимают объект класса как первый аргумент, то что мы обычно 
называем self.

К примеру, у нас есть класс для домашних растений Plant:

class Plant: 
     oxygen = 900 

     def __init__(self, height): 
         self.height = height 

     def grow(self, cm): 
         self.height += cm 
         self.oxygen += 35 
         return self.height 
у объектов Plant есть метод grow, принимающий ссылку на объект self, и cm - на сколько 
сантиметров выросло растение.

Каждый раз как растение растет, высота растения height увеличевается, также увеличивается 
количество кислорода выделяемое растением - oxygen(переменная класса).

Создадим объект и применим метод:

kaktus = Plant(10) 
print(kaktus.grow(2)) 
print(kaktus.oxygen) 
получим в терминале:

12 
935 
Как мы видим, методы экземпляра класса могут менять состояние и отдельного объекта и самого 
класса.

методы класса - принимают в параметры ссылку на сам класс, обычно обозначают переменной cls, 
и декорируются декоратором @classmethod.

Например, у нашего класса есть переменная класса season, можем написать метод класса, который 
будет менять season на новое значение:

class Plant: 
     season = 'зима' 

     @classmethod 
     def change_season(cls, value): 
         cls.season = value 

Plant.change_season('весна') 
kaktus = Plant() 
ficus = Plant() 
print(kaktus.season, ficus.season) 
получим в терминале:

весна весна 

Методы класса меняют состояние всего класса, и это отражается на всех объектах созданных от
 класса. Однако методы класса не могут менять состояние конкретного, одного объекта.

статические методы - создаются при помощи декоратора @staticmethod, данные методы не принимают
 ни объект, ни класс.
Такие методы полезны для создания вспомогательных функций(простое преобразование из одного 
типа в другой, расчеты и.т.д).

Например:

class Plant:

     @staticmethod 
     def is_blooming(season): 
         if season == 'весна': 
                 print('Да') 
         else:  
                 print('Нет') 
                 
мы создали статический метод проверяющий цветут ли наши растения сейчас(допустим что они 
цветут только весной), можем вызвать метод через класс и передать сезон:

Plant.is_blooming('осень') 
получим:

Нет 

Статические методы не имеют доступа к атрибутам экземпляра класса и к атрибутам 
самого класса.

**
Методы класса можно использовать также для создания новых объектов от класса.

К примеру, у нас есть класс Contact, экземпляры которого имеют атрибуты name и phone:

class Contact:

     def __init__(self, name, phone): 
         self.name = name 
         self.phone = phone 

Представим что мы получаем данные от пользователя в виде списка [имя, телефон], 
и нам нужно создавать объекты от подобных списков.

Для этого, можем создать свой конструктор объектов через метод класса:

class Contact: 
 . . . 
     @classmethod 
     def from_list(cls, lst): 
         name = lst[0] 
         phone = lst[1] 
         return cls(name, phone) 
декорируем метод from_list декоратором @classmethod, метод будет принимать в аргументы 
сам класс и список(lst).

Внутри метода в переменную name и phone запишем элементы списка по индексам - 0 и 1.

В конце передадим в класс(cls), наши значения из списка в переменных name и phone.

Применим метод from_list к классу и передадим список:

contact = Contact.from_list(['John', '0550550550']) 
print(contact) 
распечатав переменную где хранится объект, получим:

<__main__.Contact object at 0x7fd87b82cfd0> 
т.е в переменной contact хранится объект принадлежащий к классу Contact.

"""

"""
instance method -> self
class method - @classmethod -> cls
static method - @staticmethod
"""

# Task-1

class Makers:
    language_choices = 'Python', 'JavaScript'

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"Hello, {self.name}"

    @classmethod
    def class_method(cls):
        return f"Welcome to Makers! What type of language do you choose?: {cls.language_choices}"

    @staticmethod
    def static_method(choice):
        return f"Great! You chose {choice} coures"

student1 = Makers(name='Alex')
print(student1.instance_method())
print(student1.class_method())
print(student1.static_method(choice='Python'))
print()
student1 = Makers(name='Eric')
print(student1.instance_method())
print(student1.class_method())
print(student1.static_method(choice='JavaScript'))

#---------------------------------------------------------

# Task-2

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"{self.name}, {self.email}"

    @classmethod
    def add_data(cls, user_info:list):
        name, email = user_info
        return cls(name, email)

list_of_users = [
    ['Emily', 'emily@gmail.com'],
    ['Betty', 'bett@yahoo.com'],
    ['Clare', 'clare@gmail.com']
]

for info in list_of_users:
    user = User.add_data(info)
    print(user.get_info())


#---------------------------------------------------------

# Task-3

class Lottery:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def _generate_number():
        import random
        number = random.sample(list('123456789'), k=5)
        number = ''.join(number)
        return number

    def get_number(self):
        number = self._generate_number()
        self.number = number
        return f"Dear {self.name}! Your lucky number is {self.number}"

participant1 = Lottery(name='Alex')
print(participant1.get_number())
print(participant1.number)

participant2 = Lottery(name='Bill')
print(participant2.get_number())
print(participant2.number)
#---------------------------------------------------------

# Task-4 - 1

class Pizza:

    def __init__(self, ingredients:list):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza with {self.ingredients}"

pizza1 = Pizza(['tomatoes', 'mozarella', 'basil'])
pizza2 = Pizza(['meat', 'chilli pepper', 'cheese'])
print(pizza1)
print(pizza2)
# ---------------------------------------

# Task-4 - 2

class Pizza:

    def __init__(self, ingredients:list):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza with {self.ingredients}"

    @staticmethod
    def circle_area(radius):
        import math
        area = round(math.pi*radius**2, 2)
        return f"Pizza's size is {area} cm2"

    def area(self, radius):
        self.radius = radius
        # print(self)
        return self.circle_area(self.radius)

    @classmethod
    def margarita(cls):
        return cls(['mozarella', 'tomatoes', 'basil'])

    @classmethod
    def pepperoni(cls):
        return cls(['pepperoni', 'cheese'])

    @classmethod
    def chilli(cls):
        return cls(['chilli peppers', 'cheese', 'meat', 'souce'])

# SOLID, DRY, KISS

pizz1 = Pizza.margarita()
print(pizz1)
print(pizz1.area(4))
print('--------------------------------------------------')
pizz2 = Pizza.pepperoni()
print(pizz2)
print(pizz2.area(5))
print('--------------------------------------------------')
pizz3 = Pizza.chilli()
print(pizz3)
print(pizz3.area(8))