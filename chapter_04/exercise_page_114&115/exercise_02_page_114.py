"""
Author: Nguyen Xuan Tung
Date: 02/08/2021
Program: exercise_02_page_114.py
Problem:
    Translate each of the following numbers to binary numbers:
    a. 47(10)
    b. 127(10)
    c. 64(10)
Solution:
    a. 101111
    b. 1111111
    c. 1000000
"""
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder,
                              bitString))
    print("The binary representation is", bitString)
