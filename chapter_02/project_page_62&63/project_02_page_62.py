"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_02_page_62.py
Problem:
    You can calculate the surface area of a cube if you know the length of an edge.
    Write a program that takes the length of an edge (an integer) as input and prints
    the cube’s surface area as output.
Solution:
    Compute the cube's surface area.
    1. Surface of the cube
    - There are 6 surfaces. So, assign number of face to 6
    2. Input length of an edge
    - edge
    3. Computations
    - area of a face = edge ** edge = s1
    - the cube's surface area = s1 * 6 = S
    4. The output are
    - the cube's surface area
"""
# Assign number of face
number_of_face = 6

# Input length of an edge
edge = int(input('Input length of an edge: '))

# Compute the cube's surface area
s1 = edge * edge
S = s1*6

# Display
print('the cube\'s surface area: ' + str(S))


