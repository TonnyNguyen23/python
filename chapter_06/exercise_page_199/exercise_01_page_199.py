"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_01_page_199.py
Problem:
    Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
Solution:

"""

numbers = [1, -2, -66, 79]
result = list(map(abs, numbers))
print(result)
