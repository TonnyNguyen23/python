"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_07_page_100.py
Problem:
    Teachers in most school districts are paid on a schedule that provides a salary
    based on their number of years of teaching experience. For example, a beginning
    teacher in the Lexington School District might be paid $30,000 the first year. For
    each year of experience after this first year, up to 10 years, the teacher receives a
    2% increase over the preceding value. Write a program that displays a salary schedule,
    in tabular format, for teachers in a school district. The inputs are the starting
    salary, the percentage increase, and the number of years in the schedule. Each row
    in the schedule should contain the year number and the salary for that year.
Solution:

"""
salary = int(input('Enter the starting salary: $'))
annual_Increase = (float(input('Enter the annual % increase: ')) / 100)
years = int(input('Enter the number of years: '))
print('Year\tSalary')
print('--------------')
for year in range(1, years + 1):
    salary = salary + salary * annual_Increase
    print(year, '\t', "%0.2f" % salary)
