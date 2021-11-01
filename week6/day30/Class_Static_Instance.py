"""" TASK-1 """

class Category:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Category: {self.name}'

iphone = Category('Iphone')
samsung = Category('Samsung')
nokia = Category('Nokia')
xiaomi = Category('Xiaomi')

class Condition:

    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return f'Condition: {self.condition}'

new = Condition('Новый')
used = Condition('Б/У')
repaired = Condition('Отремонтированный')


class Phone:

    def __init__(self, category, model, price, condition):
        self.category = category
        self.model = model
        self.price = price
        self.condition = condition

    @classmethod
    def create_iphone(cls, model, price, condition):
        return cls(
            category = iphone,
            model = model,
            price = price,
            condition = condition
        )
    
    @classmethod
    def create_samsung(cls, model, price, condition):
        return cls(
            category = samsung,
            model = model,
            price = price,
            condition = condition
        )

    @classmethod
    def create_nokia(cls, model, price, condition):
        return cls(
            category = nokia,
            model = model,
            price = price,
            condition = condition
        )

    @classmethod
    def create_xiaomi(cls, model, price, condition):
        return cls(
            category = xiaomi,
            model = model,
            price = price,
            condition = condition
        )

    @property
    def title(self):
        return f"{self.category}, {self.model}, {self.price}, {self.condition}"

    def __repr__(self) -> str:
        return self.title

    @staticmethod
    def sale(percent, price):
        x = price * percent/100
        return x

    def sale_price(self, percent, code):
        sale = self.sale(percent, self.price)
        if code.lower() == "makers":
            self.price -= sale


p1 = Phone.create_iphone('SE', 78000, new)
p2 = Phone.create_iphone('X', 56000, used)
p3 = Phone.create_xiaomi('T10 pro', 28000, repaired)
p4 = Phone.create_nokia('XZ', 20000, used)
p5 = Phone.create_samsung('A-5', 7000, used)

print(p1.title)
p1.sale_price(30, 'Makers')
print(p1.price)
# print(p2)
# print(p3)
# print(p4)
# print(p5)
