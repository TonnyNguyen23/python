"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_05_page_62.py
Problem:
    An object’s momentum is its mass multiplied by its velocity. Write a program
    that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
    inputs and then outputs its momentum.
Solution:
    Calculator momentum
    1. Input
    - mass: m
    - velocity: v
    2. Calculator
    - momentum: result = m * v
    3. Output
    - momentum is: result
"""
# Input
m = float(input("Mass is: "))
v = float(input("Velocity is: "))

# Calculator
result = m * v

# Output
print("Momentum is: " + str(result))
