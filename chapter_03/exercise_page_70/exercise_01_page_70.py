"""
Author: Nguyen Xuan Tung
Date: 19/07/2021
Program: exercise_01_page_70.py
Problem:
    1. Write the outputs of the following loops:
    a. for count in range(5):
     print(count + 1, end = " ")
    b. for count in range(1, 4):
     print(count, end = " ")
    c. for count in range(1, 6, 2):
     print(count, end = " ")
    d. for count in range(6, 1, –1):
     print(count, end = " ")
Solution:
    Results:
        a. 1 2 3 4 5
        b. 1 2 3
        c. 1 3 5
        d. 6 5 4 3 2
"""
# cau a
print("cau a: ")
for count in range(5):
    print(count + 1, end=" ")
print("\n")

# cau b
print("cau b: ")
for count in range(1, 4):
    print(count, end=" ")
print("\n")

# cau c
print("cau c: ")
for count in range(1, 6, 2):
    print(count, end=" ")
print("\n")

# cau d
print("cau d: ")
for count in range(6, 1, -1):
    print(count, end=" ")
