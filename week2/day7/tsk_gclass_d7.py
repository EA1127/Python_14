# Task 1

# okroshka = {'картофель', 'яйца', 'огурцы', 'колбаса', 'зелень'}
# olivie = {'картофель', 'cсоленые огурцы', 'колбаса', 'морковь', 'яйца'}

# print(okroshka.intersection(olivie))
# common = len(okroshka.intersection(olivie))
# print(common)

# unique_okroshka = okroshka.difference(olivie)
# print(unique_okroshka)

# unique_olivie = olivie.difference(okroshka)
# print(unique_olivie)


# Task 2

# users = {
#     ('Alice', 'Python', 3),
#     ('Jack', 'JavaScript', 4),
#     ('Alice', 'JavaScript', 1),
#     ('Bill', 'JavaScript', 2),
#     ('Mark', 'Python', 5)
#     }

# countPython = 0
# countJavaScript = 0
# setPython = set()
# setJS = set()
# for info in users:
#     countPython += info.count('Python')
#     countJavaScript += info.count('JavaScript')

#     if info[1] == 'Python':
#         setPython.add(info[0])
#     else:
#         setJS.add(info[0])
# print(setPython)
# print(setJS)
# print(f'Python изучают {countPython} человек')
# print(f'JavaScript изучают {countJavaScript} человек')
# print(f'{list(setPython & setJS)[0]} изучает оба языка программирования')


# Task 3

# while True:
#     currency = input('Введите валюту (сом или доллар): ')
#     amount = int(input(f'Введите сумму, которую вы хотите конвертировать в {currency}ы: '))

#     if currency == 'доллар':
#         result = amount / 84.5
#         print(f'{round(result, 1)} $')
#     elif currency == 'сом':
#         result = amount * 84.5
#         print(f'{round(result, 1)} сом')
#     else:
#         print('Введите правильные данные')
#         continue
#     choose = input('Хотите продолжить?: ')
#     if choose.lower() == 'да':
#         continue
#     else:
#         print('Всего хорошего!')
#         break



