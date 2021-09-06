"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_02_page_199.py
Problem:
    Write the code for a filtering that generates a list of the positive numbers in a list
    named numbers. You should use a lambda to create the auxiliary function.
Solution:

"""

numbers = [1, -2, -66, 79]
result = list(filter(lambda x: x > 0, numbers))
print(result)
