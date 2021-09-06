"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_09_page_101.py
Problem:
    Write a program that receives a series of numbers from the user and allows the
    user to press the enter key to indicate that he or she is finished providing inputs.
    After the user presses the enter key, the program should print the sum of the
    numbers and their average.
Solution:

"""
theSum = 0.0
data = input("Enter a number or press Enter to quit: ")

while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or press Enter to quit: ")
    avg = theSum/number

print("The sum is", theSum)
print("The average is", avg)
