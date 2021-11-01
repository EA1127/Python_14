# Task 1
# university = {
#     'программирование': 150,
#     'экономика': 98,
#     'медицина': 82
# }
# # ---a---
# university['экономика'] = 120
# print(university)

# # ---b---
# # university['лингвистика'] = 60
# # university.update({'лингвистика': 60})
# university.setdefault('лингвистика', 60)
# print(university)

# # ---c---
# print(university.pop('медицина'))
# print(university)
# print(sum(list(university.values())))


# Task 2
# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# new_dict = {}
# for key, val in dict_.items():
#     new_dict.update({val: key})
# print(new_dict)


# Task 3
# count = int(input('How many guests to invite?: '))
# guests = {}
# for i in range(1, count+1):
#     name = input('Enter guest name: ')
#     guests.setdefault(i, name)
# print(guests)


# Task 4
# my_list = [
#     {'potato': 10},
#     {'milk': 1},
#     {'eggs': 20},
#     {'bread': 2}
# ]
# while my_list:
#     product_to_remove = input()
#     for products in my_list:
#         if product_to_remove in products:
#             del products[product_to_remove]
#             print(my_list)
    
#     # any(), all() = or, and
#     if not any(my_list):
#         break

# print("It's time to pay")
