"""
Author: Nguyen Xuan Tung
Date: 01/08/2021
Program: exercise_04_page_106.py
Problem:
    Assume that the variable myString refers to a string. Write a code segment that
    uses a loop to print the characters of the string in reverse order.
Solution:

"""
myString = input("Enter my string: ")
reverseString = ""
length = len(myString) - 1
while length >= 0:
    reverseString += myString[length]
    length -= 1
print(reverseString)
