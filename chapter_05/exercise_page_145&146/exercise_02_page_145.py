"""
Author: Nguyen Xuan Tung
Date: 08/08/2021
Program: exercise_02_page_145.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
    that perform the following tasks:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data.
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.
Solution:
    a. [1, 3, 7]
    b. [5, 3, 7, 9]
    c. [5, 3, 22, 7]
    d. [5, 7]
    e. [5, 3, 7, 2, 4]
    f. 7
    g. [3, 5, 7]
"""
data = [5, 3, 7]
# a...
# data[0] = 1
# print(data)

# b...
# data.append(9)
# print(data)

# c...
# data.insert(2, 22)
# print(data)

# d...
# data.pop(1)
# print(data)

# e...
# data.extend([2, 4])
# print(data)

# f...
# target = 7
# if target in data:
#     print(target)
# else:
#     print(-1)

# g...
print(data.sort())
print(data)




