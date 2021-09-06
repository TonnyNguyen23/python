"""
Author: Nguyen Xuan Tung
Date: 02/08/2021
Program: exercise_01_page_118.py
Problem:
    Assume that the variable data refers to the string "Python rules!". Use a string
    method from Table 4-2 to perform the following tasks:
    a. Obtain a list of the words in the string.
    b. Convert the string to uppercase.
    c. Locate the position of the string "rules".
    d. Replace the exclamation point with a question mark.
Solution:

"""
string = "Python rules!"

# a. Obtain a list of the words in the string.
words = string.split()
print(words)

# b. Convert the string to uppercase.
print(string.upper())

# c. Locate the position of the string "rules".
print(string.find("rules"))

# d. Replace the exclamation point with a question mark.
print(string.replace("!", "?"))
