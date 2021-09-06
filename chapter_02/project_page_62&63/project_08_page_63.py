"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_08_page_63.py
Problem:
    Light travels at 3 *108 meters per second. A light-year is the distance a light beam
    travels in one year. Write a program that calculates and displays the value of a
    light-year.
Solution:
    Calculate the value of a light-year.
    1. Constant
    - speed of light: speed_light = 3*108 m/s
    2. Change value
    - number of seconds in a year: second_year = 365 * (24 * 3600)
    3. Calculate
    - a light-year: light_year = speed_light * second_year
    4. Output
    - the value of a light-year: light_year
"""
# speed of light
speed_light = 3*108

# number of seconds in a year
second_year = 365 * (24 * 3600)

# Calculate
light_year = speed_light * second_year

# Output
print("The value of a light-year: " + str(light_year) + " m/s")
