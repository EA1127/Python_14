# counter = False

# def registration(name, *args, **kwargs):
#     name = name
#     email = args[0]
#     print(name)

#     def is_email(*args, **kwargs):
#         email = kwargs.get('email')
#         if email.endswith('@gmail.com'):
#             return 'Email accepted'
#         else:
#             raise ValueError('Email is NOT accepted') 
#     is_email(email=email)

#     password = kwargs.get('password')
#     password_confirm = kwargs.get('password_confirm')
#     print(args)
#     print(kwargs)
#     print(password)
#     def is_valid(*args, **kwargs):
#         password = kwargs.get('password')
#         password_confirm = kwargs.get('password_confirm')
#         if password != password_confirm:
#             raise ValueError('passwords are not matched')
#         else:
#             return 'you are registered'

#     def count_users():
#         global counter
#         counter += 1
#         return f'amount of registered: {counter}'

#     print(count_users())

#     return is_valid(password=password, password_confirm=password_confirm)

# print(registration('python14', "python14@gmail.com", password = '123', password_confirm = '123'))


