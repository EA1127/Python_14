""" 1) Типы данных """
""" 2) Циклы """
""" 3) Условные операторы """
""" 4) Try except """

""" 5) Функции """
# task1
# def get_symbol(*name, **saf):
#     a = 'а, у, о, ы, и, э, я, ю, ё, е, й'
#     glass, soglass, symbol = 0, 0, 0
#     # print(name)
#     for i in name:
#         for m in i:
#             if m in a:
#                 glass += 1
#             elif m.isalpha():
#                 soglass += 1
#             else:
#                 symbol += 1
#     return f"glass - {glass}, soglass - {soglass}, symbol - {symbol}"

# murat = get_symbol('Мурат супер!', 'чай', 'кофе', 'аи')
# print(murat)

# task2
# def momo(name, year):
#     nono = chek_age(year)
#     return f'{name} {nono}'
# def chek_age(age):
#     return 2010 - age
# c = [('Murat', 1997), ('Timur', 1992), ('Tofik', 2000)]
# for n,p in c:
#     a = momo(n, p)
#     print(a)

# task3
# def momo(name, year):
#     if len(name) >= 5:
#         name
#     else:
#         name = "Anonim"
#     l = chek_age(year)
#     return f'{name}, {l}'

# def chek_age(year):
#     g = 2021 - year
#     if g > 18:
#         return "18+"
#     else:
#         return "You are child"

# c = [('Murat', 1997), ('Tim', 1992), ('Tofik', 2007)]
# solo= []
# for n, p in c:
#     f = momo(n,p)
#     solo.append(f)
# print(solo)


""" 6) Работа с файлами """
# with open('text.txt', 'w') as file:
#     file.write('1\n2\n3\n67\n')

# with open('text.txt', 'r') as file1:
#     lines = [int(line.replace('\n', '')) for line in file1.readlines()]
#     max_ = max(lines)
#     min_ = min(lines)
#     print(max_)
#     print(min_)

# with open('text.txt', "r+") as file:
#     lines = file.readlines()
#     # print(lines)
#     lines2 = []
#     for i in lines:
#         lines2.append(int(i.replace('\n', '')))
#     c = sum(lines2)
# with open('text1.txt', 'w') as file:
#     file.write(str(c))

""" 7) Работа с виртуальным окружением """
# 8) Парсинг
