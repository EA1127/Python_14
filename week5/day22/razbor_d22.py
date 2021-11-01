""" 1 Напишите декоратор repeat, который принимает как именованный аргумент num целое число 
(количество выполнения декорированной функции) и запускает декорированную функции указанное количество раз.

Например
```python
@repeat(num=4)
def function(name):
    print(f"{name}")

При вызове function("Python"), вывод должен выглядеть так:
Python
Python
Python
Python
"""

# ______________________________________________________________________________


""" 2 Напишите декоратор countdown, который принимает параметр seconds и отсчитывает секунды до запуска декорированной функции.

Например:
```python
@countdown(seconds=5)
def func():
    print('Hello world')
```
#вывод
5
4
3
2
1
Hello world!
"""

#__________________________________________________________________________________

# Task - 3

# def title(func):
#     def wrapper(name):
#         name = func(name)
#         return name.title()
#     return wrapper

# def chek_symbols(func):
#     def wrapper(name):
#         name_l = list(func(name))
#         # symbols_l = list('1234567890!@#$%^&*()_-+=?/<>:"}{|[]')
#         # name_l = [letter for letter in name_l if not letter in symbols_l]
#         name_l = [letter for letter in name_l if letter.isalpha()]
#         print(name_l)
#         name = ''.join(name_l)
#         return name
#     return wrapper

# @title
# @chek_symbols
# def get_name(name):
#     return name

# print(get_name('@#$riHanNa897%^&*()')) # Rihanna


#__________________________________________________________________________________

# Task - 4

def main(iters: int) -> int:
    def actual_decorator(func):
        def wrapper(*args):
            print('Верхняя булочка')
            print('Помидоры')
            for _ in range(iters):
                print('Котлета')
            func(*args)
            print('Кетчуп')
            print('Салат')
            print('Нижняя булочка')
        return wrapper
    return actual_decorator

customer_choice = int(input('Сколько котлет к бургеру желаете?: '))

@main(iters=customer_choice)
def get_info(*extra_adds):
    if extra_adds:
        # print(extra_adds)
        for adds in extra_adds:
            print(adds)

ingredients = input('Какие дополнительные добавки желаете?\
(перечислите через пробел): ').split()

get_info(*ingredients)