"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_04_page_72.py
Problem:
    Write a loop that outputs the numbers in a list named salaries. The outputs should be
    formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:

"""

# list salary
a = [2, 3, 12, 77]
for i in a:
    print("%12.2f" % i)

