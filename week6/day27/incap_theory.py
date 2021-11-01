"""
Инкапсуляция 

Инкапсуляция — ограничение доступа к составляющим объект компонентам 
(методам и переменным). Инкапсуляция делает некоторые из компонент доступными только 
внутри класса. Инкапсуляция в Python работает лишь на уровне соглашения между программистами 
о том, какие атрибуты являются общедоступными, а какие — внутренними. 

Одиночное подчеркивание в 
начале имени атрибута говорит о том, что переменная или метод не предназначен для использования 
вне методов класса, однако атрибут доступен по этому имени. Python 3 предоставляет 3 уровня
 доступа к данным: 
 
 публичный (public, нет особого синтаксиса, publicBanana); 
 защищенный (protected, одно нижнее подчеркивание в начале названия, _protectedBanana); 
 приватный (private, два нижних подчеркивания в начала названия, __privateBanana). 
 
class A: 
    def _protected(self): 
        return "Это защищенный метод!" 
         
a = A()
print(a._protected()) # Это защищенный метод! 

Двойное подчеркивание в начале имени атрибута даёт большую защиту: атрибут становится недоступным по этому имени. 

class B:
    def __private(self):
        print("Это приватный метод!")

b = B()
print(b.__private()) 

Traceback (most recent call last): File "/home/murat/Desktop/python/test/test.py",
line 6, in <module> print(b.__private()) AttributeError: 'B' object has no attribute '__private' 
Однако полностью это не защищает, так как атрибут всё равно остаётся доступным под именем 

_ИмяКласса__ИмяАтрибута:

class B:
    def __private(self):
        print("Это приватный метод!")

b = B()
print(b._B__private()) # Это приватный метод!

Заключение Python3 не обеспечивает ограниченный доступ к каким-либо переменным или методам класса. 
Данные, которые должны быть скрыты, на самом деле могут быть прочитаны и изменены. 
В Python3 инкапсуляция является скорее условностью, и программист должен самостоятельно заботиться о ее сохранении.


*
С помощью инкапсуляции можно ограничить доступ к атрибутам и методам внутри класса.
В Python существует три вида "защиты": публичный, защищенный и приватный.
К публичному виду относятся все элементы класса по умолчанию, то есть здесь инкапсуляция отсутсвует.
К защищенному виду относятся атрибуты и методы с одним подчеркиванем в начале названия атрибута или метода:

class A: 
  def _protected(self): 
      print('защищен') 
однако, если мы создадим объект от данного класса и вызовем метод _protected:

a = A() 
a._protected() 
то в терминале все равно получим вывод:

защищен 

Данный вид инкапсуляции, в Python, работает на уровне соглашения между разработчиками, т.е на самом деле Python, 
никак не скрывает и не защищает ваши методы и атрибуты.

Но вы можете поставить одно подчеркивание перед названием, чтобы дать понять другим программистам, которые будут 
использовать ваш код, что данный элемент изменять нельзя.

Приватные методы и атрибуты создаются двумя нижними подчеркиваниями до названия метода или атрибута.

Например:

class A:
    def __private(self):
        print('приватный') 
если мы создадим объект и попытаемся вызвать такой метод:

a = A() 
a.__private() 
в терминале уже получим исключение:

AttributeError: 'A' object has no attribute '__private' 


** getter,  setter

Несмотря на то что, при вызове приватных методов и атрибутов мы получали в терминале исключения, 
такую инкапсуляцию в Python также можно обойти. Для этого используют getters и setters методы.

На самом деле getters и setters методы представляют из себя самые обыкновенные методы внутри класса, 
в которых мы прописываем такую логику, с помощью которой сможем получить тот или иной приватный атрибут.

getter(геттер) - это любой метод, с помощью которого мы можем получить значение приватного атрибута
setter(сеттер) - это любой метод, с помощью которого мы можем изменить значение приватного атрибута

К примеру, у нас есть класс Phone, у объектов класса есть приватное свойство - __passcode, пароль от телефона:

class Phone: 
def __init__(self, passcode): 
    self.__passcode = passcode 

напишем для данного атрибута геттер и сеттер:

class Phone: 
def __init__(self, passcode): 
    self.__passcode = passcode

def get_passcode(self): 
    return self.__passcode
    
def set_passcode(self, new): 
    self.__passcode = new 

методы геттеры и сеттеры могут называться как угодно, но для ясности часто перед началом названия 
метода добавляют get, либо set.

get_passcode - наш getter метод, возвращает значение атрибута __passcode в обход защиты.

set_passcode - устанавливает новое значение атрибуту, которое передается в переменную new.

Создадим объект от данного класса, изменим пароль с помощью set_passcode и вызовем get_passcode:

myphone = Phone(1234) 
myphone.set_passcode(9876) 
print(myphone.get_passcode()) 

Получим в терминале новое значение:

9876 

Зачем мы используем getters и setters?

- с помощью getters и setters можно установить разные уровни доступа, к примеру с помощью условного 
ветвления if...else можно установить доступ к атрибутам в зависимости от выполнения условий.

- таким способом можно скрыть структуру кода, представления атрибутов, т.е посторонние не увидят как 
реализован тот или иной атрибут, но смогут получить значение атрибута.

- можно добавить логику проверки для получения и установки значения.

- можно поддерживать единый интерфейс на случай изменения внутренних элементов, т.е можно контроллировать 
изменения извне.


***  @название.setters   @property

Для удобства, в инкапсуляции существует два декоратора для setters - @название.setters, а для getters - @property.

С помощью данных декораторов можно имитировать обычное присваивание нового значение атрибуту через знак равно 
и доступ к значению атрибута через точку для приватных атрибутов.

То есть они будут работать также, как будто бы и не были защищены:

obj.атрибут  
     #выведет значение  
obj.атрибут = 'hello!'  
     #установит новое значение атрибуту объекта 
Перепишем методы нашего класса Phone через данные декораторы:

class Phone: 
  def __init__(self, passcode): 
      self.__passcode = passcode 
 
  @property 
  def code(self): 
      return self.__passcode

  @code.setter 
  def code(self, new): 
      self.__passcode = new  

Обычно, Python не допускает создание функций с одинаковым названием, но в инкапсуляции для того чтобы 
наши декораторы работали корректно, оба метода и setter и getter должны иметь одно название.

Для декоратора @property достаточно просто добавить его над методом, который отвечает за получение значения.

Для декоратора @название.setter, в начале нужно прописать название функции, к примеру если функция называется 
func, то декоратор будет выглядеть таким образом - @func.setter.

Создадим объект от класса и посмотрим как применяются декорированные методы:

  myphone = Phone(1234) 
  print(myphone.code) 

как мы видим, для получения приватного атрибута, теперь достаточно просто указать название объекта и через 
точку указать название атрибута, в терминале получим:

1234 

если же мы хотим установить новое значение, делается это также как если бы мы присваивали новое значение 
обычному(публичному) атрибуту:

myphone.code = 4321 
print(myphone.code) 
в терминале получим:

4321 

Помним что, основная цель любого декоратора - изменить методы или атрибуты вашего класса таким образом, 
чтобы вам не нужно было вносить какие-либо изменения в свой код.

"""



#  Модификаторы доступа,  getter, setter

"""
Модификаторы доступа:
1, public - password,  get_info()
2. protected - _password, _get_info()
3. private - __password, __get_info()

"""
# 1)------ getter, setter

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def get_password(self, username):   # getter
        if self.username == username:
            return self.__password
        else:
            return 'NO!!!'

    def set_password(self, old_password, new_password):   # setter
        if self.__password == old_password:
            self.__password = new_password
        else:
            return "NO!!!"


#     def __get_info(self):
#         print(f"Username {self.username}, password {self.__password}")

# user1 = User(username='makers123', password='bootcamp567')
# print(user1.username)
# print(user1.get_password(username='makers123'))
# user1.set_password(old_password='bootcamp567',
#                    new_password="hello_world111")
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username='makers123'))


# 2)------ getter, setter

class Divider:
    def __init__(self):
        self.__divide_num = 2
        # self.divide_num = 0

    def get_divider(self):
        return self.__divide_num

    def set_divider(self, value):
        if not value == 0:
            self.__divide_num = value
            return "divide number is successfully changed"
        else:
            return "NO!!!"
    def divide(self, value):
        return value / self.__divide_num

obj = Divider()

# obj.divide_num = 0   # new object
# obj.__divide_num = 2   # new object
# print(obj.divide_num)
# print(obj.__divide_num)

# print(obj.divide(7))
# print(obj._Divider__divide_num)  # этот способ не стоит использовать, чтобы не нарушать соглашение!!!

print(obj.get_divider())
print(obj.divide(7))
print(obj.set_divider(value=14))
print(obj.get_divider())



# 3)------ @propety, @setter

class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.name}, {self.last_name}"

person = Person(name='John', last_name='Snow')
print(person.full_name)  # не вызываем метод а просто к нему обращаемся

# ---------------------------------------------------------------------------

# 4)------ @propety, @setter

class Divider:
    def __init__(self):
        self.__divide_num = 2
        # self.divide_num = 0

    @property           # --> getter
    def divider(self):
        return self.__divide_num

    @divider.setter     # --> setter  (позволяет обращаться как к атрибуту и менять значение атрибута)
    def divider(self, value):
        if not value == 0:
            self.__divide_num = value
            return "divide number is successfully changed"
        else:
            return "NO!!!"
    def divide(self, value):
        return value / self.__divide_num

obj = Divider()

print(obj.divider)   # using getter
print(obj.divide(7))
obj.divider = 14     # using setter
print(obj.divider)


# 5) ----------

class Car:

    def _inject_fuel(self):
        print('Fuel injected')

    def _init_bang(self):
        print('Bang!!!')

    def _send_signal_to_ignition_system(self):
        print('Ignition starter')
        self._inject_fuel()
        self._init_bang()

    def _send_signal_to_pc(self):
        print('Start')
        self._send_signal_to_ignition_system()

    def start_engine(self):
        self._send_signal_to_pc()

car = Car()
car.start_engine()


# 6) -----protected,  ------private
"""
1. _a,  __a
2. protected - мы еще можем получить скрытые данные
3. protected - данные наследуются в дочках
"""

class A:
    def __say_hello(self):  # private
        print('Hello, makers!!')

class B(A):
    pass

b = B()
b.__say_hello()   # AttributeError

#-------------------------------------------

class A:
    def _say_hello(self):  # protected
        print('Hello, makers!!')

class B(A):
    pass

b = B()
b._say_hello()   # наследуется у дочки