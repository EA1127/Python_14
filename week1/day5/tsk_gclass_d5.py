""" Task-1 """
# password = input("Enter your password: ")
# if password.isdigit() and len(password) >= 8:
#     print("Your password is saved")
# if not len(password) >= 8:
#     print("Your password must NOT be less than 8 symbols")
# if not password.isdigit():
#     print("Your password must contain only numbers")

# """ Task-2 """
# score = input('Введите свои баллы по математике, английскому языку и литературе через запятую: ').split(', ')
# math = int(score[0])
# english = int(score[1])
# literature = int(score[-1])
# average = (math + english + literature) / 3
# if average > 69:
#     print(f'Вы допущены к экзамену. Ваш средний балл составляет {round(average, 1)}')
# else:
#     print('У вас нет допуска к экзамену')

""" Task-3 """   
# import random 
# play = ['Камень', 'Ножницы', 'Бумага']
# # print(dir(random))
# my_choice = input('Ваш выбор: ')
# comp_choice = random.choice(play)
# print(f'Выбор компьютера: {comp_choice}')
# if my_choice == 'Ножницы' and comp_choice == 'Бумага':
#     print('Вы выиграли!')
# elif my_choice == 'Ножницы' and comp_choice == 'Камень':
#     print('Вы проиграли:(')
# elif my_choice == 'Бумага' and comp_choice == 'Ножницы':
#     print('Вы проиграли:(')
# elif my_choice == 'Бумага' and comp_choice == 'Камень':
#     print('Вы выиграли!')
# elif my_choice == 'Камень' and comp_choice == 'Ножницы':
#     print('Вы выиграли!')
# elif my_choice == 'Камень' and comp_choice == 'Бумага':
#     print('Вы проиграли:(')
# elif (my_choice == 'Ножницы' and comp_choice == 'Ножницы') or (my_choice == 'Бумага' and comp_choice == 'Бумага') or (my_choice == 'Камень' and comp_choice == 'Камень'):
#     print('Ничья')