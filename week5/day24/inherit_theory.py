"""
ООП. Наследование. Теория

В языке Python класс может быть создан либо как совершенно новый, либо как «производный» от существующего. 
Важно отметить, что производный класс наследует члены родительского (базового) класса, от которого он произошел, 
в дополнение к своим собственным членам.

Возможность наследовать члены из базового класса позволяет создавать производные классы, имеющие некоторые общие 
свойства, которые были определены для базового класса. Например, в базовом классе Polygon (Многоугольник) могут 
быть определены такие свойства, как ширина и высота, которые являются общими для всех многоугольников. 
Классы Rectangle (Прямоугольник) и Triangle (Треугольник) могут являться производными от класса Polygon, 
наследуя его свойства «ширина» и «высота», а также могут иметь свои собственные члены, определяющие уникальные 
свойства, присущие только им.

Чтобы объявить производный класс, нужно после его имени добавить скобки, в которых указать имя родительского класса.

class Polygon:
    width = 0
    height = 0
    def set_values(self, width, height):
        Polygon.width = width
        Polygon.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def area(self):
        return(self.width * self.height) / 2

rect = Rectangle()
trey = Triangle()

rect.set_values(4, 5)
trey.set_values(4, 5)

print('Rectangle Area:', rect.area())
print('Triangle Area:', trey.area())
В языке Python класс равносилен понятию тип данных.

Что такое класс или тип?

Проведем аналогию с реальным миром. Если мы возьмем конкретный стол, то это объект, но не класс. А вот общее представление 
о столах,их назначении – это класс. Ему принадлежат все реальные объекты столов, какими бы они ни были. Класс столов дает 
общую характеристику всем столам в мире, он их обобщает. То же самое с целыми числами в Python. Тип int – это класс целых 
чисел. Числа 5,100134, -10 и т. д. – это конкретные объекты этого класса. Например, мы можем создать свой класс, похожий на словарь:

class Mydict(dict):
    def get(self, key, default = 0):
        return dict.get(self, key, default)

a = dict(a=1, b=2)
b = Mydict(a=1, b=2)
Класс Mydict ведёт себя точно так же, как и словарь, за исключением того, что метод get по умолчанию возвращает не None, а 0.

Создание родительского класса в Python.
Создайте класс Person, с name в качестве свойства и двумя методами get_name(), is_student().

class Person(object):
    # Constructor
   def __init__(self, name):
       self.name = name

    # To get name
   def get_name(self):
       return self.name

    # To check if this person is Student
   def is_student(self):
       return True

person = Person("Влад")  # An Object of Person
print(person.get_name(), person.is_student())

# Вывод
# Влад True
Создание дочернего класса.
Если мы хотим создать класс, который наследует функциональность от другого класса, отправьте родительский класс 
в качестве параметра при создании дочернего класса. Смотрите следующий код.

class Student(Person):
    # Here we return true
   def is_student(self):
       return False
Теперь класс Student имеет те же свойства и методы, что и класс Person.

Используйте класс Student для создания объекта, а затем выполните методы get_name() и is_student().

student = Student("Айпери")  # An Object of Student
print(student.get_name(), student.is_student())
# Вывод
# Айпери False
Добавление ​​метода init(). Мы уже добавили конструктор внутри класса Person.

def __init__(self, name):
      self.name = name
Это означает, что во время создания объекта мы можем установить свойства класса.

Когда вы добавляете функцию init() в дочерний класс (в нашем случае это класс Student), дочерний класс больше 
не наследует родительский метод init(). Дочерний метод init() отменяет наследование родительского init(). 
Если мы хотим сохранить наследование родительского метода init(), добавьте вызов родительского метода init(). 
Смотрите следующий код.

class Student(Person):
   def __init__(self, name):
       Person.__init__(self, name)
Одиночное наследование. Когда дочерний класс наследует только от одного родительского класса, это называется 
одиночным наследованием. Мы видели пример выше.

Множественное наследование. Когда дочерний класс наследуется от нескольких родительских классов, это 
называется множественным наследованием. В отличие от Java и C ++, Python поддерживает множественное наследование. 
Мы указываем все родительские классы в виде списка через запятую в скобках.

class Base1(object):
   def __init__(self):
       self.str1 = "Eleven"
       print("First Base Class")

 class Base2(object):
   def __init__(self):
       self.str2 = "Krunal"
       print("Second Base Class")

 class Derived(Base1, Base2):
   def __init__(self):
       Base1.__init__(self)
       Base2.__init__(self)
       print("Derived Class")

    def print_data(self):
       print(self.str1, self.str2)

obj = Derived()
obj.print_data()

# Вывод
# First Base Class
# Second Base Class
# Derived Class
# Eleven Krunal
Многоуровневое наследование Многоуровневое наследование означает бабушка с дедушкой -> родители -> дети.

class GrandParents(object):
    # Constructor
   def __init__(self, name):
       self.name = name

    # To get name
   def get_name(self):
       return self.name

 # Inherited or SubClass
class Parents(GrandParents):
    # Constructor
   def __init__(self, name, age):
       GrandParents.__init__(self, name)
       self.age = age

    # To get name
   def get_age(self):
       return self.age

 # Inherited or SubClass
class Children(Parents):
    # Constructor
   def __init__(self, name, age, address):
       Parents.__init__(self, name, age)
       self.address = address

    # To get address
   def get_address(self):
       return self.address

g = Children("Иван", 36, "Бишкек")
print(g.get_name(), g.get_age(), g.get_address())

# Вывод
# Иван 36 Бишкек
Иерархическое наследование
Когда более одного класса является производным от одного базового класса, такое наследование известно как 
иерархическое наследование, где методы, которые являются общими на нижнем уровне, включаются в родительский класс.

Проблемы, в которых должна поддерживаться иерархия, могут быть эффективно решены с помощью этого наследования. 
Проще говоря, из одной базы создается более одного производного класса.

Гибридное наследование
Гибридное наследование представляет собой комбинацию множественного наследования и многоуровневого наследования. 
Класс является производным от двух классов, как в множественном наследовании. Однако один из родительских классов 
не является базовым классом. Это производный класс.

Гибридное наследование объединяет несколько форм наследования. Это смесь более чем одного типа наследования.


* Принципы ООП. Наследование.

С помощью принципа ООП наследования, можно вынести общие "черты", характеристики нескольких классов 
в один родительский класс.

Наследование позволяет нам не повторяться и делает наш код более организованным. Давайте рассмотрим 
простой пример:

class Parent: 
     def __init__(self): 
         pass 

     def method(self): 
         return 'Метод класса Parent' 

class Child(Parent): 
     pass 

для того чтобы наследовать класс Child от класса Parent, после названия Child, в скобках прописываем 
название класса от которого наследуем - class Child(Parent).

Теперь все методы и свойства которые есть у Parent, будут доступны в Child:

obj = Child() 
print(obj.method()) 
распечатает в терминале:

Метод класса Parent 
несмотря на то, что мы создали объект obj от класса Child, внутри которого данного метода нет.

Дочерние классы могут наследовать методы от родительских и переопределять(изменять) их внутри своего 
класса и при этом это никак не повлияет и не изменит сам родительский класс.


**
Одним из главных преимуществ наследования является возможность расширения родительских методов.

Наследуя от родительского класса, можно дополнить, либо полностью изменить методы родительского 
класса в дочернем.

У нас есть родительский и дочерние классы:

class Transport: 
     def move(self): 
         print("движется:") 
 
class Boat(Transport): 
     pass 

class Car(Transport): 
     pass 

у родительского класса Transport есть метод move, т.е любой транспорт может двигаться.

От Trasnport наследуем классы Boat - лодка, и Car - машина.

Для Boat и Car метод move уже доступен, так как они унаследовали его сразу от родителя, 
но допустим мы хотим расширить метод move и добавить дополнительный функционал.

Для этого воспользуемся функцией super():

class Transport: 
     def move(self): 
         print("движется:") 

class Boat(Transport): 
     def move(self): 
         super().move() 
         print("плывет") 

class Car(Transport): 
     def move(self): 
         super().move()  
         print("едет") 
к каждому из дочерних классов прописываем метод move, внутри move в начале прописываем функцию super(), 
которая указывает на родительский класс(говорит Python: "ищи у родителя")

через точку указываем что именно мы хотим перенять, в нашем случае метод move() - super().move().

После того как мы переняли сам метод, можем расширить его, дописав дополнительный код, 
в Boat мы добавили - print("плывет"), а в Car - print("едет").

Создадим объект от Boat и вызовем метод move:

boat = Boat() 
boat.move() 
В терминале получим:

движется: 
плывет 
Проделаем тоже самое с Car:

car = Car() 
car.move() 
Вывод будет:

движется: 
едет 


***
Все в языке Python является объектом, то есть имеет свои аттрибуты и методы, такие же как мы прописывали 
для созданных нами классов.

Каждый тип данных относится к своему классу, созданный нами словарь это объект класса dictionary, число 
в нашем коде - объект от класса integer, строка 'hello' которую мы можем распечатать является экземпляром 
класса string.

Это значит что мы можем наследовать наши собственные классы от этих встроенных классов.

Создадим свой класс Number, который наследуется от встроенного int:

class Number(int): 
     def __init__(self, value): 
         self.value = value
    
     def count_digits(self): 
         digits = len(str(self.value)) 
         return digits 
у чисел в Python нет метода высчитывающего из скольких цифр состоит число, напишем свой метод count_digits, 
который переводит каждое число в тип данных string и возвращает длину строки.

Создадим экземпляр класса Number в переменной num, со значением в value - 123 и применим к нему метод 
count_digits:

num = Number(123) 
print(num.count_digits()) 
Получим вывод в терминале:

3 

т.к цифр в числе 123 - три.

Если мы попробуем создать объект от Number не с числом, а со строкой:

num = Number('hello') 
наследование от класса int, не допустит объекты с не числовым значением и выдаст нам исключение:

ValueError: invalid literal for int() with base 10: 'hello' 
таким образом можем удостовериться что наследование от int в нашем классе работает.


****
Наследуя от встроенных классов, мы также можем переопределять родительские методы, то есть встроенные методы 
типов данных.

Создадим свой класс MyList, наследуя от встроенного класса list и переопределим встроенный метод списков 
append таким образом чтобы при добавлении нового элемента нам печаталась строка "добавил!":

class MyList(list): 
     def append(self, object): 
         print('добавил!') 
         return super().append(object) 
метод append принимает ссылку на объект в self и второй параметр - объект который мы хотим добавить в 
список(у нас в переменную object).

Добавляем print('добавил!'), затем возвращаем родительский метод класса list через функцию super(), 
говорим какой именно метод переопределяем - встроенный append и передаем объект который нужно 
добавить - super().append(object).

Создадим экземпляр класса MyList в перемнной lst, применяя метод append добавим новый элемент в список:

lst = MyList([1, 2, 3]) 
print(lst.append(4)) 
print(lst) 
Получим в терминале:

добавил! 
[1, 2, 3, 4] 
Благодаря тому, что мы корректно унаследовали родительский метод через функцию super(), встроенный 
метод append не сломался и работает правильно.


*****
Помимо обычных методов, в Python можно также наследовать __init__ родительского класса. К примеру, 
у нас есть класс Person(человек) объекты которого имеют атрибут name:

class Person: 
 def __init__(self, name): 
     self.name = name  
теперь, создадим класс Employee(работник) который наследуется от класса Person, у объектов Employee 
также должны быть имена - name, но мы хотим добавить еще один атрибут - job(работа).

Для этого, переопределяем функцию __init__, в параметры записываем атрибуты которые нам нужны - self, name и job.

Внутри функции, унаследуем родительский метод __init__ через super(), и в скобках укажем какой атрибут 
нам нужен из родительского класса - name.

Затем, привяжем новый атрибут job через ссылку на объект self:

class Employee(Person): 
  def __init__(self, name, job): 
      super().__init__(name) 
      self.job = job 

теперь объект созданный от класса Employee будет иметь атрибуты name и job:

obj = Employee('Steve', 'programmer') 


******
Каждый раз как мы создаем метод внутри класса, мы обязательно передаем в параметры 
self - ссылку на сам объект созданный от класса.

Зачем же нам нужен self в методах?

Создадим класс A, у которого есть один метод, который просто распечатывает строку 'hey!'. 
Создадим экземпляр класса в переменной x и применим к нему метод:

class A: 
  def method(self): 
      print('hey!') 
 
x = A()  
x.method() 
получим вывод в терминале:

hey! 
тут, нигде явно не видна работа параметра self, self также не используется внутри функции.

Попробуем удалить self из метода и заново применить метод к объекту x:

class A: 
 def method(): 
     print('hey!') 

x = A() 
x.method() 
получим в терминале исключение:

TypeError: method() takes 0 positional arguments but 1 was given  
#метод не принимает никаких позиционных аргументов, но мы передали 1 
Сама привязка метода к объекту - x.method(), то есть в том месте где мы указываем наш объект ставим 
точку и вызываем метод, и является тем самым self который мы указываем при создании метода.

Мы убрали self из метода и попытались привязать объект x к методу method, в итоге Python не понял 
куда именно поместить ссылку на объект, так как у метода нет никаких параметров, скобки пустые и выдал исключение.

В self всегда хранится ссылка на наш объект, поэтому чтобы привязать метод или атрибут к объекту или манипулировать 
объектом с помощью циклов, функций, встроенных методов мы должны обращаться к нему через self.


*
При полиморфизме один и тот же метод может использоваться для объектов от разных классов, при этом результат может 
меняться в зависимости к какому классу принадлежит объект.

Одним из самых распространенных примеров полиморфизма в Python является оператор + . Напишем простую функцию, 
складывающую два параметра:

def add(x, y): 
    print(x + y) 
Теперь, используем функцию add для двух строк, двух списков и двух чисел:

add('makers ','bootcamp') 
add([1, True], [3, False]) 
add(1, 2) 
во всех трех случаях наш код отработает корректно, однако в зависимости от того к какому классу, типу данных, 
принадлежат переданные аргументы, поведение функции меняется.

В терминале получаем вывод:

makers bootcamp 
[1, True, 3, False] 
3 
функция add провела конкатенацию со строками, объединила два списка в один, а числа сложила по значению.
"""

# 1) Syntax
# class Parent:  # class Parent(object): or class Parent():
#     pass

# class Child(Parent):
#     pass

# 2)
# class A(object):
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# # isinstance(obj, class)
# a = A()
# b = A()
# c = C()
# print(isinstance(c, A))  # True
# print(isinstance(c, B))  # True
# print(isinstance(b, A))  # True
# print(isinstance(a, B))  # False


# 3) Наследование методов и атрибутов / переопределение методов

# class Polygon:

#     sides = 'many'

#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         # print(self.args)
#         # print(self.kwargs)

#     def get_perimeter(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return sum(self.kwargs.values())

# class Rectangle(Polygon):
    
#     sides = 4
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def get_perimeter(self):
#         return (self.a + self.b) * 2

# class Square(Rectangle):
    
#     def __init__(self, a):
#         self.a = a

#     def get_perimeter(self):
#         return self.a * 4

# class Triangle(Polygon):

#     sides = 3
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def get_perimeter(self):
#         return self.a + self.b + self.c

# square = Square(a=5)
# print(square.sides)
# print(square.get_perimeter())

# triangle1 = Triangle(a=2, b=3, c=4)
# print(triangle1.sides)
# print(triangle1.get_perimeter())

# rectangle = Rectangle(a=7, b=6)
# rectangle2 = Rectangle(a=9, b=2)
# print(rectangle.sides)
# print(rectangle.get_perimeter())
# print(rectangle2.get_perimeter())

# polygon = Polygon(8, 9, 3)
# polygon = Polygon(a=8, b=9, c=3, d=5, e=7)
# print(polygon.get_perimeter())
# print(polygon.sides)


# 4) переопределение методов

# class MyDict(dict):
#     def get(self, key, default='Makers'):
#         print('This method has been changed')
#         return dict.get(self, key, default)

# dict1 = dict(a=3, b=5, c=8)
# print(dict1.get('d'))

# dict2 = MyDict(a=3, b=5, c=8)
# print(dict2.get('d'))


# 5)
# class Person:

#     def __init__(self, name, last_name, id_number):
#         self.name = name
#         self.lastname = last_name
#         self.id = id_number

#     def get_info(self):
#         print(f'{self.name} {self.lastname}, id: {self.id}')

# class Employee(Person):
#     def __init__(self, name, last_name, id_number, position, salary):
#         Person.__init__(self, name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         Person.get_info(self)
#         print(f'His occupation is {self.position} and his wage is {self.salary} $')

# person = Person(name='Jack', last_name='Smith', id_number=678)
# person.get_info()

# employee = Employee(name='Jack', last_name='Smith', id_number=678, position='Coder', salary=2500)
# employee.get_info()


# 6) 
# class Human:
#     test = 'bootcamp'

#     def __init__(self, name, last_name, id_number):
#         self.name = name
#         self.lastname = last_name
#         self.id = id_number

#     def get_info(self):
#         print(f'{self.name} {self.lastname}, id: {self.id}')

# class Employee(Human):
#     def __init__(self, name, last_name, id_number, position, salary):
#         super().__init__(name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         super().get_info()
#         print(super().test)
#         print(f'His occupation is {self.position} and his wage is {self.salary} $')

# person = Human(name='Jack', last_name='Smith', id_number=678)
# person.get_info()

# employee = Employee(name='Jack', last_name='Smith', id_number=678, position='Coder', salary=2500)
# employee.get_info()


# 7)

# class Art:
#     students_count = 100

# class Music(Art):
#     students_count = 50

#     def __init__(self):
#         Music.students_count += 1
#         Art.students_count += 1

# class Acting(Art):
#     students_count = 50

#     def __init__(self):
#         Acting.students_count += 1
#         Art.students_count += 1

# student1 = Music()
# student2 = Acting()
# student3 = Acting()

# print(Music.students_count)
# print(Acting.students_count)
# print(Art.students_count)


# 8)

# class Animal:
#     def sound(self):
#         raise NotImplementedError

# class Cat(Animal):
#     def sound(self):
#         print('Meow')

# class Dog(Animal):
#     def sound(self):
#         print('Bark')


# class Frog(Animal):
#     def sound(self):
#         print('Quak')

# # animal = Animal()
# # animal.sound()

# cat = Cat()
# cat.sound()