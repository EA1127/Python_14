# Task-1

# class Som:
#     currencies = {
#         'USD': 84.5,
#         'EUR': 101.4,
#         'RUB': 1.06,
#         'KZT': 0.2,
#         'SOM': 1
#     }

#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value*curr1} som and {other.value*curr2} som')
#         return self.value*curr1 + other.value*curr2

#     def __sub__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value*curr1} som and {other.value*curr2} som')
#         return self.value*curr1 - other.value*curr2        

# a = Som(100, 'USD')
# b = Som(25, 'EUR')
# print(a + b)
# print(a - b)

# c = Som(15000, 'RUB')
# d = Som(40000, 'KZT')
# print(c + d)
# print(c - d)

# -------------------------------------------------------------------------

# # Task-2

# class Distance:
#     units_M = {
#         'SM': 0.01,
#         'DM': 0.1,
#         'M': 1,
#         'KM': 1000,
#         'Miles': 1600
#     }

#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit

#     def __gt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 > other.value * dist2

#     def __eq__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 == other.value * dist2

#     def __lt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 < other.value * dist2

# a = Distance(7, 'KM')
# b = Distance(5.8, 'Miles')
# print(a < b)


# -------------------------------------------------------------------------

# Task-3

# class PasswordValidationMixin:

#     def validate_password(self, password):
#         if len(password) >= 8 and not password.isdigit() and not password.isalpha() and not password.islower():
#             self.password = password
#             print("Password created")
#             return True
#         else:
#             print("Invalid password")
#             return False

# class Facebook(PasswordValidationMixin):

#     def __init__(self, username, password):
#         if self.validate_password(password):
#             self.username = username
#             print(f"Facebook account created for {username}!")
#         else:
#             print("Facebook account not created!")

#     def __getattr__(self, attr):
#         print('Сработал GETATTR!!!')
#         return ("Such facebook account wasn't created")

#     def __getattribute__(self, name: str):
#         print('Сработал GETATTRIBUTE!!!')
#         return super().__getattribute__(name)

# user1 = Facebook('jannat', "qwerTy112344")
# print(user1.username)
# print(user1.last_name)
# user1.email = 'jannat@gmail.com'
# print(user1.__dict__)


# -------------------------------------------------------------------------

# Task-4

class Person:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, attr, value):
        if attr == 'password':
            print("Cannot create password")
            return None
        return super().__setattr__(attr, value)
        # self[name] = value

jannat = Person('Jannat')
jannat.name = 'Atai'
jannat.lastname = 'Jannatov'
print(jannat.lastname)
jannat.password = 'qwerty'
print(jannat.password)
