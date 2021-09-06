"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_02_page_99.py
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is a right triangle.
    Recall from the Pythagorean theorem that in a right triangle, the square of
    one side equals the sum of the squares of the other two sides.
Solution:

"""
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a**2 == b**2 + c**2:
    print("This is a right triangle")
elif b**2 == a**2 + c**2:
    print("This is a right triangle")
elif c**2 == a**2 + b**2:
    print("This is a right triangle")
else:
    print("This is not a right triangle")
