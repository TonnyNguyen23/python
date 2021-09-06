"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_10_page_63.py
Problem:
    An employee’s total weekly pay equals the hourly wage multiplied by the total
    number of regular hours plus any overtime pay. Overtime pay equals the total
    overtime hours multiplied by 1.5 times the hourly wage. Write a program that
    takes as inputs the hourly wage, total regular hours, and total overtime hours and
    displays an employee’s total weekly pay.
Solution:
    An employee’s total weekly pay
    1. Input
    - the hourly wage: wage
    - total regular hours: regular_hour
    - total overtime hours: overtime_hour
    2. Calculate
    - total = (wage * regular_hour) + (overtime_hour * wage * 1.5)
    3. Output
    - an employee’s total weekly pay: total
"""
# Input
wage = float(input("The hourly wage: "))
regular_hour = float(input("Total regular hours: "))
overtime_hour = float(input("Total overtime hours: "))

# Calculate
total = (wage * regular_hour) + (overtime_hour * wage * 1.5)

# Output
print("An employee’s total weekly pay:", total)
