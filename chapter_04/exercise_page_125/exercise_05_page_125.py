"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: exercise_05_page_125.py
Problem:
   Write a code segment that prompts the user for a filename. If the file exists, the
    program should print its contents on the terminal. Otherwise, it should print an
    error message.
Solution:

"""
from os.path import exists
inputNameFile = input("Enter a file name: ")

if not exists(inputNameFile):
    print("Error: the file does not exist!")
else:
    inputFile = open(inputNameFile, 'r')
    print(inputFile.read())
