"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_02_page_182.py
Problem:
    The factorial of a positive integer n, fact(n), is defined recursively as follows:
    fact(n) = 1 , when n = 1
    fact(n) = n * fact(n - 1) , otherwise
    Define a recursive function fact that returns the factorial of a given positive
    integer.
Solution:

"""
number = int(input("Enter n to calculate: "))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


result = fact(number)
print(f"Factorial of {str(number)} is: " + str(result))
