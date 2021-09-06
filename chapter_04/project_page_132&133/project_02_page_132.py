"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: project_02_page_132.py
Problem:
    Write a script that inputs a line of encrypted text and a distance value and outputs
    plaintext using a Caesar cipher. The script should work for any printable characters.
Solution:

"""
inputs = input("Enter the coded text: ")
distance = int(input("Enter distance: "))
final = ""
for ch in inputs:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordvalue - 1))
    final += chr(cipherValue)
print(final)
