"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: project_03_page_203.py
Problem:
    Elena complains that the recursive newton function in Project 2 includes an extra
    argument for the estimate. The function’s users should not have to provide this
    value, which is always the same, when they call this function. Modify the definition of
    the function so that it uses a keyword argument with the appropriate
    default value, and call the function without a second argument to demonstrate
    that it solves this problem.
Solution:

"""
approximating = 0.000001


def newton2(x, estimate=1.0):
    """
    Calculate approximating square
    :param estimate:
    :param x: enter a number to calculate approximating square
    :return: the estimate of its square root
    """
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference > approximating:
        estimate = newton2(x, estimate)
    return estimate


print(newton2(4))
