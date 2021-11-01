"""
*
Множественное наследование и миксины.
В Python, классы могут наследоваться сразу от нескольких родительских классов.

При этом методы и атрибуты родительских классов также как при обычном наследовании 
будут доступны дочернему классу.

Например, у нас есть два класса - электроавтомобили - ElectricCar и обычные 
авто - RegularCar, наследуя от этих двух классов можем создать новый класс гибридных машин - Hybrid:

class ElectricCar: 
     def use_batteries(self): 
         print('использую электричество') 

class RegularCar: 
     def use_gasoline(self): 
         print('использую бензин') 

class Hybrid(ElectricCar, RegularCar): 
     pass 
У родительских классов есть методы use_batteries и use_gasoline, которые теперь доступны 
и в дочернем классе Hybrid. Создадим экземпляр от гибридного класса и вызовем методы родителей:

car = Hybrid() 
car.use_batteries() 
car.use_gasoline() 
в терминале получим:

использую электричество 
использую топливо 


**
Миксины, или классы-примеси, это особый вид множественного наследования.

Задачей миксинов является расширение функционала других классов(например новые методы), 
но при этом, миксины не предназначены для создания от них объектов.

В качестве аналогии, рассмотрим данный пример:

class Borsh: 
     pass

class Salad: 
     pass 
у нас есть два класса для борща и салата, к этим двум классам можем написать 
миксины для соли - SaltMixin и перца - PepperMixin:

class SaltMixin: 
     def salt(self): 
         print('посолили') 

class PepperMixin: 
     def pepper(self): 
         print('поперчили')
 
class Borsh(SaltMixin, PepperMixin): 
     pass  
class Salad(SaltMixin): 
     pass 
в зависимости от того от какого миксина наследуются наши классы, объекты 
созданные от класса Borsh и Salad будут иметь доступ к методам salt и pepper:

sup = Borsh() 
sup.salt() 
sup.pepper() 
в терминале получим:

посолили 
поперчили 

При этом, блюда необязательно солить или перчить, это все делается по выбору, 
на свой вкус. Также и с миксинами, данные классы необязательны, и не предоставляют основной, 
критический функционал.

Миксины используют для добавления дополнительных свойств и методов к классу.

Подытожа, можно сказать что миксины используются в таких случаях:

- если нужно предоставить классу несколько дополнительных, но необязательных функций
- если нужно использовать одно свойство или метод в нескольких разных классах


***

Множественное наследование и миксины.

Узнав про такой принцип ООП как полиморфизм, мы понимаем что у нескольких разных классов 
могут быть одинаковые методы.

Что происходит в таком случае с классом который наследуется от нескольких других классов?

Например, у нас есть два класса А и B, в обоих классах есть метод method, также есть третий 
класс С который наследуется от классов А и B:

class A: 
     def method(self): 
         print('метод класса А')

class B: 
     def method(self): 
         print('метод класса B')

class C(A,B): 
     pass 
По принципу множественного наследования, класс С должен получить все методы и 
свойства родительских классов -А и B.

Но так как, и у А и у B есть метод с одинаковым названием method, потенциально 
это должно приводить к ошибке, так как в одном классе С не может существовать двух 
методов с одним и тем же названием.

Python обходит такую конфликтную ситуацию, таким образом, в начале поиск указанного 
метода ведется в первом указанном родителе, т.е класс А, если в классе А действительно 
есть метод под названием method, то дочерний класс С, наследует данный метод от А, 
если же его нет поиск метода ведется в классе B и так по порядку, пока метод не будет найден.

Создадим объект от класса С и вызовем метод method:

c = C() 
c.method() 
получим в терминале:

метод класса А 
Поиск метода проводится правильно, а теперь попробуем удалить метод из класса А и 
снова запустить код:

class A: 
     pass

class B: 
     def method(self): 
         print('метод класса B') 

class C(A,B): 
     pass 

c = C() 
c.method() 
получим в терминале:

метод класса B 
Python не найдя метод в первом родительском классе, перешел ко второму 
родителю - к классу B и унаследовал данный метод от класса B.

****
В предыдущем примере, мы рассмотрели как ведется поиск методов и атрибутов во множественном наследовании.
 Формально такой поиск называют МRO - method resolution order, порядок разрешения методов(атрибуты 
 тоже попадают под это правило).

Допустим, у нас есть классы с множественным наследованием:

class Grandpa: 
     pass 
class Grandma: 
     pass 
class Dad(Grandpa, Grandma): 
     pass 
class Mom: 
     pass 
class Me(Dad, Mom): 
     pass 
Класс Me наследуется от классов Dad и Mom, класс Dad в свою очередь наследуется от 
классов Grandpa, Grandma.

При поиске методов и атрибутов, для самого младшего класса Me, мы знаем что Python в начале будет 
искать в самом классе Me, затем перейдет к первому родителю - Dad.

Если же метод или атрибут не будет найден, далее будет производится поиск в родительских классах 
класса Dad, также начиная с первого указанного родителя, т.е в Grandpa, затем в Grandma.

Проверив всю ветку класса Dad, только в случае если запрашиваемый метод и атрибут не были найдены, 
Python начнет поиск во втором родительском классе класса Me - Mom.

Для того, чтобы подвтердить это, можем распечатать встроенный атрибут __mro__ и у класса Me:

print(Me.__mro__) 
получим в терминале запись:

(<class '__main__.Me'>, <class '__main__.Dad'>, <class '__main__.Grandpa'>, <class '__main__.Grandma'>,
 <class '__main__.Mom'>, <class 'object'>) 
в самом конце поиск методов и атрибутов проводится в классе object, который является базовым классом от 
которого наследуются все созданные нами классы.

"""

# 1) -----Наследование-----

# class Parent:
#     def who_am_i(self):
#         print("I'm a parent")

# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print("I am a child")

# child = Child()
# child.who_am_i()


# 2) -----Многоуровневое наследование, MRO(method resolution order)-----

# class Grandpa:
#     def talant(self):
#         print("I'm good at dancing")

# class Grandma:
#     def talant(self):
#         print("I'm good at singing")

# class Father:
#     last_name = 'White'

#     def talant(self):
#         print("I can build houses")

# class Mother(Grandpa, Grandma):
#     last_name = 'Brown'

#     # def talant(self):
#     #     print("I'm good at cooking")

# class Child(Father, Mother):
#     pass

# child = Child()
# print(child.last_name)
# child.talant()
# # print(Child.mro())



# 3) ----- -----

# class A:
#     def __init__(self, param):
#         print(f"Hey, it's A class, I got {param}parameters")

#     def get_letter(self):
#         print('Aaaaa')

# class B:
#     def __init__(self, param):
#         print(f"Hey, it's B class, I got {param} prameter")

#     def get_letter(self):
#         print('Bbbbb')

# class C(A, B):
#     # pass
#     def get_letter(self):
#         print('Ccccc')

#     # pass
#     # def __init__(self):
#     #     print(f"Hey it's C class, I don't get any parameters")

# c = C('makers')
# print(C.mro())
# c.get_letter()


""" 4) ----- Diamond problem ----- """

        #     A
        #   /   \
        # B-------C
        #   \   /
        #     D

class A:
    def method(self):
        print("Hello im A")

class B(A):
    # pass
    def method(self):
        # super().method()
        print("Hello im B")

class C(A):
    def method(self):
        # super().method()
        print("Hello im C")

class D(B, C):
    pass
    # def method(self):
    #     print("Hey, D")

d = D()
d.method()
print(D.mro())


""" 5) ----- Миксины ----- """

#SOLID

# class Insects:
#     def __init__(self):
#         print("I am an insect")

# class Bird:
#     def __init__(self):
#         print("I am a bird")

# class FlyMixin:
#     def fly(self):
#         print("I can fly")

# class Hawk(Bird, FlyMixin):
#     pass        #DRY

# class Butterfly(Insects, FlyMixin):
#     pass

# class Eagle(Bird, FlyMixin):
#     pass

# class Pinguin(Bird):
#     pass

# hawk = Hawk()
# hawk.fly()

# eagle = Eagle()
# eagle.fly()

# ping = Pinguin()

# butterfly = Butterfly()
# butterfly.fly()


# 6) -----  -----

# class Vehicle:
#     pass

# class Gadgets:
#     pass

# class Home:
#     pass

# class RadioMixin:
#     def play_song(self, station):
#         print(f"Playing some song on station {station}")

# class Car(Vehicle, RadioMixin):
#     pass

# class Phone(Gadgets, RadioMixin):
#     pass

# class ShowerCabin(Home, RadioMixin):
#     pass

# car = Car()
# tel = Phone()
# showercab = ShowerCabin()
# car.play_song(station='Europe +')
# tel.play_song(station='Makers_Bootcamp')
# showercab.play_song(station='Retro_FM')