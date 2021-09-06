"""
Author: Nguyen Xuan Tung
Date: 01/08/2021
Program: exercise_02_page_106.py
Problem:
    Assume that the variable data refers to the string "myprogram.exe". Write the
    expressions that perform the following tasks:
    a. Extract the substring "gram" from data.
    b. Truncate the extension ".exe" from data.
    c. Extract the character at the middle position from data.
Solution:
    a. data[5:9]
    b. data[:9]
    c. data[7]
"""
data = "myprogram.exe"
print(data[5:9])
print(data[:9])
print(data[7])
