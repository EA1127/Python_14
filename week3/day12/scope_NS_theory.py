""" Пространство имен"""

#1 built-ins - встроенное пространство имен - содержит все имена встроенных обЬектов

#2 global -глобальное пространство имен - содержит все имена опеределенные на уровне основной программы
#3 local - локальное пространство имен - содержится внутри функции def
#4 enclosed - замкнутое пространство имен - пространство между глобальным и локальным


""" Область видимости переменной """
# функции:

# locals() - возвращает словарь локального пространства имен
# globals() - возвращает словарь глобального пространства имен

# this_var_is_visible = 'You can see me inside and outside the function'
# def var_visibility():
#     this_var_is_not_visible = 'You can see me only inside the function'
#     print(this_var_is_not_visible)

# print(this_var_is_visible)
# var_visibility()

""" 1) built-ins """
# print(dir(__builtins__))

# name = "Makers"
# name = "Bootcamp"
# print(name)

# word = "I'm global"
# def func_a():
#     word = "I'm local"
#     print(word)

# func_a()
# print(word)

""" 2) enclosed """
# word = "I'm global"

# def outer():
#     word = "I'm enclosed"
#     print(word)

#     def inner():
#         word = "I'm local"
#         print(word)

#     inner()

# outer()
# print(word)

""" 3) globals(), locals() """

# name = "Makers"
# name = "Bootcamp"
# name2 = "Boot"
# print(name)
# print(globals())


# def func(company):
#     name = 'Bootcamp'
#     # name2 = 'it school'
#     print(locals())

# func(company = 'Makers')


# def info (name, age, height):
#     name = "Alice"
#     age = 30
#     height = 175
#     print(locals())

# info(name='Carly', age=25, height=170)

# print(globals())
# print(locals())


""" 4) изменение переменной вне области их видимости """
# x = 20
# def func():
#     global x # перезаписали значение x в глобальном пространстве
#     x = 40
#     print(x)
# func()
# print(x)


# y = 30
# def func():
#     globals()['y'] = 50
# func()
# print(y)


# a, b, c = 5, 16, 23
# def func():
#     global a, b, c
#     a = 10
#     b = 2
# func()
# print(a)
# print(b)
# print(c)

def outer():
    name = 'makers'

    def inner():
        # global name # -> globals() ['name']
        nonlocal name
        name = 'bootcamp'
        # print(name)
    inner()
    print(name)

outer()
