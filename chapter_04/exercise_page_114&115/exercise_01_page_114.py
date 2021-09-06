"""
Author: Nguyen Xuan Tung
Date: 02/08/2021
Program: exercise_01_page_114.py
Problem:
    Translate each of the following numbers to decimal numbers:
    a. 11001(2)
    b. 100000(2)
    c. 11111(2)
Solution:
    a. 25
    b. 32
    c. 31
"""
bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
