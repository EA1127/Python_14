# task-1

# class Class1:
    
#     def __init__(self): 
#         pass
    
#     def first(self):
#         pass
    
#     def second(self):
#         pass
    
# class Class2(Class1):
    
#     def third(self):
#         pass
    
#     def fourth(self):
#         pass
    
# obj = Class2()

# obj.first()
# obj.second()
# obj.third()
# obj.fourth() 

#-------------------------------------------------------------------------

# task-2

# class A:
    
#     def method1(self):
#         print('Основной функционал') 
        
# class B(A):
    
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')
        
# obj = B()
# obj.method1()

#-------------------------------------------------------------------------

# task-3

# class MyString(str):
    
#     def __init__(self, string):
#         self.string = string
        
#     def __str__(self):
#         return self.string
        
#     def append(self, plused):
#         self.string = f'{self.string}{plused}'
        
#     def pop(self):
#         list_string = list(self.string)
#         string_pop = list_string.pop()
#         self.string = ''.join(list_string)
#         return string_pop

# example = MyString('String') 
# example.append('hello') 
# print(example) 
# print(example.pop())
# print(example)


# # a = 'hello'
# # a = a.split()
# # a.append('world')
# # print(a)


#-------------------------------------------------------------------------

# task-4

# class MyDict(dict):

#     def get(self, object):
#         if super().get(object) == None:
#             return "Are you kidding?"
#         else:
#             return super().get(object)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some_title'))


#-------------------------------------------------------------------------

# task-5

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')

# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# obj_student = Student('Rick', 21, 'science')

# obj_student.display() 
# obj_student.display_student() 


#-------------------------------------------------------------------------

# task-6

# class ContactList(list):
    
    
#     def __init__(self, sum_list):
#         self.list_ = sum_list
        
#     def search_by_name(self, name):
#         for_return = []
#         for name_ in self.list_:
#             if name in name_:
#                 for_return.append(name_)
#         return for_return
        
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

#-------------------------------------------------------------------------

# task-7 NOT PASSAED!!!

# class SmartPhones():
    
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
        
#     def __str__(self):
#         return f'{self.name} {self.memory}'
        
#     def charge(self, charged):
#         self.battery = self.battery + charged

# class Iphone(SmartPhones):
    
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios
    
#     def send_imessage(self, text):
#         return f'sending {text} from {self}'

# class Samsung(SmartPhones):
    
#     def __init__(self, name, color, memory, android):
#         super().__init__(name,color,memory)
#         self.android = android
        
#     def show_time(self):
#         from datetime import datetime
#         return datetime.now().time()
#         return '18:37:02.712036'
        
# phone = SmartPhones('generic', 'blue', '128GB') 

# print(phone)
# print(phone.battery)
# phone.charge(20) 
# print(phone.battery)

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

# -------------------------------------------------------------------------

# task-8  NOT PASSED!!

# class CustomError(Exception):

#     def __init__(self, my_exception):
#         self.my_exception = my_exception

# capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")

# def check_letters(string_):
#     if string_.isupper() == False:
#         raise capitals_error
#     else:
#         return f"ВСЕ ОТЛИЧНО! {string_}"

# print(check_letters("HELLO"))
# print(check_letters("hello"))


