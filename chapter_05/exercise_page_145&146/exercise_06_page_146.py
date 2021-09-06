"""
Author: Nguyen Xuan Tung
Date: 08/08/2021
Program: exercise_06_page_146.py
Problem:
   Write a loop that replaces each number in a list named data with its absolute value.
Solution:

"""
data = [1, -2, 5, -9]
for i in range(len(data)):
    if data[i] >= 0:
        print(data[i])
    else:
        print(data[i] * -1)
