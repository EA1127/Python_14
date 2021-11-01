"""
*
Магические методы это специальные методы, которые начинаются и заканчиваются двойным подчеркиванием.

Эти методы не предназначены для непосредственного вызова, вызов происходит внутри класса при выполнении 
определенного действия.

Взаимодействие с кодом, другие методы и функции запускают магические методы без нашего вмешательства, 
это может быть создание объекта от класса - метод __init__, сложение чисел оператором плюс - метод __add__ и.т.д.

Мы уже использовали некоторые магические методы, и знаем что их можно переопределять и подстраивать под себя, 
например:

-метод __init__ инициализирует объект, задает нашему объекту атрибуты
-метод __str__ срабатывает когда выводим объект в терминал через функцию print() и возвращает человекочитаемый 
вид объекта
-метод __repr__ возвращает в целом читаемый вид объекта, в отличие от __str__, не обязательно понятный человеку
-есть еще такой магический метод как __del__, который срабатывает когда вы заканчиваете работу с объектом и 
сборщик мусора 
Python начинает подчищать память.


**
В Python существует целая группа магических методов, срабатывающих тогда когда мы производим 
арифметические операции.

Данные методы вызываются как только мы ставим в нашем коде знаки арифметических 
операторов + - * / // ** % | и &

Например:

print(42 + 42) 
print('makers' + 'bootcamp') 
    #в обоих случаях срабатывает метод __add__

print(21 - 1) 
    #срабатывает метод __sub__

print(2 * 4) 
    #здесь вызывается метод __mul__

print(15 // 3) 
    #а здесь метод __floordiv__ 
Эти методы также можно переопределять для своих классов.

Например, у нас есть класс MyClass, где мы переопределим метод для оператора // :

class MyClass: 
     def __init__(self, num): 
             self.num = num

     def __floordiv__(self, num2): 
             return f'Деление без остатка равно: {self.num//num2}'
    
#здесь в self.num будет попадать число из атрибута объекта num, а в num2 попадает второе число 
# после оператора //
создадим объект от класса, со значением num равным 5 и поделим наш объект на 2:

obj = MyClass(5) 
print(obj // 2) 
в терминале получим:

Деление без остатка равно: 2 

в этом примере 2 попало в переменную num2 метода __floordiv__, а из самого объекта obj, 
метод __floordiv__ взял указанный атрибут num.


***
В Python все является объектом, а значит магические методы можно встретить везде, в том числе 
и в отдельных типах данных.

Посмотреть список магических методов можно применив функцию dir() к объекту или к классу и 
распечатав результат в терминал. К примеру, выведим магические методы списков:

print(dir(list)) 
получим данный список:

[ ... '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
 '__setattr__', '__setitem__' ...]
Зная за что отвечает тот или иной метод его можно легкo переопределить.

Так, переопределив метод __getitem__ у списков, можно изменить поведение объекта, 
при попытке вывести отдельный элемент списка.

Изменим метод так чтобы, при выводе элемента по индексу, возвращалась строка:

class Spisok(list): 
     def __init__(self,mylist): 
             self.mylist = mylist 
     def __getitem__(self, index): 
             return f'на этом месте стоит элемент {self.mylist[index]}'

lst = Spisok(['первый','второй', True]) 
print(lst[0])
метод __getitem__ получает в переменную index индекс элемента, который мы хотим 
получить(число передаемое в скобках), а в self попадает сам объект.

в терминале получим:

на этом месте стоит элемент первый 


****
Для операторов сравнения также существует своя группа магических методов.

Это:

__eq__ - для оператора равенства, ==

__ne__ - для оператора неравенства, !=

__lt__ - для оператора меньше, <

__gt__ - для оператора больше, >

__le__ - для оператора меньше или равно, <=

__ge__ - для оператора больше или равно, >=

каждый из этих методов получает два аргумента self - попадает наш объект к которому мы 
применяем сравнение и other - второе передаваемое значение, с чем мы сравниваем.

(помним что self, other это просто переменные, можно называть как угодно, главное соблюдать 
порядок передачи аргументов)


"""

# class X:
#     pass

# obj = X()

# print(dir(obj))

"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__']
"""

# print(dir(6))

"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__',
'__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', 
'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
 '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', 
 '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
  'imag', 'numerator', 'real', 'to_bytes']
"""

# print(dir('bootcamp'))

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
  '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
   '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
   'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
   'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
   'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
   'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex',
    'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
    'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""

# def func():
#     pass

# print(dir(func))
"""
['__annotations__', '__call__', '__class__', '__closure__', '__code__', 
'__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', 
'__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""

"""1) ----- __init__() -----"""

# class User:
#     def __init__(self, **kwargs):
#         print("Object is initializing...")
#         self.name = kwargs['name']
#         self.family_name = kwargs['last_name']
#         print("Object is inintialized")

# user = User(name='Linus', last_name='Torvalds')
# print(user.name)
# print(user.family_name)


"""2) ----- __new__() -----"""

# class Human(object):
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = super().__new__(cls)
#         instance.heart = 'with 4 cameras'
#         print(instance.heart)
#         print("Object created")
#         return instance

#     def __init__(self, name, last_name):
#         print("Object is initializing")
#         self.name = name
#         self.family_name = last_name

# human1 = Human(name='Linus', last_name='Torvalds')
# # print(human1.heart)

# human2 = Human('John', 'Snow')
# # print(human1.heart)

""" Singleton -- От однго класса можно создать только один обЪект """

# class Sun:
#     instance = None

#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = object.__new__(cls)   # можно использовать super() вместо object
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# sun3 = Sun()
# print(sun1 is sun2)  # True
# print(id(sun1))   # 140715950207136
# print(id(sun2))   # 140715950207136
# print(id(sun3))   # 140715950207136



"""3) ----- __str__() -----"""

# class Human:
#     def __init__(self, name, last_name):
#         self.last_name = last_name
#         self.name = name

#     def get_fullname(self):
#         return f"{self.name}, {self.last_name}"

#     def __str__(self):
#         return self.get_fullname()

# human1 = Human('Linus', 'Torvalds')
# print(human1)
# # a = str(human1)
# # print(a)


"""4) ----- __repr__() -----"""

class Human:
    def __init__(self, name, last_name):
        self.last_name = last_name
        self.name = name

    # def __str__(self):
    #     return f"{self.name}, {self.last_name} -- сработал метод str"

    def __repr__(self):
        return f"{self.name}, {self.last_name} -- сработал метод repr"

human = Human('John', 'Snow')
print(human)



"""5) ----- dunder methods -----"""

"""
__add__(self, other) -> +
__sub__(self, other) -> -
__mul__(self, other) -> *
__truediv__(self, other) -> /
__mod__(self, other) -> %
"""

# class MyInt(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         # self.value + other
#         print('This is my addition')
#         return self.value + other/3

#     def __sub__(self, other):
#         # self.value - other
#         print('This is my substraction')
#         return self.value - other + 100

#     def __mul__(self, other):
#         # self.value * other
#         print('This is my multiplication')
#         return self.value * other - 1

#     def __truediv__(self, other):
#         # self.value / other
#         print('This is my division')
#         return self.value / other + 1

#     def __mod__(self, other):
#         # self.value % other
#         return f"Остаток от деления: {self.value % other}"

#     """ Отраженные арифметические операторы """

    # def __radd__(self, other):
    #     # other + self.value
    #     print('This is my r-addition')
    #     return other + self.value + 20

    # def __rsub__(self, other):
    #     # other - self.value
    #     print('This is my r-substraction')
    #     return other - self.value/2

    # def __rmul__(self, other):
    #     # other * self.value
    #     print('This is my r-multiplication')
    #     return other * self.value + 5

    # def __rtruediv__(self, other):
    #     # other / self.value
    #     print('This is my r-division')
    #     return other / self.value - 7

#     """ Составное присваивание"""

    # a = 7
    # a += 7  ==  a = a + 7

#     def __iadd__(self, other):
#         print('This my i-addition')
#         return self.value + other

#     def __isub__(self, other):
#         print('This my i-substraction')
#         return self.value - other - 1

#     def __imul__(self, other):
#         print('This my i-multiplication')
#         return self.value * other

#     def __itruediv__(self, other):
#         print('This my i-division')
#         return self.value / other

# a = MyInt(10)
# # print(a + 5)
# # print(a - 5)
# # print(a * 3)
# # print(a / 5)
# # print(a % 3)
# # print(5 + a)
# # print(20 - a)
# # print(7 * a)
# # print(40 / a)
# # a += 7
# # print(a)
# # a -= 7
# # print(a)
# # a *= 7
# # print(a)
# a /= 7
# print(a)


"""6) ----- Магические методы сравнения -----"""

"""
__eq__ -> ==
__ne__ -> !=
__gt__ -> >
__ge__ -> >=
__lt__ -> <
__le__ -> <=
"""

# class Human:
#     def __init__(self, name, familia, age):
#         self.name = name
#         self.familia = familia
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

#     def __ne__(self, other):
#         return self.age != other.age

#     def __gt__(self, other):
#         return len(self.name) > len(other.name)

#     def __lt__(self, other):
#         return len(self.name) < len(other.name)

#     def __ge__(self, other):
#         return len(self.familia) >= len(other.familia)

#     def __le__(self, other):
#         return len(self.familia) <= len(other.familia)

# human1 = Human(name="Tom", familia="Levi", age=14)
# human2 = Human(name="John", familia="Snow", age=34)
# print(human1 == human2)
# print(human1 != human2)
# print(human1 > human2)
# print(human1 < human2)
# print(human1 >= human2)
# print(human1 <= human2)



"""7) __getattr__, __setattr__, __delattr__, ___getattribute__"""

# class MyClass:
#     def __init__(self):
#         self.name = "Makers"
#         self.last_name = "Bootcamp"
#         print(self.__dict__)

#     def __getattr__(self, item):
#         print(self.__dict__)
#         return self.__dict__.get(item, 'Hi dude')

#     def __getattribute__(self, item):
#         print('This is custom getattribute magic method')
#         return super().__getattribute__(item)

#     def __setattr__(self, item, value):    #self.value = value
#         print(f"I want to set attribute {item} with value {value}")
#         self.__dict__[item] = value

#     def __delattr__(self, item):    # del  self.item
#         print(f"Want to delete attribute named {item}")
#         self.__dict__.pop(item, 0)

# obj = MyClass()
# # print(obj.name)
# # print(obj.age)
# obj.age = 2
# del obj.age
# print(obj.age)


# 8)---------------

"""
__len__(self) -> len()
__getitem__(self, key) -> self.key
__setitem__(self, key, value) -> self[key] = value
__delitem__(self, key) -> del self[key]
__contains__(self, item) -> item in self  or  item not in self (True, False)
"""

# class MyClass(dict):  
#     def __getitem__(self, key):
#       print(f'I am giving you a value of {key}')
#       result = super().__getitem__(key) + 1
#       return result

#     def __setitem__(self, key, value):
#       value += 1
#       super().__setitem__(key, value)

# dict_ = MyClass(a=6, b=7, c=8)
# # print(dict_)
# print(dict_['c'])
# dict_['d'] = 9
# print(dict_)



# 9)---------------


# class MyList(list):
#     def __init__(self, iterable):
#         self.list = iterable

#     def __contains__(self, item):
#         if item in self.list:
#           return True
#         else:
#           return False

# a = MyList([1, 2, 3, 4, 5])
# print(3 in a)
        
