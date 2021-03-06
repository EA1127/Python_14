"""

ООП. Полиморфизм. Теория
Полиморфизм в объектно-ориентированном программировании – это возможность обработки разных типов данных, т. е. принадлежащих к разным классам, 
с помощью "одной и той же" функции, или метода. На самом деле одинаковым является только имя метода, его исходный код зависит от класса. 
Кроме того, результаты работы одноименных методов могут существенно различаться. Поэтому в данном контексте под полиморфизмом понимается 
множество форм одного и того же слова – имени метода.

Например, два разных класса содержат метод total, однако инструкции каждого предусматривают совершенно разные операции. 
Так в классе T1 – это прибавление 10 к аргументу, в T2 – подсчет длины строки символов. В зависимости от того, к объекту 
какого класса применяется метод total, выполняются те или иные инструкции.

class T1:
    def __init__(self):
        self.n = 10
    def total(self, a):
        return self.n + int(a)
class T2:
    def __init__(self):
        self.string = 'Hi'
    def total(self, a):
        return len(self.string + str(a))
t1 = T1()
t2 = T2()
print(t1.total(35))  # Вывод: 45
print(t2.total(35))  # Вывод: 4

В предыдущем уроке мы уже наблюдали полиморфизм между классами, связанными наследованием. У каждого может быть свой метод init() 
или square() или какой-нибудь другой. Какой именно из методов square() вызывается, и что он делает, зависит от принадлежности 
объекта к тому или иному классу.

Однако классы не обязательно должны быть связаны наследованием. Полиморфизм как один из ключевых элементов ООП существует 
независимо от наследования. Классы могут быть не родственными, но иметь одинаковые методы, как в примере выше.

Полиморфизм дает возможность реализовывать так называемые единые интерфейсы для объектов различных классов. 
Например, разные классы могут предусматривать различный способ вывода той или иной информации объектов. 
Однако одинаковое название метода вывода позволит не запутать программу, сделать код более ясным.

В Python среди прочего полиморфизм находит отражение в методах перегрузки операторов. Два из них мы уже рассмотрели. 
Это init() и del(), которые вызываются при создании объекта и его удалении. 
Полиморфизм у методов перегрузки операторов проявляется в том, что независимо от типа объекта, его участие 
в определенной операции, вызывает метод с конкретным именем. В случае init() операцией является создание объекта.

Рассмотрим пример полиморфизма на еще одном методе, который перегружает функцию str(), которую автоматически 
вызывает функция print().

Если вы создадите объект собственного класса, а потом попробуете вывести его на экран, 
то получите информацию о классе объекта и его адрес в памяти. Такое поведение функции str() по-умолчанию 
по отношению к пользовательским классам запрограммировано на самом верхнем уровне иерархии, 
где-то в суперклассе, от которого неявно наследуются все остальные.

class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

a = A(3, 4)
b = str(a)
print(a) # <__main__.A object at 0x7f251ac2f8d0>
print(b) # <__main__.A object at 0x7f251ac2f8d0>
Здесь мы используем переменную b, чтобы показать, что функция *print()* вызывает *str()* неявным образом, 
так как вывод значений обоих переменных одинаков.
Если же мы хотим, чтобы, когда объект передается функции print(), выводилась какая-нибудь другая более полезная информация, 
то в класс надо добавить специальный метод str(). Этот метод должен обязательно возвращать строку, которую будет в свою очередь 
возвращать функция str(), вызываемая функций print():

class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        s = str(self.field1)+" "+str(self.field2)         return s

a = A(3, 4)
b = str(a)

print(a) # 3 4
print(b) # 3 4
Какую именно строку возвращает метод str(), дело десятое. Он вполне может строить квадратик из символов:

class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)
    def __str__(self):
        rect = []
        # количество строк
        for i in range(self.h):
            # знак повторяется w раз
            rect.append(self.s * self.w)
        # превращаем список в строку
        rect = '\n'.join(rect)
        return rect
b = Rectangle(10, 3, '*')
print(b)  
''' **********
**********
********** '''
Пример: полиморфизм в методах класса
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

     def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

     def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

     def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

     def make_sound(self):

        print("Bark")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

Вывод:
Meow
I am a cat. My name is Kitty. I am 2.5 years old.
Meow
Bark
I am a dog. My name is Fluffy. I am 4 years old.
Bark

Здесь мы создали два класса Cat и Dog. У них похожая структура и они имеют методы с одними и теми же именами info() и *make_sound().

Однако, заметьте, что мы не создавали общего класса-родителя и не соединяли классы вместе каким-либо другим способом. 
Даже если мы можем упаковать два разных объекта в кортеж и итерировать по нему, мы будем использовать общую переменную animal. 
Это возможно благодаря полиморфизму.

"""


