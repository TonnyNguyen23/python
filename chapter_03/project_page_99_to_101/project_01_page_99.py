"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_01_page_99.py
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is an equilateral
    triangle.
Solution:

"""
# a = int(input("Side 1: "))
# b = int(input("Side 2: "))
# c = int(input("Side 3: "))
#
# if a == b == c:
#     print("This is an equilateral triangle.")
# else:
#     print("This is not an equilateral triangle.")

sum = 0.0
while True:
    num = input("enter: ")
    if num == "":
        break
    sum += float(num)

