"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: project_07_page_165.py
Problem:
    Write a program that inputs a text file. The program should print the unique
    words in the file in alphabetical order.
Solution:

"""
inName = input("Enter the input File Name: ")
inputFile = open(inName, 'r')
uniqueWords = []

for line in inputFile:
    words = line.split()
    for word in words:
        if not word in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()

for word in uniqueWords:
    print(word)
