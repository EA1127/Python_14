# print(type(4 > 3))

# """ord()"""
# print('makers' > 'bootcamp')
# # ord()
# print(ord('m'))
# print(ord('b'))
# print(ord('M'))

"""chr()"""
# chr()
# print(chr(109))  --> буква 'м'

# print(type(False))
# a = True
# b = False
# print(int(a)) --> 1, True
# print(int(b)) --> 0 or '', [], {}, set(), None, False

# print(bool(3.5))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))

# >, <, <=, >=, ==, !=
# a = 10
# b = 7
# print(a + b > 15) # True
# print(a < 20 - b) # True
# print(a <= b + 3) # True
# print(a != b) # True
# print(a == b) # False
# c = a == b # False
# print(c)

# and, or
# a = 15
# b = 25
# print(a >= 15 and b < 30)
      # True  and  # True = True
# print(a > 15 and b < 30)
      # False and  # True = False
# print(a == 15 or b > 30)
      # True  or  # False = True
# print(a != 15 and b > 30)
      # False or  # False = False

# not
x = 20
# print(not x > 10) # --> not True = False
# print(not x == 10) # --> not False = True


"""Условные операторы if, elif, else"""
"""
if condition is True:
    some code 1
elif condition is True:
    some code 2
else:
    some code 3
"""

# a = 19
# if a > 20:
#     if a > 30:
#         print('a is greater than 30')
#     else:
#         print('a is greater than 20')
#     print('a is greater than 20')
# elif a == 20:
#     print('a is equal to 20')
# else:
#     print('a is less than 20')


# a = 10
# b = 5
# c = 20
   # True    # False
# if a > b and b > c:  # False
#     print('MAKERS')
# else:
#     print('makers')

# if a > b or b > c:  # True
#     print('MAKERS')
# else:
#     print('makers')

# if not (a > b or b > c):  # False
#     print('MAKERS')
# else:
#     print('makers')

# list_ = [11, 42, 64, 59]
 # True (not False)     # True
# if not 20 in list_ and 11 in list_:
#     print('YES')


"""тернарный оператор"""

"""
expression_true if condition else expression_false
"""

# a = True
# print(a if True else False)

# a = "MAKERS"
# b = 10
# print(a if b > 0 else 'makers')

"""
(expression_false, expression_true) [condition]
"""
# a = 10                           # 1 = True
# print(('negative', 'positive') [a >= 0])

"""Nonetype"""
# print(type(None))

# null_variable = None   # False
# not_null_variable = "MAKERS"

# if null_variable is None:
#       print('This is None')
# else:
#       print('This is not None')

# if not null_variable is None:
#       print('This is None')
# else:
#       print('This is not None')

# if not null_variable:
#       print('This is None')
# else:
#       print('This is not None')

# print(id(null_variable))
# print(id(None))
