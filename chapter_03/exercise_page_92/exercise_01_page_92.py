"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_01_page_92.py
Problem:
    Translate the following for loops to equivalent while loops:
    a. for count in range(100):
    print(count)
    b. for count in range(1, 101):
    print(count)
    c. for count in range(100, 0, –1):
     print(count)
Solution:
    a. count = 0
        while count < 100:
            print(count)
            count += 1
    b. count = 0
        while count < 100:
            count += 1
            print(count)
    c. count = 100
        while count > 0:
            print(count)
            count -= 1
"""
# a.
# for count in range(100):
#     print(count)
# count = 0
# while count < 100:
#     print(count)
#     count += 1


# b.
# for count in range(1, 101):
#     print(count)
# count = 0
# while count < 100:
#     count += 1
#     print(count)

# c.
# for count in range(100, 0, -1):
#     print(count)
count = 100
while count > 0:
    print(count)
    count -= 1
