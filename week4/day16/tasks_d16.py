# Task 1
# with open('/home/hello/Desktop/bootcamp/week4/day16/task1.txt', 'r') as file1:
#     for line in file1.readlines(8):
#         print(line)

# with open('task1.txt', 'r') as file1:
#     for line in file1.readlines(8):
#         print(line)

# Task 2
# with open('/home/hello/Desktop/bootcamp/week4/day16/task2.txt', 'r') as file1:
#     for line in file1:
#         print(line)

# with open('task2.txt', 'r') as file1:
#     for line in file1:
#         print(line)


# Task 3
# with open('/home/hello/Desktop/bootcamp/week4/day16/task3.txt', 'w+') as file1:
#     for i in range(10):
#         file1.write(str(i) + '*')
#     file1.seek(0)
#     print(file1.read())

# with open('task3.txt', 'w+') as file1:
#     for i in range(10):
#         file1.write(str(i) + '*')
#     file1.seek(0)
#     print(file1.read())


# Task 4
# with open('/home/hello/Desktop/bootcamp/week4/day16/task4.txt', 'r') as file1:
#     print(len(file1.readlines()))

# with open('task4.txt', 'r') as file1:
#     print(len(file1.readlines()))


# Task 5
# with open('/home/hello/Desktop/bootcamp/week4/day16/task5.txt', 'r+') as file:
#     list1 = [int(i.replace('\n', '')) for i in file.readlines()]

# with open('task5.txt', 'r+') as file:
#     list1 = [int(i.replace('\n', '')) for i in file.readlines()]


# Task 6  
# with open('/home/hello/Desktop/bootcamp/week4/day16/task6.txt', 'w') as file:
#     file.write(f'{min(list1)}-{max(list1)}')

# with open('task6.txt', 'w') as file:
#     file.write(f'{min(list1)}-{max(list1)}')