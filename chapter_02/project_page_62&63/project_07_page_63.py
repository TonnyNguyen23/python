"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_07_page_63.py
Problem:
    Write a program that calculates and prints the number of minutes in a year.
Solution:
    Calculator the number of minutes in a year.
    1. Choose year
    - a year has 365 day: year_365
    - a year has 366 day: year_366
    2. Calculate
    - year_365 = (24 * 60) * 365
    - year_366 = (24 * 60) * 366
    3. Output
    - the number of minutes in year has 365 day: year_365
    - the number of minutes in year has 366 day: year_366
"""
year_365 = (24 * 60) * 365
year_366 = (24 * 60) * 366

print("the number of minutes in year has 365 day are: " + str(year_365) + " minutes")
print("the number of minutes in year has 366 day are: " + str(year_366) + " minutes")

