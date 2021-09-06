"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_04_page_99.py
Problem:
    A standard science experiment is to drop a ball and see how high it bounces.
    Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index.
    For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6,
    and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to continue
    bouncing, the distance after two bounces would be 10 ft 6 111 ft 6 ft 3.6 ft 5 25.6 ft. Note that the
    distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the
    ball comes back up. Write a program that lets the user enter the initial height
    from which the ball is dropped and the number of times the ball is allowed to
    continue bouncing. Output should be the total distance traveled by the ball.
Solution:

"""
# Input
height = int(input("Enter the height from which the ball is dropped: "))
bounce_index = float(input("Enter the bounciness of the ball: "))
number_of_bounces = float(input("Enter the number of times: "))

# calculate
distance = 0
while number_of_bounces > 0:
    distance += height
    height *= bounce_index
    distance += height
    number_of_bounces -= 1

print("The total distance traveled by the ball %d units." % distance)
