"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: exercise_04_page_149.py
Problem:
    Define a function named summation. This function expects two numbers, named
    low and high, as arguments. The function computes and returns the sum of the
    numbers between low and high, inclusive.
Solution:

"""
low = int(input("Enter low: "))
high = int(input("Enter high: "))


def summation():
    sum = 0
    for i in (low, high):
        sum += i
    print(sum)


summation()
