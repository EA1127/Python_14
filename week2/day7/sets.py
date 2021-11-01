# Task 1
# monday = {'Math', 'Literature', 'Physics'}
# tuesday = {'Russian', 'Biology', 'Chemistry'}
# wednsday = {'PE', 'Biology', 'History'}
# thursday = {'Russian', 'Music', 'Math'}
# friday = {'Economics', 'Chemistry', 'CS', 'Math'}

# study_week = (monday, tuesday, wednsday, thursday, friday)  # кортеж из множеств

# a
# for day in study_week:
#     # print(day)
#     for subject in day:
#         if subject == 'Chemistry':
#             day.remove('Chemistry')
#             day.add('Politics')
# print(study_week)

# b
# for i in range(len(study_week)-1):
#     if study_week[i] & study_week[i + 1]:
#         study_week[i + 1].remove(*(study_week[i] & study_week[i + 1]))
#         study_week[i + 1].add('Politics')
# print(study_week)


# Task 2

# set1 = {20, 78, 33}
# set2 = {90, 20, 40}
# set3 = {33, 90, 100}
#      # {78, 33}  {78}
# print(set1 - set2 - set3)
# print(set2 - set1)

# import random
# print(random.choice(['Emma', 'Billy', 'Uma', 'Ann', 'Dean']))
# print(random.randrange(50, 1000))