"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: exercise_03_page_125.py
Problem:
     Assume that a file contains integers separated by newlines. Write a code segment
    that opens the file and prints the average value of the integers.
Solution:

"""
test = open("integers.txt", 'w')
test.write("1 \n 2 \n")
test = open("integers.txt", 'r')
theSum = 0
count = 0
for line in test:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        theSum += number
        count += 1
    if count == 0:
        average = 0
    else:
        average = theSum/count
print("The average is", average)
