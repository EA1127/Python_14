"""
1) Напишите декоратор, который печатает перед вызовом полученной функции строку: 
"Вызываю функцию <имя_функции>". Затем следует вызов функции. 
После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""
# def my_decorator(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return wrapper
    
# @my_decorator   
# def first():
#     print('hello')
# first()


"""
2) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, 
и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. 
Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, 
переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#     pi = 3.14
#     color = 'green'

#     def __init__(self, radius):
#         self.radius = radius

#     def get_sqr(self):
#         return Circle.pi * (self.radius**2)

# circle1 = Circle(2)
# circle1.color = 'yellow'
# print(circle1.color)
# print(circle1.get_sqr())
        

"""
3) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. 
Также создайте метод get_info, который выводит информацию о контакте в следующем виде: 
"Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

# class Contact_book():
#     def __init__(self, name, last_name, phone_number):
#         self.name = name
#         self.last_name = last_name
#         self.phone_number = phone_number

#     def get_info(self):
#         return f"Контакт: {self.name} {self.last_name}, телефон: {self.phone_number}"

# contact1 = Contact_book("Иван", "Петров", "+996555777888")
# print(contact1.get_info())

"""
4) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. 
Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, 
он должен принимать все атрибуты, которые были определены в родительском классе 
и добавьте еще один атрибут, который будет описывать направление студента. 
Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""
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

# obj_student = Student('Emil', 33, 'Programming')

# obj_student.display() 
# obj_student.display_student() 

"""
5) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", 
для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), 
которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:

#     def voice(self):
#         voice = 'Гав'
#         return voice
    
# class Cat:

#     def voice(self):
#         voice = 'Мяу'
#         return voice

# animal1 = Dog()
# animal2 = Cat()

# def to_pet(animal):
#     print(animal.voice())
#     return animal.voice()

# to_pet(animal2)



"""
Дополнительно

1)

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

# class Solution(object):
#     def isPalindrome(self, x):
#         x = x.lower()
#         if x == x[::-1]:
#             print(True)
#         else:
#             print(False)
# num = Solution()
# num.isPalindrome(str(121))
# num.isPalindrome('Civic')


"""
2)

Учитывая целочисленный массив nums и целое число val, удалите все вхождения val в nums на месте. 
Относительный порядок элементов может быть изменен.

Поскольку на некоторых языках невозможно изменить длину массива, вы должны вместо этого поместить 
результат в первую часть номеров массива. Более формально, если после удаления дубликатов остается 
k элементов, то первые k элементов числа nums должны содержать окончательный результат. Неважно, 
что вы оставите за пределами первых k элементов.

Верните k после помещения окончательного результата в первые k слотов с числами.

Не выделяйте лишнее место для другого массива. Вы должны сделать это, изменив входной массив 
на месте с дополнительной памятью O (1).

Пользовательский судья:

Судья проверит ваше решение с помощью следующего кода:

int [] nums = [...]; // Входной массив
int val = ...; // Значение для удаления
int [] expectedNums = [...]; // Ожидаемый ответ правильной длины.
                            // Сортировка без значений, равных val.

int k = removeElement (числа, значение); // Вызывает вашу реализацию

assert k == expectedNums.length;
sort (числа, 0, k); // Сортируем первые k элементов числа
for (int i = 0; i <actualLength; i ++) {
    утверждать числа [я] == ожидаемое число [я];
}
Если все утверждения пройдут, ваше решение будет принято.

 

Пример 1:

Ввод: nums = [3,2,2,3], val = 3
Вывод: 2, число = [2,2, _, _]
Объяснение: Ваша функция должна вернуть k = 2, причем первые два элемента nums равны 2.
Неважно, что вы оставите после возвращенного k (следовательно, они являются подчеркиванием).
Пример 2:

Ввод: nums = [0,1,2,2,3,0,4,2], val = 2
Вывод: 5, число = [0,1,4,0,3, _, _, _]
Объяснение: Ваша функция должна возвращать k = 5, причем первые пять элементов числа содержат 0, 0, 1, 3 и 4.
Обратите внимание, что пять элементов могут быть возвращены в любом порядке.
Неважно, что вы оставите после возвращенного k (следовательно, они являются подчеркиванием).
 

Ограничения:

0 <= nums.length <= 100
0 <= nums [i] <= 50



https://leetcode.com/problems/remove-element/
"""

class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
            else:
                nums[i] = "_"
            count += 1

        return count-1, nums

num1 = Solution()
print(num1.removeElement([3, 2, 2, 3], 3))