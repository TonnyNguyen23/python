"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_04_page_85.py
Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.
Solution:

"""
from typing import List, Callable

string = input("Enter string: ")

words: list[Callable[[], str]] = [word.lower() for word in string.split()]

words.sort()

for word in words:
    print(word)

