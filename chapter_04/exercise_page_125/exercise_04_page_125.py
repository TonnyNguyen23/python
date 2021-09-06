"""
Author: Nguyen Xuan Tung
Date: 03/08/2021
Program: exercise_04_page_125.py
Problem:
    Write a code segment that prints the names of all of the items in the current
    working directory.
Solution:

"""
import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if ".py" in name:
        print(name)
