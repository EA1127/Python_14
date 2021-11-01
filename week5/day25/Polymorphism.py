

# ---1---

# a = 6
# b = 9
# print(a + b)
# c = '6'
# d = '9'
# print(c + d)
# f = [1,2,3,4,5]
# e = [6,7,8,9]
# print(f + e)


# ---2---

# a = 'makers'
# b = 3
# c = [True, 'bootcamp', 677]
# d = {'makers': 'bootcamp'}
# e = (6,7,8,9)
# f = {False, 'Makers', 6, 3, 8}
# print(f'This is string methods: {dir(a)}')
# print(f'This is integer methods: {dir(b)}')
# print(f'This is list methods: {dir(c)}')
# print(f'This is dictionary methods: {dir(d)}')
# print(f'This is tuple methods: {dir(e)}')
# print(f'This is set methods: {dir(f)}')

"""
This is string methods: 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

This is integer methods: ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
'__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', 
'__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', 
'__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 
'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

This is list methods: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
'pop', 'remove', 'reverse', 'sort']

This is dictionary methods: ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

This is tuple methods: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'count', 'index']

This is set methods: ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', 
'__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

"""

# ---3---
# pop() -> list, dict, set

# list_ = [3,4,5,6]
# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 11, 7}

# list_.pop(1)
# dict_.pop('b')
# set_.pop()

# print(list_)
# print(dict_)
# print(set_)


# ---4---

# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 11, 7, 0}

# dict_.update(d=4, e=5)
# set_.update({8, 0, -1})
# print(dict_)
# print(set_)


""" 5 """

class Car:
    def __init__(self, name):
        self.name = name

    def go(self, destination):
        print(f"{self.name} is going by car to {destination}")


class Ship:
    def __init__(self, name):
        self.name = name

    def go(self, destination):
        print(f"{self.name} is going by ship to {destination}")

class Airplane:
    def __init__(self, name):
        self.name = name

    def go(self, destination):
        print(f"{self.name} is flying by airplane to {destination}")

class Train:
    def __init__(self, name):
        self.name = name

    def go(self, destination):
        print(f"{self.name} is going by train to {destination}")


""" 6 """

class Infomixin:

    def info(self):
        my_class = self.__class__.__name__
        print(f"I'm a {my_class}, named {self.name}, age {self.age}")    


class Cat(Infomixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Meow')

class Dog(Infomixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Woof')

class Duck(Infomixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Quack')

animal = Dog('Tom', 7)
animal.info()


""" 7 """

# class T1:
#     def __init__(self, iterible):
#         self.list = iterible

#     def total(self):
#         return sum(self.list)

# class T2:

#     def __init__(self, iterible):
#         self.list = iterible

#     def total(self):
#         return len(self.list)


# t1 = T1([1,2,3,4,5,6,7])
# t2 = T2([1,2,3,4,5,6,7])

# print(t1.total())
# print(t2.total())



""" Task - 1 
ABSTRACT CLASS (https://docs.python.org/3/library/abc.html)"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, pizza, cost):
        self.pizza = pizza
        self.cost = cost

    @abstractmethod
    def add_extra(self, ingredient):
        self.ingredient = ingredient
        print(f'{self.pizza} with extra {self.ingredient} costs {self.cost}')

class DodoPizza(Pizza):
    def add_extra(self, *ingredient):
        self.cost += 50 * len(ingredient)
        return super().add_extra(ingredient)

    def late(self, time):
        if time >= 5:
            print(f"You get free pizza card!!!")

class PapaJohns(Pizza):
    def add_extra(self, *ingredient):
        self.cost += 70  * len(ingredient)
        return super().add_extra(ingredient)

    def late(self, time):
        if time >= 100:
            print(f"This pizza is free")
            self.cost = 0
        else:
            self.cost = self.cost - (self.cost * time / 100)


pizza1 = DodoPizza('Pepperoni', 500)
pizza1.add_extra('cheese', 'sauce', 'garlic')
pizza1.late(5)
pizza2 = PapaJohns('Margarita', 400)
pizza2.add_extra('tomatos', 'bazil')
pizza2.late(30)
print(pizza2.cost)

# for pizza in [pizza1, pizza2]:
#     pizza.late(10)


""" Task - 2 """
# class_method -> (cls)
# instance_method


class King:
    def move(self):
        print("Я хожу на 1 клетку в любую сторону")

class Queen:
    def move(self):
        print("Я хожу как королева")

class Horse:
    def move(self):
        print("Я хожу буквой Г")

figure1 = King()
figure2 = Queen()
figure3 = Horse()

for figure in [figure1, figure2, figure3]:
    figure.move()

#-------------------------------------------------------

# static_method

class King:
    @staticmethod
    def move():
        print("Я хожу на 1 клетку в любую сторону")

class Queen:
    @staticmethod
    def move():
        print("Я хожу как королева")

class Horse:
    @staticmethod
    def move():
        print("Я хожу буквой Г")

figure1 = King()
figure2 = Queen()
figure3 = Horse()

for figure in [figure1, figure2, figure3]:
    figure.move()
