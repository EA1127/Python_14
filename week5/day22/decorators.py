# Task - 1

# def slugify(func):
#     def wrapper(title):
#         return title.replace(' ', '-').lower()
#         func()
#     return wrapper

# @slugify
# def get_title(word):
#     return word
# print(get_title('Nike Airforce 2021'))
# print(get_title('BMW X-7 Samurai'))

# @property
# @classmethod
# @staticmethod


# Task - 2

# def on_sale(func):
#     def wrapper(sale, old_price):
#         func(sale, old_price)
#         new_price = old_price - (sale * old_price /100)
#         print(f'New price is {new_price}$')
#         return new_price
#     return wrapper

# @on_sale
# def buy_product(sale, price):
#     print(f"I've got coupon with {sale}% discount. Old price was {price}$")

# sale = int(input('Enter sale: '))
# price= int(input('Enter price: '))

# if __name__ == '__main__':
#     buy_product(sale, price)


# Task - 3

users = {
    'jannat': 'qwerty',
    'atai': 'elchacha',
    'ulan': 'ulik'
}

def login_required(func):
    def wrapper(**kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        # print(username, password)
        if username in users and password == users.get(username):
            print('POST CREATED!')
            func(kwargs.get('title'), kwargs.get('image'))
        elif not username or not password:
            print('You should login')
        else:
            print('Not valid')
    return(wrapper)

@login_required
def create_post(title, image):
    print(f'{title} - {image}')

create_post(title = 'Post 1', 
            image = 'post1.jpeg', 
            username = 'jannat', 
            password = 'qwerty')