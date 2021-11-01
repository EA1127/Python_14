"""
1) Task-1

Создайте свой класс MyUser. В этом классе реализуйте следующие условия:
При инициализации объекта, необходимо передавать аргументы: name, last_name. 
Автоматически программа генерирует вам пароль password, который состоит только 
из гласных букв, входящих в состав атрибутов name и last_name
При вызове самого объекта, возвращаются только первые буквы имени и фамилии, 
остальные буквы скрыты символом *
При попытке получения пароля (при вызове атрибута password) должна выдаваться 
ошибка-сообщение: “Forbidden”
	Например:
	user = MyUser(“Makers”, “Bootcamp”)
	print(user)  ->    M***** B*******
	print(user.password)  ->  Exception: Forbidden
"""

# class MyUser:

#     def _get_vowels(self, name, last_name):
#         vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#         list_of_letter = list(name) + list(last_name)
#         list_of_letter = [letter for letter in list_of_letter if letter in vowels]
#         # print(list_of_letter)
#         result = ''.join(list_of_letter)
#         # print(result)
#         return result

#     def _generate_password(self, name, last_name):
#         password = self._get_vowels(name, last_name)
#         return password

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.password = self._generate_password(name, last_name)

#     def __str__(self):
#         n = self.name[0]
#         l = self.last_name[0]  # ljust(lenght, symbol), rjust(lenght, symbol) - str
#         return f"{n.ljust(len(self.name), '*')} {l.ljust(len(self.last_name), '*')}"

#     def __getattribute__(self, item):
#         if item.lower() == 'password':
#             raise Exception('Forbidden')
#         else:
#             return super().__getattribute__(item)

# user = MyUser(name='Makers', last_name='Bootcamp')
# print(user)
# print(user.password)


"""
2)  Task-2

Создайте класс MyTuple. Создайте объекты от этого класса, они должны быть 
кортежами, в которых элементы - числа. Далее сравните эти кортежи, но сравнение 
должно происходить по сумме чисел в кортежах. Например:
a = (1,2,3,4,5)  - сумма 15
b = (6,7,8)        - сумма 21
print(a == b) -> False
print(a > b) -> False
print(a < b) -> True
print(a != b) -> True

"""
# class MyTuple(tuple):

#     def __init__(self, item):
#         self.tuple = item

#     def __eq__(self, other):
#         return sum(self.tuple) == sum(other)

#     def __gt__(self, other):
#         return sum(self.tuple) > sum(other)

#     def __lt__(self, other):
#         return sum(self.tuple) < sum(other)

#     def __ne__(self, other):
#         return sum(self.tuple) != sum(other)

# a = MyTuple([1,2,3,4,5])   # print(sum(a)) -> 15
# b = MyTuple([6,7,8])       # print(sum(b)) -> 21

# print(a == b)
# print(a > b)
# print(a < b)
# print(a != b)