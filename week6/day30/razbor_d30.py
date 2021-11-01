"""
1) Создайте класс Passport, в котором есть следующие атрибуты:
Атрибут класса users_images, в котором хранится пустой список, и атрибут класса 
black_list - тоже пустой список

Атрибуты экземпляра класса при инициализации объекта: 
name, last_name, date_of_birth, image, INN (INN при создании объекта равен None)

Метод check_dublicate_person, который при вызове через созданный объект класса, 
заносит атрибут данного объекта image в список users_image, если такой фотографии еще нет, 
если же она уже есть, т.е. если человек с такой фотографией уже есть в нашей “базе данных”, 
то этот объект-человек, через который мы вызвали данный метод, заносится в черный список. 

Также есть метод get_inn, который выдает сгенерированный INN для объекта. 
INN должен содержать какое-то число от 1999999-19999999. Но если объект находится 
в черном списке, то метод get_inn выдает сообщение: “Для объекта черного списка INN 
не генерируется”

По надобности переопределите методы __str__ или __repr__.

Создайте объекты от класса Passport и вызовите у каждого объекта метод 
check_dublicate_person и метод get_inn. 

Также проверьте черный список и users_images. 
"""

class Passport:
    users_images = []
    black_list = []

    def __init__(self, name, last_name, date_of_birth, image):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.image = image
        self.INN = None

    def __repr__(self):
        return f"{self.name} {self.last_name}"

    def check_dublicate_person(self):
        if self.image in self.__class__.users_images:
            self.__class__.black_list.append(self)
        else:
            self.__class__.users_images.append(self.image)

    @staticmethod
    def _generate_inn():
        import random
        return random.randrange(1999999, 19999999)

    def get_inn(self):
        if not self in self.__class__.black_list:
            self.INN = self._generate_inn()
            return f"{self.name} - {self.INN}"
        else:
            return 'Для объекта черного списка INN не генерируется'


person1 = Passport('John', 'Snow', '12/12/1990', 'john.jpg')
person2 = Passport('Emily', 'White', '10/12/1990', 'emily.jpg')
person3 = Passport('Karen', 'Green', '11/07/1992', 'karen.jpg')
person4 = Passport('Emi', 'White', '1/12/1990', 'emily.jpg')
person5 = Passport('john', 'snow', '12/12/1990', 'john.jpg')
person6 = Passport('Bill', 'Brown', '17/08/1989', 'bill.jpg')
person7 = Passport('caren', 'Green', '11/07/1992', 'karen.jpg')

for person in [person1, person2, person3, person4, person5, person6, person7]:
    person.check_dublicate_person()
    print(person.get_inn())

print(Passport.users_images)
print(Passport.black_list)
print(person3.INN)