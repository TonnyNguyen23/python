"""
Author: Nguyen Xuan Tung
Date: 19/07/2021
Program: exercise_05_page_70.py
Problem:
    Assume that the variable teststring refers to a string. Write a loop that prints
    each character in this string, followed by its ASCII value.
Solution:

"""
string = input("Input a random string: ")
for character in string:
    print("Each character of string: " + character, "and character's ASCII: " + str(ord(character)))


