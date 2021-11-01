# task-1

# class User:
#     platform = 'Makers'

#     def __init__(self, age, username, password):
#         self.age = age
#         self.username = username
#         self.password = password
#         self.followers = []
    
#     def follow(self, user):
#         user.followers.append(self.username)
    
#     def unfollow(self, user):
#         user.followers.remove(self.username)

#     def followers_count(self):
#         print(len(self.followers))
#         return len(self.followers)
    
#     def __str__(self):
#         return f'{self.username} {self.age}'

# user1 = User(age=22,
#             username='jannat',
#             password='qwerty')

# user2 = User(age=18,
#             username='atai',
#             password='helloworld')

# user3 = User(age=25,
#             username='ulan',
#             password='python3')

# print(user1)
# # print(user2)
# print(user1.age, user1.username, user1.platform)
# print(user2.age, user2.username, user2.platform)

# user2.follow(user1)
# user3.follow(user1)
# print("Jannats's followers:", user1.followers)

# user1.follow(user2)
# print("Atai's followers:", user2.followers)

# user2.unfollow(user1)
# print("Jannats's followers:", user1.followers)

# user1.followers_count()
# user2.followers_count()
# user3.followers_count()


# task-2

# class FootballPlayer():

#     status = 'sportik'

#     def __init__(self, name, last_name, team):
#         self.name = name
#         self.last_name = last_name
#         self.team = team
#         self.goals = 0

#     def goal(self):
#         self.goals += 1
#         print('GOOOAAAL!!!')

# player1 = FootballPlayer('Cristiano', 'Ronaldo', 'MU')
# player2 = FootballPlayer('Lionel', 'Messi', 'PSG')

# import random
# players = [player1, player2]
# for _ in range(10):
#     random.choice(players).goal()

# print(player1.goals)
# print(player2.goals)

# player1.team = 'Dordoi'
# print(player1.team)
# player1.salary = 100000
# print(player1.salary)

# print(player1.status)
# print(player2.status)
# player1.status = 'proger'
# print(player1.status)
# print(player2.status)

# player1.goal()
# player2.goal()
# player1.goal()
# print(player1.goals)
# print(player2.goals)

        
