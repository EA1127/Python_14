# Task 1 - map()
# numbers = [-2, -1, 0, 1, 2]
# abs_values = list(map(abs, numbers))
# print(abs_values)


# Task 2
# words = ['welcome', 'to', 'Python', '14']
# len_words = list(map(len, words))
# print(len_words)


# Task 3
# first_it = [1, 2, 3]
# second_it = [4, 5, 6]
# third_it = [1, 1, 1]

# new_list = list(map(pow, first_it, second_it, third_it))
# print(new_list)


# Task 4
# def starts_with_A(word):
#     return word[0] == 'A'

# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# A_fruits = list(map(starts_with_A, fruits))
# print(A_fruits)
# print(A_fruits.count(True))

# F_fruits = list(filter(starts_with_A, fruits))
# print(F_fruits)


# Task 4.1
# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# # new_fruits = list(filter(lambda x: x[0]!='A', fruits))
# new_fruits = list(filter(lambda x: not x.startswith('A'), fruits))
# print(new_fruits)


# Task 4.2 - это не нужно обычно
# strings = ['john', 'emily', 'atai', 'ulan', 'jannat']
# strings_ = [(lambda x: f'${x}!')(name) for name in strings]
# print(strings_)


# Task 5
# studens = [
#     ('Adilet', 89),
#     ('Gulya', 78),
#     ('Beks', 50),
#     ('Nurs', 49),
#     ('Aibek', 69)
#     ]

# # pass_students = list(filter(lambda x: x[-1] >= 61, studens))
# pass_students = [name[0] for name in studens if name[-1] >= 61]
# print(pass_students)


# Task 6
# from functools import reduce
# def add(x, y):
#     return x + y

# numbers = [6, 7, 1, 90, 33, 45]
# print(reduce(add, numbers))
# print(reduce(add, numbers, 10)) #  с initial number


# Task 7
# students = ['Atai', 'Jannat', 'Ulan']
# groups = ['Python 14', 'JS 13', 'Python Ev.13']
# room = [9, 11, 5]
# result = list(zip(students, groups, room))
# print(result)


# Task 8
code = 'print("Hello World")'
eval(code)

code1 = 'for i in range(10):\n\tprint(i)'
exec(code1)