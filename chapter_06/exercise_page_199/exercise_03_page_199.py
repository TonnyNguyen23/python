"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_03_page_199.py
Problem:
   Write the code for a reducing that creates a single string from a list of strings named
    words.
Solution:

"""
from functools import reduce


def add(x, y):
    return x + y


words = ["h", "e", "l", "l", "o"]
result = reduce(add, words)
print(result)
