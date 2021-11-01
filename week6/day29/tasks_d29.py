# task-1

# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан')
#     def __repr__(self):
#         return f'{self.name} {self.balance}'
    
#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print('Пока')
        
# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account))

#-------------------------------------------------------------------

# task-2

# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         return f'Это сложение и результат равен: {self.value + other}'

    
#     def __sub__(self, other):
#         return f'Это вычитание и результат равен: {self.value - other}'

    
#     def __mul__(self, other):
#         return f'Это умножение и результат равен: {self.value * other}'

    
#     def __truediv__(self, other):
#         return f'Это деление и результат равен: {self.value / other}'


# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)

#-------------------------------------------------------------------

# task-3

# class MyList(list):
#     def __init__(self, mylist):
#         self.mylist = mylist
        
#     def __getitem__(self, index):
#         return self.mylist[index-1]
        
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])

#-------------------------------------------------------------------

# task-4

# class  Student:

#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball

#     def __lt__(self, other):
#         return f'< {sum(self.ball.values())/len(self.ball) < sum(other.ball.values())/len(other.ball)}'
#     def __gt__(self, other):
#         return f'> {sum(self.ball.values())/len(self.ball) > sum(other.ball.values())/len(other.ball)}'
#     def __le__(self, other):
#         return f'<= {sum(self.ball.values())/len(self.ball) <= sum(other.ball.values())/len(other.ball)}'
#     def __ge__(self, other):
#         return f'>= {sum(self.ball.values())/len(self.ball) >= sum(other.ball.values())/len(other.ball)}'
    
    
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)

#-------------------------------------------------------------------

# task-5

# class Word(object):
    
#     def __new__(cls, word):
#         instance = super().__new__(cls)
#         instance.word = word.replace(' ', '')
#         # print(instance)
#         # print(instance.word)
#         return instance
        
#     def __init__(self, *word):
#         self.str = self.word
#         self.len = len(self.word)

#     def __gt__(self, other):
#         return self.len > other.len

#     def __lt__(self, other):
#         return self.len < other.len

#     def __ge__(self, other):
#         return self.len >= other.len

#     def __le__(self, other):
#         return self.len <= other.len
        
# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2)


#-------------------------------------------------------------------

# task-6   my version!!!

# class Kopilka(list):
    
#     def __init__(self):
#         self.__total = 0
#         self.__coins = []

#     def add_moneta(self, moneta):
#         self.moneta = moneta
#         self.__total += moneta
#         self.__coins.append(moneta)
#         return self.__coins

#     def __len__(self):
#         return len(self.__coins)

#     def __getitem__(self, key):
#         return self.__coins[key]

#     def __str__(self):
#         return str(self.__coins)

# obj = Kopilka()
# obj.add_moneta(25)
# obj.add_moneta(30)
# # print(obj)
# print(len(obj))

# for i in obj:
#     print(i)

#------------------------------------------------------

# from ilgiz

# class Kopilka:
    
#     def __init__(self):
#         self.__total = 0
#         self.__coins = []

#     def add_moneta(self, moneta):
#         self.__total += moneta
#         self.__coins.append(moneta)
        
#     def __len__(self):
#         return len(self.__coins)

#     def __getitem__(self, key):
#         return self.__coins[key]
       
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)

# print(len(obj)) 
# for i in obj: 
#     print(i)


#-------------------------------------------------------------------

# task-7  NOT DONE!!!

"""
Создайте класс Anagram который наследуется от класса str.

Переопределите магический метод отвечающий за сравнение так чтобы, 
знак == сравнивал объекты класса, строки, на то являются ли они анаграммами или нет.

Также переопределите магический метод с помощью которого можно размножить строки:
 2 * "hello" обычно возвращает "hellohello", сделайте так чтобы результат возвращался 
 в обратном порядке как: "olleholleh"

Создайте экземпляры класса в переменных word1 и word2, 
сравните их оператором == и размножьте word1 на 3.

Ввод должен быть:

word1 = Anagram('hello') 
word2 = Anagram('olleh') 
print(word1 == word2) 
print(word1 * 3) 

Вывод:

True 
olleholleholleh

"""