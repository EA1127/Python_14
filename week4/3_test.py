# task-1
"""
Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def sum_(x,y):
#     return(x + y)

# sum_(7,8)
# print(sum_(7,8))


# task-2
"""
Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
# def gettype_(x,y):
#     return(type(x), type(y))
# gettype_(7,True)
# print(gettype_(7,8))

# task-3
"""
Напишите функцию, которая принимает список чисел и возвращает их произведение
"""
# a = [1, 2, 3, 4, 5]
# def multiply(a):
#     count = a[0]
#     for i in a:
#         count *= i
#     return(count)
# print(multiply(a))


# task-4
""" Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 лет, Эржану - 21 лет, Чынгызу - 24 лет, Алтынай - 17 лет, Асеме - 16 лет.
Напишите программу которая определяет кого пустить в ночной клуб а кого нет."""

# dict_ = {'Murat': 24, 'Erjan': 21, 'Chyngyz': 24, 'Altynai': 17, 'Asema': 16}
# def age_control(dict_):
#     for key, val in dict_.items():
#         if val >= 17:
#             print(f'{key} you are allowed ')
#         else:
#             print(f'{key} you are NOT allowed ')
    
# age_control(dict_)


# task-5 не решил
"""
Напишите функцию, которая принимает строку и выводит количество гласных, 
согласных букв и остальных символов. Используйте только кириллические символы
"""
# vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', "ё", 'е']
# def count_symbols(word):
#     glas, sogl, other = 0, 0, 0
#     for i in word:
#         if i.isalpha() and i in vowels:
#             glas = glas + 1
#         elif i.isalpha():
#             sogl = sogl + 1
#         else:
#             other = other + 1
#     return f'Количество гласных: {glas}, согласных: {sogl}, остальных символов: {other}'
# print(count_symbols('Мурат супер!'))


# task-6 не решил
"""Дан список из чисел. Проверьте, что все числа больше трёх."""
# list_ = [1, 5, -9, 6, -4]
# result = all(i > 3 for i in list_)
# print(result) # False



# task-7 не решил
"""Дан список из имён. Найдите самое длинное имя из списка функцией reduce."""

# import functools
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = functools.reduce(lambda a,b: a if len(a) > len(b) else b, list_)
# print(result)