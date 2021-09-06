"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_05_page_100.py
Problem:
    A local biologist needs a program to predict population growth. The inputs
    would be the initial number of organisms, the rate of growth (a real number
    greater than 0), the number of hours it takes to achieve this rate, and a number
    of hours during which the population grows. For example, one might start with a
    population of 500 organisms, a growth rate of 2, and a growth period to achieve
    this rate of 6 hours. Assuming that none of the organisms die, this would imply
    that this population would double in size every 6 hours. Thus, after allowing
    6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
    have 2000 organisms. Write a program that takes these inputs and displays a prediction
    of the total population.
Solution:

"""
# Enter the initial number of organisms
organisms = int(input("Enter the initial number of organisms:"))

# Enter the rate of growth (a real number greater than 0)
rate_of_growth = int(input("Enter the rate of growth [a real number > 0]: "))

# Enter the number of hours it takes to achieve this rate
num_of_hours = int(input("Enter the number of hours to achieve the rate of growth: "))

# Enter a number of hours during which the population grows
total_hours = int(input("Enter the total hours of growth: "))

total_organisms = organisms
while num_of_hours >= total_hours:
    organisms *= rate_of_growth
    total_organisms += organisms
    num_of_hours += num_of_hours
print("The total population is ", total_organisms)
