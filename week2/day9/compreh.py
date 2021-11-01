""" Task 1 list - comprehension """

# через генератор листов
# string = 'Azamat is an amazing actor.'
# list_ = [
#     i if i.lower() != 'a' else '*'
#     for i in string
#     ]
# print(''.join(list_))

# через цикл
# list_ = []
# for i in string:
#     if i.lower() == 'a':
#         list_.append('*')
#     else:
#         list_.append(i)
# print(''.join(list_))


""" Task 2 - dictionary comprehension """

# users = {
#     'post1': ['Emil', 'Jannat', 'Sezim', 'Atay', 'Jannet', 'Ruslan'],
#     'post2': ['Atay', 'Nurbek', 'Bektur'],
#     'post3': ['Jannat', 'Atay', 'Aikol', 'Alia', 'Bektur']
# }

# likes = {key:len(val) for key,val in users.items()}
# most_liked_post = None
# most_likes = 0
# for post,like in likes.items():
#     if like >= most_likes:
#         most_likes = like
#         most_liked_post = post
# print(most_liked_post)


""" Task 3 - dictionary comprehension """

# users = {
#     'post1': ['Emil', 'Janat', 'Sezim', 'Atay', 'Jannet', 'Bektur'],
#     'post2': ['Atay', 'Nurbek', 'Bektur', 'Emil'],
#     'post3': ['Janat', 'Atay', 'Aikol', 'Alia', 'Bektur', 'Emil']
# }

# candidates = [
#     name.upper() + '!!!' for name in users['post1']
#     if name in users['post2'] and
#     name in users['post3']
#     ]
# print(candidates)
# import random
# winner = random.choice(candidates)
# print(winner)


""" Task 4 - set comprehension """

users = {
    'post1': ['Emil', 'Janat', 'Sezim', 'Atay', 'Jannet', 'Bektur'],
    'post2': ['Atay', 'Nurbek', 'Bektur', 'Emil'],
    'post3': ['Janat', 'Atay', 'Aikol', 'Alia', 'Bektur', 'Emil']
}

list_users = [set(list_) for list_ in users.values()]
# print(list(users.values()))
# print(list_users)
# print(list_users[0] & list_users[1] & list_users[-1])
candidates = list_users[0]
for set in list_users:
    candidates &= set

print(candidates.pop())
