"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: exercise_03_page_149.py
Problem:
    Use the function even to simplify the definition of the function odd presented in
    this section.
Solution:

"""


def main():
    number = float(input("Enter number to check even: "))
    result = isEven(number)
    print(result)


def isEven(x):
    if x % 2 != 0:
        return True
    else:
        return False


# main
main()
