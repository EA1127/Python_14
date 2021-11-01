# Task-1

class Employee:

    stuff = []

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.id = self.generate_id()
        Employee.stuff.append({
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name
        })

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

    def generate_id(self):
        import random
        id_ = random.randint(500, 1000)
        for worker in Employee.stuff:
            if worker.get('id') == id_:
                return self.generate_id()
        return id_

class BonusMixin:
    def bonus(self, hours):
        if hours > 100:
            self.salary = self.salary * 1.05
        else:
            self.salary = self.salary
        # return self.salary

class SalaryEmployee(Employee):

    def __init__(self, name, last_name, salary):
        super().__init__(name, last_name)
        info = {"id": self.id, 'name': self.name, 'last_name': last_name}
        self.salary = salary
        for worker in Employee.stuff:
            if info == worker:
                worker.update({"salary": self.salary}) 

class HourlyEmployee(Employee, BonusMixin):

    def __init__(self, name, last_name, hours, per_hour):
        super().__init__(name, last_name)
        info = {"id": self.id, 'name': self.name, 'last_name': last_name}
        self.salary = hours * per_hour
        self.bonus(hours)
        for worker in Employee.stuff:
            if info == worker:
                worker.update({"salary": self.salary}) 

john = Employee('John', 'Snow')
emely = Employee('Emely', 'Smith')
jannat = SalaryEmployee('Janat', 'Janatov', 16000)
aikol = HourlyEmployee('Aikol', 'Aikolev', 102, 150)
print(Employee.stuff)
