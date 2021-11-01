# 1
# a = 9
# def func():
#     a = 0
#     a += 1
#     return a
# print(func())
# print(a)

# 2
# def func1():
#     a = 9
#     def func2():
#         a = 10
#         a += 1
#         print('hello')
#         return a
#     func2()
#     print('world')
#     return func2()
# print(func1())

# 3 
# def func1():
#     a = 9
#     def func2():
#         a = 10
#         def func3():
#             # a = 0
#             nonlocal a
#             a += 1
#             return a
#         # return 'hello'
#         return func3()
#     return func2()
# print(func1())


# 4
instagram = {}

def generate_id():
    import random
    id_ = random.randint(1, 11)
    if id_ in instagram.keys():
        return generate_id()  # рекурсия
    else:
        return id_

def create_post(title, author):
    post_id = generate_id()
    print(post_id)
    post = {
        post_id: {
            'title': title,
            'author': author
        }
    }
    instagram.update(post)
    return post_id

def update_post(post_id):
    confirm_upd = input('Wanna update your recent post (y/n)?: ')
    if confirm_upd == 'y':
        instagram[post_id]['title'] = input('Enter your new title: ')
        instagram[post_id]['author'] = input('Enter your new name: ')
    else:
        pass

def delete_post(post_id):
    confirm_del = input('Do you really want to delete this post (y/n)?: ')
    if confirm_del == 'y':
        instagram.pop(post_id)
        print('successfully deleted!')
    else:
        pass

post1 = create_post('Hello World', 'Kani')
post2 = create_post('Python 14', 'Ema')
post3 = create_post('Java', 'Alice')
print(instagram)
update_post(post3)
delete_post(post2)
print(instagram)
# print(instagram[post3])


# def dfr_(a = 1, b = 2, *args):
