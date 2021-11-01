# Task1

# with open('platform.txt', 'w+') as f:
#     while True:
#         email = input("Enter your email: ")
#         if not email:
#             print("STUDENT ADDED")
#             break
#         f.write(email + '\n')


# Task2

# with open('platform.txt') as f:
#     student = input('Enter your email: ')
#     students = f.read()
#     if student in students:
#         print('You have an access')
#     else:
#         print("- -")


# Task3

# with open('kpi.txt') as f:
#     # print(f.readlines())
#     data = list(map(lambda x: x.replace('\n', ''), f.readlines()))
#     # print(data)
#     data = [name.split() for name in data]
#     print(data)
#     max_point = 0
#     max_voice = 0
#     for list_ in data:
#         if int(list_[1]) > max_point:
#             max_point = int(list_[1])
#             best_student = list_[0]
#         if int(list_[-1]) > max_voice:
#             max_voice = int(list_[-1])
#             fire_student = list_[0]
#     print(best_student, max_point)
#     print(fire_student, max_voice)


# Task4
# with open('contacts.txt') as f:
#     contacts = f.readlines()
#     # print(contacts)
#     contacts = [contact.split() for contact in contacts]
#     # print(contacts)
#     contacts = {contact[0]: contact[1] for contact in contacts}
#     # print(contacts)
#     name = input("Enter name: ").lower().title()
#     # print(name)
#     print(contacts.get(name, 'no such name in contact-book'))


# Task5
from datetime import datetime

with open('qrcode.txt', 'a') as f:
    name = input('Enter name: ')
    f.write(f'{name} {datetime.now().strftime("%H:%M:%S %d-%B-%Y")}\n')
