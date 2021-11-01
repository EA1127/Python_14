""" 1 try / except  else / finally"""
"""
try:
    some code 1
except:
    some code 2
else:
    some code 3
finally:
    some code 4
"""


""" 1 """
# ---1---
# try:
#     num1 = int(input('Вводите число: '))
# except:
#     print('Вы ввели не число')

# ---2---
# try:
#     num1 = int(input('Enter 1st number: '))
#     num2 = int(input('Enter 1st number: '))
#     result = num1 / num2
# except Exception as e:               
#     print(e)
#     print(type(e).__name__)
# except ZeroDivisionError:
#     print('Cant be divided by zero!')
# except ValueError:
#     print('You entered NOT number!')
# else:
#     print(result)
# finally:
#     print('Program is finished')


# ---3---
# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key,val in dict_.items()}
# dict_.update({'except': 'Exception'})
# print(dict_)

# while True:
#     try:
#         key = input('Enter word: ')
#         if key == 'exit':
#             break
#         dict_[key] += 2
#     except (KeyError, TypeError):
#         print('There is NO such key in dictionary or you cant concatуnate strings with nums!')
#         print()
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)

# --- 4 ---

# list_ = [i for i in range(1, 31)]
# try:
#     index = int(input())
#     list_[index] = 'Makers'
# except (IndexError):
#     print('You are out of list range')
# except (ValueError):
#     print('You entered Not number')
# else:
#     print('There is no exception')
# finally:
#     print(list_)


# --- 5 ---
# try:
#     print(makers)
# except NameError:
#     print('You have not create variable -> makers')


""" генерация исключений"""
# raise

# --- 6 ---
# number = int(input('Enter number in range 1-70: '))
# if not number in range(1, 71):
#     raise Exception('You entered number out of range!')
# print('Okey')