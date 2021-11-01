# Task-1

# with open('/home/hello/Desktop/bootcamp/week4/day16/tsk_numbers.txt', 'w') as file1:
#     for number in range(1, 21):
#         file1.write(str(number) + '\n')

# with open('/home/hello/Desktop/bootcamp/week4/day16/tsk_squares.txt', 'w') as file2:
#     with open('/home/hello/Desktop/bootcamp/week4/day16/tsk_numbers.txt') as file1:
#         # data = file1.read().split('\n')
#         # data.pop()
#         # # print(data)
#         # new_data = list(map(int, data))
#         # # print(new_data)
#         # for i in new_data:
#         #     file2.write(str(i ** 2) + '\n')

#         data = file1.read().split()
#         for i in data:
#             file2.write(str(int(i)**2) + '\n')


# Task-2
# with open('/home/hello/Desktop/bootcamp/week4/day16/tsk_usernames.txt', 'w') as my_file:
#     while True:
#         username = input('Enter username: ')
#         if username.lower() == 'end':
#             break
#         my_file.write(f'{username} - {len(username)}\n')
