"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""

class Clock:

    def current_time(self):
        from datetime import datetime
        time_ = datetime.now().strftime("%H:%M:%S")
        print(time_)
    
class Alarm:

    def on(self):
        print('just on')

    def off(self):
        print('just off')

class AlarmClock(Clock, Alarm):

    def alarm_on(self):
        print('Alarm is turned on!!!')

clock1 = AlarmClock()

clock1.current_time() 
clock1.alarm_on()
clock1.on()
clock1.off()

print()

"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""
class  Student:

    def __init__(self, name, class_, point):
        self.name = name
        self.class_ = class_
        self.point = point

    def __lt__(self, other):
        return f'{sum(self.point.values())/len(self.point) < sum(other.point.values())/len(other.point)}'

    def __gt__(self, other):
        return f'{sum(self.point.values())/len(self.point) > sum(other.point.values())/len(other.point)}'

    def __le__(self, other):
        return f'{sum(self.point.values())/len(self.point) <= sum(other.point.values())/len(other.point)}'

    def __ge__(self, other):
        return f'{sum(self.point.values())/len(self.point) >= sum(other.point.values())/len(other.point)}'
    
student1 = Student('Emil', 'A', {'math': 100, 'history': 89, 'literature': 88})
student2 = Student('John', 'B', {'math': 100, 'history': 90, 'literature': 85})
print(student1 > student2)
print(student1 < student2)
print(student1 >= student2)
print(student1 <= student2)

print()
"""

3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.

"""
class Makers:

    student_count = 0

    def __init__(self, name, language):
        self.name = name
        self.language = language
        
    def __str__(self):
        return f'{self.name}, {self.language}, {self.kpi}'

    @classmethod
    def add_new_student(cls, name, language):
        cls.student_count += 1
        return cls(name, language)

    def show_info(self):
        return f"Student name: {self.name}, Language: {self.language}"

    def add_kpi(self, kpi):
        self.kpi = kpi
        return self.kpi

student1 = Makers.add_new_student('Emil', 'Python')
student2 = Makers.add_new_student('John', 'JavaScript')
student3 = Makers.add_new_student('Tony_Stark', 'CSharp')

print(student1.add_kpi(90))
print(student2.add_kpi(85))
print(student3.add_kpi(100))

print(student1.show_info())
print(student2.show_info())
print(student3.show_info())

print(student1)
print(student2)
print(student3)

print(Makers.student_count)

print()

"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, new_amount):
        self.amount = new_amount

    def __repr__(self):
        return f'{self.amount}'

    @staticmethod
    def dollarize(float_num):
        if float_num >= 0:
            return '${:,.2f}'.format(float_num)
        else:
            return '-${:,.2f}'.format(-float_num)

    def __str__(self):
        return self.dollarize(self.amount)


cash = MoneyFmt(12345678.021) 
print(cash) 
cash.update(100000.4567) 
print(cash) 
cash.update(-0.3) 
print(cash) 
print(repr(cash))
































































































































































































































































































































































































































































































