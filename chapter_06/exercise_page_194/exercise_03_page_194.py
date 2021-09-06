"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: exercise_02_page_194.py
Problem:
    What is the lifetime of a variable? Give an example.
Solution:
    A variable’s lifetime is the period of time during program execution when the variable has memory storage
    associated with it. When a variable comes into existence, storage is allocated for it; when it goes out of
    existence, storage is reclaimed by the PVM.
    Example:
        def func1():
            x='Local_x'
            print(x)
        func1()
        print(x) # Accessing Local Variable ‘x’ Outside func1() method
"""