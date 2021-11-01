# task 1

# try:
#     some code 1
# except:
#     some code 2
# else:
#     some code 3
# finally:
#     some code 4

# task 2
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Переменная "a" не определена')

# task 3
# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(result)


# task 4
# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(result)


# task 5
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа!')
# else:
#     print(dict_['key3'])

# task 6
# list_ = [1, 4, 9, 16, 25, 36]

# try:
#     print(list_[6])
# except IndexError:
#     print('Нет такого элемента!')
# else:
#     print(list_[6])

# task 7
# как должно быть
# try:
#     age = int(input())
#     if age < 18:
#         raise Exception('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
"""------------------------------------------"""
# пропустило
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# task 8
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')

# task 9
# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)


# Extra task 1

# inp1 = input()
# inp2 = input()
# try:
#     print(int(inp1) + int(inp2))
# except Exception as e:               
#     print(e)
#     print(type(e).__name__)
# except ValueError:
#     print(inp1 + inp2)


# Extra task 2

# try:
#     inp1 = input().split()
#     list_ = []
#     for i in inp1:
#         list_.append(int(i))
# except ValueError:
#     raise Exception ('Данный элемент не является числом!')
# print(list_)

