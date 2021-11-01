# (1)
# def get_product_cost(item, qty, price_per_one):
#     result = qty * price_per_one
#     print(f'{item} - {result} dollars')

# get_product_cost(price_per_one=3, item='Banana', qty=5)

# (2) *args
# best_friends = []
# def add_to_best_friends(bff, *args):
#     best_friends.append(bff.upper())
#     # print(args)
#     for name in args:
#         best_friends.append(name)
#         print(f'new friend {name} is added to best friend')
# add_to_best_friends('Aidai', 'Bektur', 'Emil')
# add_to_best_friends('Atai', 'Ulan')
# add_to_best_friends('Jannet')
# print(best_friends)

# (3) *args ** kwargs
# best_friends = []
# def add_to_best_friends(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['bff1'])
#     for name in args:
#         best_friends.append(name)
#         print(f'new friend {name} is added to best friend')
# add_to_best_friends('Aidai', 'Bektur', 'Emil', bff1 = 'Emma', bff2 = 'Alisa')
# # add_to_best_friends('Atai', 'Ulan')
# # add_to_best_friends('Jannet')
# print(best_friends)

# (4)
def get_sum(a, b):
    # print(a + b)
    return(a + b)
result1 = get_sum(3, 7)
result2 = get_sum(7, 11)
print(result1)
print(result2)