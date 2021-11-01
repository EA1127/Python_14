# task-1 не прошел!!!

# class Song:

#     def __init__(self, author, title, year):
#         self.author = author
#         self.title = title
#         self.year = year

#     def show_author(self):
#         print(f'Автор этой песни {self.author}')
        
#     def show_title(self):
#         print(f'Название этой песни {self.title}')

#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')

# song = Song(author='Adel', title='Hello', year=2015)
# song.show_author()
# song.show_title()
# song.show_year()

#------------------------------------------------------------------

# task-2

# class Circle:
#     color = 'Синий'
#     pi = 3.14
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         return self.radius**2*Circle.pi

# circle = Circle(2)
# circle.color = 'Красный'
# print(circle.get_area())
# print(circle.color)
# # print(isinstance(circle, Circle))

#------------------------------------------------------------------

# task-3

# class BankAccount:
    
#     def __init__(self):
#         self.balance = 0
       
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
#         return self.balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')
#         return self.balance
        
# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500)

#------------------------------------------------------------------

# task-4

# class Taxi:

#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#         self.km = 0

#     def get_total_cost(self, km):
#         self.km += km
#         return f'Такси {self.name}, стоимость поездки: {self.km * self.cost_km + self.cost} сом'

# taxi1 = Taxi('Namba', 60, 13)
# taxi2 = Taxi('Yandex', 80, 10)
# taxi3 = Taxi('Jorgo', 50, 15)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(10)) 
# print(taxi3.get_total_cost(10))   

#------------------------------------------------------------------

# task-5

# class Phone:

#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")
        
# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()

#------------------------------------------------------------------

# task-6

# class Salary:

#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return (self.salary * Salary.percent * self.experience)/100

# obj = Salary(10000, 10)
# print(obj.count_percent())

#------------------------------------------------------------------

# task-7

# from datetime import date

# class Nobel:

#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         return f'выиграл {date.today().year - self.year} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

#------------------------------------------------------------------

# task-8 NOT PASSED!!!

"""
Создайте класс Password, экземеплярами класса являются пароли в виде строк. 
У класса должен быть метод validate для валидации пароля:

пароль должен быть минимум 8 символов, но меньше 15
пароль должен содержать цифры
пароль должен содержать буквы
пароль должен содержать хотя бы один из символов:
'@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите свое исключение, если же все 
условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.

Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, 
вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал 
должно выводиться: **********
"""

# class Password:
    
#     def __init__(self, password):
#         self.password = password
    
#     def __str__(self):
#         return '*'*len(self.password)

#     def validate(self):
#         list_ = {'@', '#', '&', '$', '%', '!', '~', '*'}
#         if not (len(self.password)>=8 and len(self.password)<15):
#             raise Exception('пароль должен быть минимум 8 символов, но меньше 15')
#         if self.password.isalpha():
#             raise Exception('пароль должен содержать цифры')
#         if self.password.isdigit():
#             raise Exception('пароль должен содержать буквы')
        
#         if not list_&set(self.password):
#             raise Exception("пароль должен содержать хотя бы один из символов:\n'@', '#', '&', '$', '%', '!', '~', '*'")
#         return 'Password has been saved'
    
# passwd1 = Password('joe@123456')
# print(passwd1.validate())
# print(passwd1)
#------------------------------------------------------------------

# task-9 NOT PASSED!!!

"""
Создайте класс Math, экземпляром которого должно быть число. У классa Math должно быть 3 метода:

get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)
get_sum - возвращает сумму цифр числа
get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50

Создайте экземпляр класса и примените к нему все методы.
Например, если экземпляром класса Math является число 11,
вызов get_factorial возвратит такой результат:

39916800 
т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

метод get_sum, возвратит:
2 
т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

метод get_mul_table возвратит:
11 x 1 = 11 
11 x 2 = 22 
11 x 3 = 33 
11 x 4 = 44 
11 x 5 = 55 
11 x 6 = 66 
11 x 7 = 77 
11 x 8 = 88 
11 x 9 = 99 
11 x 10 = 110 
результат методов возвращайте ключевым словом return, print() использовать не надо.

"""
# version-1 NOT PASSED!!!

# import functools
# class Math:
    
#     def __init__(self, num):
#         self.num = num
    
#     def get_factorial(self):
#         return functools.reduce(lambda x,y: x*y, range(1,self.num + 1))

#     def get_sum(self):
#         k = 0
#         for i in str(self.num):
#             k += int(i)
#         return k

#     def get_mul_table(self):
#         count = 1
#         a = ''
#         while count <= 10:
#             a += f"{self.num} x {count} = {self.num * count} \n"
#             count = count + 1
#         return a
       

# num1 = Math(11)
# print(num1.get_factorial())
# print(num1.get_sum())
# print(num1.get_mul_table())


# ILGIZ version-2  Passed
# import functools
# class Math:
    
#     def __init__(self,number):
#         self.number = number
        
#     def get_factorial(self):
#         return functools.reduce(lambda x,y: x*y, range(1,self.number + 1))
    
#     def get_sum(self):
#         k=0
#         for i in str(self.number):
#             k += int(i)
#         return k
    
#     def get_mul_table(self):
#         for i in range(11):
#             return self.number*i
        
#     def get_mul_table(self):
#         list_ = []
#         for i in range(1,11):
#             if i == 1:
#                 list_.append(f'{self.number} x {i} = {i*self.number}')
#             else:
#                 list_.append(f'\n{self.number} x {i} = {i*self.number}')
#         return list_
    
# num = Math(11)
# print(num.get_factorial())
# print(num.get_sum())
# print(*num.get_mul_table())

#------------------------------------------------------------------

# task-10

"""
Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д).
У класса должна быть переменная класса instances значением которой является пустой словарь.

Создайте внутри класса метод give_priority, который имеет параметр priority, куда принимает число - приоритет вашей задачи (1, 2, 3) 
и записывает вашу задачу в словарь instances с ключом в виде числа - priority, а значением в виде вашей задачи.

Например:

{3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

{1: 'сделать домашку'}
в этом случае это у вас самая важная задача, с приоритетом 1.

При каждом вызове метода give_priority - словарь в instances обновляется. Если вы создали три объекта от класса ToDo и к каждому объекту 
вызвали метод give_priority и дали приоритет, то ваш словарь в instances в конце будет выглядеть примерно так:

{3: 'сходить в кино', 1: 'сделать домашку', 2: 'выгулять собаку'} 
У класса должен быть метод list_of_tasks, который возвращает вам список отсортированных задач по приоритету:

[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]
"""

# class ToDo:
    
#     instances = {}
#     def __init__(self, task):
#         self.task = task

#     def give_priority(self, priority):
#         ToDo.instances[priority]  =  self.task
#     @staticmethod
#     def list_of_tasks():
#         list_sort = [i for i in ToDo.instances.keys()]
#         list_sort.sort()
#         return [(i, ToDo.instances.get(i)) for i in list_sort]

# task1 = ToDo('Сходить в кино')
# task2 = ToDo('Сделать домашку')
# task3 = ToDo('Выгулять собаку')
# task1.give_priority(3)
# task2.give_priority(1)
# task3.give_priority(2)
# print(ToDo.list_of_tasks())