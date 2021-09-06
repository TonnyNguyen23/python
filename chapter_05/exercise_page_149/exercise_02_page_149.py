"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: exercise_02_page_149.py
Problem:
    Define a function named even. This function expects a number as an argument and
    returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A
    number is evenly divisible by 2 if the remainder is 0.)
Solution:

"""


def main():
    number = float(input("Enter number to check even: "))
    result = isEven(number)
    print(result)


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


# main
main()
