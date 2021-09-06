"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_04_page_62.py
Problem:
    Write a program that takes the radius of a sphere (a floating-point number) as
    input and then outputs the sphere’s diameter, circumference, surface area, and
    volume.
Solution:
    The sphere’s diameter, circumference, surface area, and
    volume.
    1. Inputs
    - radius: r
    2. Calculator
    - diameter: d = r * 2
    - circumference: Cv = d * pi
    - surface area: S = 4 * pi * r * r
    - volume: V = 4/3 * pi * r * r * r
    3. Outputs
    - Diameter is: d
    - Circumference is: Cv
    - Surface area is: S
    - Volume is: V
"""
import math

# Input
r = float(input("Radius is: "))

# Calculator
d = r * 2
Cv = d * math.pi
S = 4 * math.pi * r * r
V = (4/3) * math.pi * r * r * r

# Outputs
print("Diameter is: " + str(round(d, 2)))
print("Circumference is: " + str(round(Cv, 2)))
print("Surface area is: " + str(round(S, 2)))
print("Volume is: " + str(round(V, 2)))
