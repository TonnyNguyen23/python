"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: project_01_page_132.py
Problem:
    Write a script that inputs a line of plaintext and a distance value and outputs an
    encrypted text using a Caesar cipher. The script should work for any printable
    characters.
Solution:

"""
# string = input("Enter string: ")
# distance = int(input("Enter the distance: "))
# final = ""
# for chac in string:
#     ordvalue = ord(chac)
#     cipherValue = ordvalue + distance
#     if cipherValue > ord('z'):
#         cipherValue = ord('a') + distance - \
#                       (ord('z') - ordvalue + 1)
#     final += chr(cipherValue)
# print(final)

data = 'Hello UDA!'
data.replace("UDA", "UDA Student")
# data = data + " Examination"
print(len(data))
