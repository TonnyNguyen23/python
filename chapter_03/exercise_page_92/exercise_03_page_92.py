"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_03_page_92.py
Problem:
    The log 2 of a given number N is given by M in the equation N 5 M2 . Using integer
    arithmetic, the value of M is approximately equal to the number of times N can be
    evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N. You can check your code by importing the
    math.log function and evaluating the expression round(math.log(N, 2)) (note
    that the math.log function returns a floating-point value).
Solution:

"""


def Log2n(number):
    return 1 + Log2n(number / 2) if (number > 1) else 0


n = int(input("Enter number: "))
print(Log2n(n))
