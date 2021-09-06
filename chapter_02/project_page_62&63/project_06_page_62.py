"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_06_page_62.py
Problem:
    The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
    where m is the object’s mass and v is its velocity. Modify the program you created
    in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
Solution:
    Calculator momentum
    1. Input
    - mass: m
    - velocity: v
    2. Calculator
    - momentum: result = m * v * v
    3. Output
    - momentum is: result
"""
# Input
m = float(input("Mass is: "))
v = float(input("Velocity is: "))

# Calculator
result = m * v * v

# Output
print("Momentum is: " + str(result))

