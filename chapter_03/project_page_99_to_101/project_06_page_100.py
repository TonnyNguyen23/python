"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_06_page_100.py
Problem:
    The German mathematician Gottfried Leibniz developed the following method
    to approximate the value of π:
    π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
    Write a program that allows the user to specify the number of iterations used in
    this approximation and that displays the resulting value
Solution:

"""
# Input the number of iterations from the user
num_of_iterations = int(input("Enter the number of iterations: "))

# declare and initialize the variables
pi_div_four = 0
iteration_counter = 1

# for loop
for i in range(1, num_of_iterations + 1):
    # check if value odd
    if i % 2 != 0:
        # compute pi_div_four
        pi_div_four = pi_div_four + 1 / iteration_counter
    # value even
    else:
        # compute pi_div_four
        pi_div_four = pi_div_four - 1 / iteration_counter
    # increase the current iteration by 2
    iteration_counter += 2

# compute pi_div_four
pi_value = pi_div_four * 4

# display
print("The approximation of pi is ", pi_value)



