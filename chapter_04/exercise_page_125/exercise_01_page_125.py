"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: exercise_01_page_125.py
Problem:
   Write a code segment that opens a file named myfile.txt for input and prints the
    number of lines in the file.
Solution:

"""
test = open("myfile.txt", 'w')
test.write("One. \nTwo. \n")

test = open("myfile.txt", 'r')

for line in test:
    print(line)

