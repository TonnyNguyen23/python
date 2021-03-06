"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: project_01_page_203.py
Problem:
    Package Newton’s method for approximating square roots (Case Study 3.6) in a
    function named newton. This function expects the input number as an argument
    and returns the estimate of its square root. The script should also include a main
    function that allows the user to compute square roots of inputs until she presses
    the enter/return key
Solution:

"""
import math

approximating = 0.000001


def newton2(x):
    """
    Calculate approximating square
    :param x: enter a number to calculate approximating square
    :return: the estimate of its square root
    """
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= approximating:
            break
    return estimate


def main():
    """
    :return:
    """
    while True:
        x = input("Enter a positive number or enter to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton2(x))
        print("Python's estimate is     ", math.sqrt(x))


if __name__ == "__main__":
    main()
