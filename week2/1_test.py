# """
# 1) Перейдите в домашнюю папку по абсолютному пути (не используя ~)
# """
# # cd

# """
# 2) Объявите 2 переменные. Первой присвойте числовое значение, второй строчное. Размножьте строку при помощи второй переменной.
# """
# x = 7
# y = 'Makers'
# c = x * y
# print(c)

# """
# 3) Объявите три переменные с целочисленными значениями x, y, z. Затем обменяйте их значения в одно действие. 
# Переменной x присвойте значение переменной y. Переменной z присвойте значение переменной x. А переменной у присвойте значение переменной z.
# """
# x = 5
# y = 7
# z = 9
# x,y,z = y,z,x

# """
# 4) Объявите строку и проведите следующие операции:  
#   1)выведите последний символ этой строки.  
#   2)распечатайте последние 2 символа. 
#   3)переверните строку и распечатайте результат.  
#   4)выведите длину объявленной строки.
# """
# string = 'bootcamp'
# print(string[-1])
# print(string[-2:])
# print(string[::-1])
# print(len(string))

# """
# 5) Дана строка "The quick brown fox jumps over the lazy dog", замените все встречающиеся буквы "o" символом "*"
# """
# string = "The quick brown fox jumps over the lazy dog"
# print(string.replace('o', '*'))

# """
# 6)  Даны несколько хэштегов, разделённых символом '#'. Разделите их в отдельные строки. Например: #makers#bootcamp#программирование#it#курсы -> ['makers', 'bootcamp', 'программирование', 'it', 'курсы']
# """
# string = '#makers#bootcamp#программирование#it#курсы'
# print(string[1:].split('#'))

# """
# 7) Запросите у пользователя ввод его имени, фамилии, возраста и города, в котором он проживает. С помощью f-строк выведите краткую информацию о нём, например: "Вас зовут Иван Пупкин, Ваш возраст: 35, Вы проживаете в городе Москва"
# """
# name = input('Введите ваше имя: ')
# last_name = input('Введите вашу фамилию: ')
# age = input('Введите ваш возраст: ')
# city = input('Введите ваш город: ')
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

# """
# 8) Проверить введенное пользователем число на то больше ли это число 5, если больше вывести “True”, меньше “False”.
# """
# num = int(input('Введите число: '))
# if num > 5:
#   print('True')
# else:
#   print('False')

# """
# 9) Проверить введенные пользователем данные, если длина строки больше или равна 5 символам вывести “True”, если меньше 'False'.
# """
# string = input('Введите слово: ')
# if len(string) >= 5:
#   print('True')
# else:
#   print('False')

# """
# 10)  Проверить введенное пользователем число если оно отрицательное то вывести “negative”, 
# если положительное то “positive”, если оно равно 0 то вывести “Zero”
# """
# num = int(input('Введите число: '))
# if num < 0:
#   print('negative')
# elif num > 0:
#   print('positive')
# else:
#   print('Zero')


# """
# 11) Посчитайте возраст собаки в собачьих годах. Введите возраст в человеческих годах, переведите в собачьи и распечатайте. 
# Формула перевода следующая: Первые 2 года жизни равны 10.5 собачьих лет. Далее каждый год равен 4 годам.
# """
# age_human = int(input('Введите возраст человека: '))
# age_in_dog = 2 * (10.5/2) + (age_human - 2) * 4
# if age_human < 2:
#     print(f'Возраст человека в собачьих годах: {10.5/2} лет')
# else:
#     print(f'Возраст человека в собачьих годах: {age_in_dog} лет')


"""12) Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, 
может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на входе четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, 
если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае."""

int_1_1 = int(input("введите число от 1 до 8: "))
int_1_2 = int(input("введите число от 1 до 8: "))
int_2_1 = int(input("введите число от 1 до 8: "))
int_2_2 = int(input("введите число от 1 до 8: "))
if int_1_1 == int_2_1 or int_1_2 == int_2_2:
  print("YES")
else:
  print("NO")