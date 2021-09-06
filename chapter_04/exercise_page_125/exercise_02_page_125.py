"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: exercise_02_page_125.py
Problem:
    Write a code segment that opens a file for input and prints the number of
    four-letter words in the file.
Solution:

"""
count = 0
test = open("myfile.txt", 'r')
for line in test:
    words = line.split()
    for word in words:
        if len(word) == 4:
            count += 1
print(count)
