# Task-1
"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который 
обозначает количество студентов, изучающих какой-либо язык программирования. 
От класса Languages создайте два дочерних класса: Python, JavaScript. 
В них  также должны быть атрибуты, указывающие на количество студентов, изучающих 
тот или иной язык. При создании объекта-студента от одного из дочерних классов, 
автоматически количество студентов в классах меняется. Если студент изучает язык Python, 
то количество студентов должно увеличиться на один и в классе Python и в классе Languages. 
Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен 
метод coding, в классе Python он должен выдавать вам строку “I am Python student. 
I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. 
Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает 
студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, 
он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали 
правильно, пишет “Good job!”, если нет - “No bueno :(”

"""
import random

class Languages:
    student_count = 0

    def __init__(self):
        Languages.student_count += 1

    def coding(self):
        return NotImplementedError

class Python(Languages):
    student_count = 0

    def __init__(self):
        super().__init__()
        Python.student_count += 1

    def __str__(self):
        return 'Python'

    def coding(self):
        print("I am Python student. I am coding now")

class JavaScript(Languages):
    student_count = 0

    def __init__(self):
        super().__init__()
        JavaScript.student_count += 1

    def __str__(self):
        return 'JavaScript'

    def coding(self):
        print("I am JavaScript student. I am coding now")

student1 = Python()
student2 = JavaScript()

my_choice = input("Guess the student's language:\n")
programm_choice = random.choice([student1, student2])

programm_choice.coding()

if programm_choice.__str__() == my_choice:
    print('Good job!!!')
else:
    print('No bueno :(')

student3 = Python()
student1.coding()
student2.coding()
print(Python.student_count)
print(JavaScript.student_count)
print(Languages.student_count)


# Task-2
"""
2) Создайте свой класс MyList, который наследуется от list. 
Переопределите метод списка insert(), который обычно принимает первым аргументом индекс,
а вторым - элемент. В своем классе MyList переопределите этот метод так, чтобы он принимал 
аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""

class MyList(list):

    def insert(self, arg1, arg2):
        print("First arg  element, second arg - index")
        return super().insert(arg2, arg1)

list1 = MyList([1, 2, 3, 4, 5])
list1.insert('Makers', 4)
print(list1)

# list2 = list([1, 2, 3, 4, 5])
# list2.insert(3, "bootcamp")
# print(list2)