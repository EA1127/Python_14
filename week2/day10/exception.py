# 1
# products = {
#     'milk': 2,
#     'bread': 1,
#     'eggs': 20,
#     'potato': 35
# }
# while products:
#     item = input('Enter product: ')
#     try:
#         products.pop(item)
#     except KeyError:
#         print('There is no such item!!!')
#     finally:
#         print(products)
# else:
#     print('Products is empty')


# 2
# gallery = []
# try:
#     memory = int(input('Choose memory size: !'))
# except ValueError:
#     print('Enter number not a symbol')
# else:
#     while memory:
#         photo = input('Enter photo: ')
#         gallery.append(photo)
#         memory -= 1
#     else:
#         print(gallery)
#         raise MemoryError('Your gallery is full!!!')


# 3
# kurs = {
#     'buy': {
#         'dollar': 84.50,
#         'euro': 101.25,
#         'ruble': 1.16
#     },
#     'sell': {
#         'dollar': 84.90,
#         'euro': 102.10,
#         'ruble': 1.30
#     }
# }

# while True:
#     try:
#         operation = input('Choose operation: (buy, sell): ').lower()
#         data = kurs[operation]
#         # print(data)
#     except KeyError:
#         print('Enter correct operation: ')
#         continue
#     else:
#         currency = input('Choose (dollar, euro, ruble): ')
#         try:
#             rate = data[currency]
#             # print(rate)
#             summa = int(input('Amount to convert?: '))
#             if operation == 'buy':
#                 result = summa * rate
#                 print(f'Your exchange {round(result, 2)} soms')
#             else:
#                 result = summa / rate
#                 print(f'Your exchange {round(result, 2)} {currency}')
#             if summa <= 0:
#                 raise ValueError
#         except ValueError:
#             print('Enter correct amount')
#         except KeyError:
#             print('Enter correct currency')
#         else:
#             end = input('Do want any convertation?: ').lower()
#             if end == 'y' or end == 'yes':
#                 continue
#             else:
#                 print('Thank you! Good bye!')
#                 break


# 4
# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
# except Exception:
#     print("Общее исключение")
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# print("Завершение программы")