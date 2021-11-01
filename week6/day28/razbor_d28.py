#-------- Task-1 --------

# from datetime import date, datetime

# class SmartPhone:
#     def call(self, phone_number):
#         print(f"Calling to {phone_number} number")

#     def where_to_wear(self):
#         print("You can keep me anywhere")

# class Watch:
#     def see_time(self):
#         print(f"It's {datetime.now()} now")

#     def where_to_wear(self):
#         print("You should wear me on your hand")

# class SmartWatch(Watch, SmartPhone):
#     pass

# smartwatch = SmartWatch()
# smartwatch.call(phone_number='+996771199')
# smartwatch.see_time()
# smartwatch.where_to_wear()


#-------- Task-2 --------

# class CheckMixin:
#     def check(self, username, password):
#         if self.username == username and self.password == password:
#             print("Successfully created!")
#             self.count += 1
#         else:
#             print("Wrong credentials")


# class Instagram(CheckMixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.count = 0
    
#     def post_post(self, title, username, password):
#         super().check(username=username, password=password)

# class TikTok(CheckMixin):

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.count = 0

#     def post_videos(self, video, username, password):
#         super().check(username=username, password=password)

# obj1 = Instagram(username='makers123', password='qwerty123')
# obj1.post_post(title='We are Makers', username='makers123', password = 'qwerty123')
# obj1.post_post(title='Test post', username='makers123', password = 'qwerty123')

# print(obj1.count)

# obj2 = TikTok(username='bootcamp678', password='asdf678')
# obj2.post_videos(video='We are Bootcamp', username='bootcamp678', password = 'asdf678')

# print(obj2.count)