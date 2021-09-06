"""
Author: Nguyen Xuan Tung
Date: 01/08/2021
Program: exercise_01_page_109.py
Problem:
    Write the encrypted text of each of the following words using a Caesar cipher with
    a distance value of 3:
    a. python
    b. hacker
    c. wow
Solution:
    a. sbwkrq
    b. kdfnhu
    c. zrz
"""
plainText = input("Enter a one-word, lowercase message: ")
distance = 3
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
print(code)
