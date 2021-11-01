# task-1

# class A:

#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'


# obj1 = A()

# print(obj1.public())
# # print(obj1._protected())
# # print(obj1.__private())

# --------------------------------------------


# task-2

# class A:
#     def method1(self):
#         return 'Hello World'
        
# class B(A):
#     def method1(self):
#         return super().method1()
    
# b1 = B()
# print(b1.method1())

# --------------------------------------------


# task-3

# class Car: 
    
#     def __init__(self): 
#         self.__speed = 0

#     def show_speed(self):
#         return self.__speed
    
#     def set_speed(self, new): 
#         self.__speed = new 
    
  
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20)
# print(car1.show_speed())

# car1.set_speed(35)
# print(car1.show_speed())

# --------------------------------------------


# task-4

# class Car: 
    
#     def __init__(self): 
#         self.__speed = 0

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, new): 
#         self.__speed = new 
    
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20
# print(car1.speed) 
