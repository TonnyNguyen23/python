"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_07_page_182.py
Problem:
    Explain what happens when the following recursive function is called with the
    values "hello" and 0 as arguments:
    def example(aString, index):
       if index == len(aString):
           return ""
        else:
           return aString[index] + example(aString, index + 1)
Solution:
    - If index = 5, program stops
    - Index < 5
    + Program call function example with parameters are aString and index + 1
    + Then, plus it with aString[index]
    + Example, index = 0
        return h(aString[0]) + example("hello", 1)
        ...
"""
