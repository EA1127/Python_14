# # 1-task
# a = {True, 15, "makers"}
# print(a)

# # 2-task
# a = {True, 15, "makers"}
# print(len(a))

# # 3-task
# a = {True, 15, "makers"}
# a.add('Hello world!')
# print(a)

# # 4-task
# a = {False, 5, 10.5, 'makers'}
# b = {True, 5, 7, 'makers'}
# a.update(b)
# print(a)

# # 5-task
# a = {False, 5, 10.5, 'makers'}
# a.discard('7')
# print(a)

# # 6-task
# a = {False, 5, 10.5, 'makers'}
# a.remove(5)
# print(a)

# # 7-task
# a = {False, 5, 10.5, 'makers'}
# a.clear()
# print(a)

# # 8-task
# a = {False, 5, 10.5, 'makers'}
# b = {False, True, 5, 'makers'}
# print(a & b)
# print(a.intersection(b))

# # 9-task
# a = {False, 5, 10.5, 'makers'}
# b = {False, True, 5, 'makers'}
# print(a - b)
# print(a.difference(b))

# # 10-task
# a = {False, 5, 10.5, 'makers'}
# b = {False, True, 5, 'makers'}
# print(a | b)
# print(a.union(b))

# # 11-task
# b = {False, 5, 10.5, 'makers'}
# a = {False, 'makers'}
# if a.issubset(b):
#     print('Подмножество!')
# else:
#     False

# # 12-task
# a = {False, 5, 10.5, 'makers'}
# b = {False, 'makers'}
# if a.issuperset(b):
#     print('Надмножество!')
# else:
#     False

# # 13
# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# result = []
# w1 = robert & kail
# w2 = robert & merri
# if w1:
#     result.append('kail')
# if w2:
#     result.append('merri')
# if result:
#     print(' '.join(result))


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# w1 = kail & robert
# w2 = merri & robert
# if w1 and w2:
#     print('kail merri')
# elif w1:
#     print('kail')
# elif w2:
#     print('merri')
# else:
#     None

# # 14
# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OchakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = tilek | timur | alexander
# a = tilek & timur & alexander & elina
# print(a)

# # 15
# ingredients = {"cыр чеддар","грибы","соус","шпинат"} 
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("Сыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)


# Extra task 1

# a = [set(), set(), set()]
# inp1 = set(input().split(' '))
# inp2 = int(input())
# if inp2 == 1:
#     a[0].update(set(inp1))
# elif inp2 == 2:
#     a[1].update(set(inp1))
# elif inp2 == 3:
#     a[2].update(set(inp1))
# else:
#     None
# for i in a:
#     if int(len(i)) == 0:
#         i.add('default value')
# print(a)


# Extra task 2

# import random
# a = set()
# b = set()
# list_a = random.sample(range(10),5)
# list_b = random.sample(range(11),5)
# for i in list_a:
#     a.add(i)
# for i in list_b:
#     b.add(i)
# # print(list_a)
# # print(list_b)
# a.pop()
# b.pop()
# print(a)
# print(b)
# print(a & b)

