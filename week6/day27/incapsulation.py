# -- 1 --

# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self, name):
#         response = input(f"{name} wants to know your salary: ").lower()
#         if response == 'yes':
#             return self.__salary
#         return 'I will not tell him!'

#     def set_salary(self, new_salary):
#         self.__salary = new_salary

# person1 = Person('Jannet', 100000)
# # person1.__salary = 20000
# # print(person1.__salary)
# print(person1.get_salary('Ulan'))
# person1.set_salary(200000)
# print(person1.get_salary('Atai'))

#----------------------------------------------------

# -- 2 --

# class Person:
#     def __init__(self, name, hours, per_hour):
#         self.name = name
#         self.hours = hours
#         self._per_hour = per_hour

#     # @staticmethod
#     # def say_hello():
#     #     print('Hello!!')

#     @property
#     def salary(self):
#         try:
#             return self.__salary
#         except:
#             self.__salary = self.hours * self._per_hour
#         return self.__salary

#     @salary.setter
#     def salary(self, new_salary):
#         self.__salary = new_salary

# # person1 = Person('Jannet', 100000)
# # print(person1.salary)  # <function Person.say_hello at 0x7f88ee91a160>
# # print(person1.salary())  # Hello!! # None

# person1 = Person('Jannet', 50, 15)
# print(person1.salary)
# person1.salary = 1000
# print(person1.salary)


# -- 3 --

# class User:
#     def __init__(self, username, password, email):
#         self.__username = username
#         self.__password = password
#         self.__email = email

#     @property
#     def info(self):
#         return f'{self.__username} {self.__password} {self.__email}'

# user1 = User('Janat', 'qwerty', 'qwert@gmail.com')
# print(user1.info)


# -- 4 --

class Post:

    posts = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.comments = []
        self._add_to_posts()


    @property
    def comments_count(self):
        return len(self.comments)

    def add_comment(self, comment):
        self.comments.append(comment)
        print('COMMENT ADDED !!!')

    @classmethod
    def _generate_id(cls):
        import random
        id_ = random.randint(100, 999)
        for post in cls.posts:
            if id_ == post.get('id'):
                return cls._generate_id()
        return id_


    def _add_to_posts(self):
        post = {
            'id': Post._generate_id(),
            'title': self.title,
            'author': self.author
        }
        Post.posts.append(post)

post1 = Post('Python', 'Emil')
post2 = Post('Django', 'Atai')
post1.add_comment('I believe in Python')
post1.add_comment('Python is popular')
print(post1.comments)
print(post1.comments_count)
print(post1.posts)
# print(Post.posts)

