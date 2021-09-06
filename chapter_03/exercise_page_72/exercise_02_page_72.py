"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_02_page_72.py
Problem:
    Write a code segment that displays the values of the integers x, y, and z on a single
    line, such that each value is right-justified with a field width of 6.
Solution:
    Result:      2      3      4
"""
x = 2
y = 3
z = 4
print("%6d" % x, "%6d" % y, "%6d" % z)
print('%6d %6d %6d' % (x, y, z))
