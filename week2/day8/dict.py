# 1
# test = {
#     'Atai': 15,
#     'Bektur': 13,
#     'Jannat': 2,
#     'Kamila': 11,
#     'Ulan': 10
# }
# scores = test.values()
# print(sum(scores) / len(scores))

# 2
# users = {
#     'kani': 'kani@gmail.com',
#     'atai': 'atai@mail.ru',
#     'jannat': 'jannat@gmail.com',
#     'bektur': 'bektur@mail.ru',
#     'nurba': 'nurba@gmail.com',
#     'ulan': 'ulan@mail.ru',
#     'sezim': 'sezim@gmail.com'
# }
# user_emails = users.values()
# # print(user_emails)
# total = len(users)
# # print(total)
# gmail_count = 0
# for email in user_emails:
#     if email.endswith('@gmail.com'):
#         gmail_count += 1
# print(f'Процент пользователей gmail составляет {round(gmail_count/total*100, 2)} %')

# 3
person = {
    "name": "Nurbolot",
    "age": 35,
    "languages": ['Python0', 'JavaScript'],
    "children": [
        {
            "name": "Jannat",
            "age": 10
        },
        {
            "name": "Aselya",
            "age": 5
        }
    ]
}

# person["languages"].append('C++')
# # person.setdefault('salary', 4000)
# person.update({'salary': 4000})
# person['wife'] = {'name': 'Karen', 'age': 29}
# person['children'].append({'name': 'New Child', 'age': 1})
# print(len(person['children']))
# print(person)

# 4
# TIME = "10:00:00"
# students = {
#     'Kanat': "09:20:34",
#     'Aliya': "09:50:50",
#     'Uluk': "14:00:00",
#     'Kair': "09:59:59",
#     "Emil": "10:00:01"
# }
# late_students = []
# for key, val in students.items():
#     if val > TIME:
#         late_students.append(key)
# print(late_students)