"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_09_page_63.py
Problem:
    Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
    • A kilometer represents 1/10,000 of the distance between the North Pole and
    the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
    Pole and the equator.
    • A nautical mile is 1 minute of an arc.
Solution:
    1. Input
    - kilometer
    2. Calculate
    - degrees per minute: degrees_per_min = 90*60
    - one kilometer: one_kilo = degrees_per_min/10.000
    - a nautical mile: nautical_mile = one_kilo * kilometer
    3. Output
    - a nautical mile: nautical_mile
"""
kilometer = int(input("Input the amount of kilometers: "))

degrees_per_min = 90*60
one_kilo = degrees_per_min/10000
nautical_mile = one_kilo * kilometer

print(kilometer,"kilometer is",nautical_mile,"nautical miles")

