"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_02_page_85.py
Problem:
    Assume that x refers to a number. Write a code segment that prints the number’s
    absolute value without using Python’s abs function.
Solution:

"""
x = int(input("Enter x: "))


def my_abs(number):
    if x <= 0:
        print(x * -1)
    else:
        print(x * 1)


my_abs(x)
