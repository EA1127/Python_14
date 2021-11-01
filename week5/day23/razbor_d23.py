"""
task - 1) 

Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра. 
Каждому устанавливается здоровье в 100 очков. В случайном порядке они стреляют друг в друга. 
Тот, кто стреляет, здоровья не теряет. У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела. 
После каждого выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья. 
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""

# import random

# class Sniper:

#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def shoot(self, sniper):
#         sniper.health -= 20

# sniper1 = Sniper(name='Ben')
# sniper2 = Sniper(name='Tom')

# choices = (sniper1, sniper2)

# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         target = sniper2
#     else:
#         target = sniper1

#     shooter.shoot(target)
#     print(f'Shooter {shooter.name} is shooting, {target.name} has {target.health} health points')

#     if sniper1.health == 0:
#         print(f'{sniper1.name} is dead, {sniper2.name} wins!')
#         break
#     elif sniper2.health == 0:
#         print(f'{sniper2.name} is dead, {sniper1.name} wins!')
#         break
#     else:
#         continue


"""
task - 2) 

Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты. При создании студентов 
необходимо указать баллы за их следующие качества: courage (храбрость), intelligence (интеллект), justice (справедливость), 
ambition (амбиции). У студентов не могут быть качества одинакового уровня. В зависимости от того, какое качество студента 
преобладает, метод sorting_hat будет распределять студента в один из факультетов и выдавать в какой факультет поступил студент.

Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""

# class Hogwarts:

#     faculties_qualities = {'courage': 'Gryffindor',
#                            'intelligence': 'Ravenclaw',
#                            'justice': 'Hufflepuff',
#                            'ambition': 'Slytherin'}
    
#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#         # locals()
#         self.qualities_dictionary = locals()
#         # print(self.qualities_dictionary)

#     def sorting_hat(self):
#         dictionary = {val: key for key,val in self.qualities_dictionary.items() if type(val) == int}
#         # print(dictionary)
#         maximum_point = max(dictionary.keys())
#         # print(maximum_point)
#         maximum_quality = dictionary[maximum_point]
#         # print(maximum_quality)
#         self.faculty = Hogwarts.faculties_qualities[maximum_quality]
#         print(f'{self.faculty}!!!')


# student1 = Hogwarts(courage=5, intelligence=8, justice=3, ambition=9)
# student1.sorting_hat()

# student2 = Hogwarts(courage=8, intelligence=6, justice=1, ambition=1)
# student2.sorting_hat()

# student3 = Hogwarts(courage=4, intelligence=7, justice=3, ambition=2)
# student3.sorting_hat()

# student4 = Hogwarts(courage=4, intelligence=5, justice=8, ambition=0)
# student4.sorting_hat()