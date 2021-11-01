# task-1

# class Product:
#     base_price = 20000
    
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color


#     def has_garantiya(self, year):
#         if year - self.year > 2:
#             return 'Ваша гарантия истекла'
#         else:
#             return 'Гарантия действительна'

#     @classmethod
#     def change_price(cls, rate):
#         Product.base_price = Product.base_price * rate

# obj = Product('A218', 2008, 'Red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 

# -------------------------------------------

# task-2

# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(email):
#         if '@' in email:
#             return True
#         return False
        
#     def __str__(self):
#         if self.validate_email(self.email):
#             return f'{self.name}:{self.email}'
#         return 'email в неправильном формате'

#     @classmethod
#     def create_user(cls, user_info: str):
#         name, lastname, email = user_info.split(',')
#         # print(user_info.split(','))
#         return cls(name, lastname, email)

# user1 = User.create_user('John,Snow,john@email.com')
# user2 = User.create_user('John,Snow,johnemail.com')

# print(user1) 
# print(user2)


# -------------------------------------------

# task-3

# class Makers:
#     student_count = 0
#     def __init__(self,name,language,kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi
        
#     @classmethod
#     def new_student(cls,name,language,kpi):
#         Makers.student_count+=1
#         return cls(name,language,kpi)        
    
#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'
        
#     def set_kpi(self,k):
#         self.kpi = k
#         return self.kpi
        
# student1 = Makers.new_student('Vlad', 'Python', 77)
# student2 = Makers.new_student('Malik', 'JavaScript', 67)

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)

# -------------------------------------------

# task-4

# class Bike:

#     def __init__(self, cost, make, model, year, min_profit):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self._sale_price = None
#         self.year = year
#         self.sold = False
#         self.min_profit = min_profit

#     def set_cost(self, _price):
#         if _price > self.cost:
#             self._sale_price = _price
#         else:
#             self._sale_price = _price + self.min_profit
#         return self._sale_price

#     def service(self, repair_cost):
#         self._sale_price += repair_cost
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         return self.cost - self._sale_price
    
#     # def __str__(self):
#     #     return f'{self.cost}, {self.make}, {self.model}, {self.year}, {self.min_profit}'

#     @classmethod
#     def get_default_bike(cls):
#         cost = 10000
#         make = 'Author'
#         model = 'Basic ASL'
#         year = 2020
#         min_profit = 2000
#         return cls(cost,make,model,year,min_profit)

# bike = Bike.get_default_bike()
# # print(bike)

# bike.set_cost(6000)
# bike.service(300)

# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit)

    
# -------------------------------------------
"""
Задание 5

Создайте класс MoneyFmt, экземпляры класса должны иметь один единственный атрибут amount.
 Создайте static метод dollarize, который принимает дробное число float в переменную float_num и 
 переводит его в долларизованный формат, то есть:

dollarize(123456.78901) --> "$123,456.80"

dollarize(-123456.7801) --> "-$123,456.78"

dollarize(1000000) --> "$1,000,000"

Класс должен содержать 5 метода:

__init__ - инициализирует значение атрибута amount
update - задаёт объекту новое значение amount
__repr__ - возвращает значение float
dollarize - статический метод
__str__ - метод, который использует метод dollarize()

Создайте обьект cash класса MoneyFmt.

Ввод у вас должен быть:

cash = MoneyFmt(12345678.021) 
print(cash) 
cash.update(100000.4567) 
print(cash) 
cash.update(-0.3) 
print(cash) 
print(repr(cash)) 
Вывод:

$12,345,678.02 
$100,000.46 
-$0.30 
-0.3 

"""
# task-5 

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount

#     def update(self, new_amount):
#         self.amount = new_amount

#     def __repr__(self):
#         return f'{self.amount}'

#     @staticmethod
#     def dollarize(float_num):
#         if float_num >= 0:
#             return '${:,.2f}'.format(float_num)
#         else:
#             return '-${:,.2f}'.format(-float_num)

#     def __str__(self):
#         return self.dollarize(self.amount)


# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))







    

    




