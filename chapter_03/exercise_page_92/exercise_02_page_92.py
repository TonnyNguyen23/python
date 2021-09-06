"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_02_page_92.py
Problem:
    The factorial of an integer N is the product of the integers between 1 and N, inclusive.
     Write a while loop that computes the factorial of a given integer N.
Solution:

"""
number = int(input("Enter number: "))
result = 1
while number > 0:
    result *= number
    number -= 1

print(result)
