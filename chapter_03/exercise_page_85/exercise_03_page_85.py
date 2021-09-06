"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_03_page_85.py
Problem:
    Write a loop that counts the number of space characters in a string. Recall that the
    space character is represented as ' '.
Solution:

"""
string = input("Enter string: ")
count = 0
for character in string:
    if character == " ":
        count += 1
print("The number of space characters: " + str(count))

