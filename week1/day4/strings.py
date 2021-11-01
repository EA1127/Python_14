# indexes
# string = "Hello! We are Python Vol. 14"
# print(string[:5])
# print(string[14:20])
# print(string[-2:])
# print(string[-1:-3:-1])
# print(string[::-1])

# string = "Civic".lower()
# print(string)
# if string == string[::-1]:
#     print('Polyndrome')
# else:
#     print('Not Polyndrome')

# len()
# password = input('Enter password: ')
# if len(password) < 8:
#     print('Password should be at least 8 symbols')
# if password.isalpha():
#     print('Password should contain digits too')
# if password.isdigit():
#     print('Password should contain letters too')
# if password.islower():
#     print('Password should contain at least 1 uppercase symbol')
# else:
#     print('Password is saved!')

# email = input('Enter your email: ')
# if not email.endswith(('@gmail.com', '@mail.ru', '@yahoo.com')):
#     print('only gmail alowed')
# else:
#     print("OK")

# join()
# list_ = ['M', 'A', 'K', 'E', 'R', 'S']
# string = '*'.join(list_)
# print(string)


# string = 'My name is Azamat. I am a developer'
# # print(string.replace('a', '*'))
# list_ = []
# for i in string:
#     if i.lower() == 'a':
#         list_.append('*')
#     else:
#         list_.append(i)
# print(''.join(list_))


# str_ = ''.join(['*' if i.lower() == 'a' else i for i in string])
# print(str_)
