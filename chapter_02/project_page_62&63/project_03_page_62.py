"""
Author: Nguyen Xuan Tung
Date: 14/07/2021
Program: project_03_page_62.py
Problem:
    Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
    like to buy LP record albums. The store rents new videos for $3.00 a night, and
    oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
    can use to calculate the total charge for a customer’s video rentals. The program
    should prompt the user for the number of each type of video and output the total
    cost.
Solution:
    Calculate the total charge for a customer's video rentals
    1. Create constants
    - Unit price of a newVideo: new_video = 3.00
    - Unit price of a oldVideo: old_video = 2.00
    2. Inputs
    - Number of new video rentals: number_new_video
    - Number of old video rentals: number_old_video
    - Number of nights renting new video: night_new_video
    - Number of nights renting old video: night_old_video
    3. Calculator
    - Total renting new video: total_new_video = number_new_video * new_video * night_new_video
    - Total renting old video: total_old_video = number_old_video * old_video * night_old_video
    - Total renting both: total = total_new_video + total_old_video
    4. Output
    - Total cost
"""
# Create constants
new_video = 3.00
old_video = 2.00

# Inputs
number_new_video = int(input("Number of new video rentals: "))
number_old_video = int(input("Number of old video rentals: "))
night_new_video = int(input("Number of nights renting new video: "))
night_old_video = int(input("Number of nights renting old video: "))

# Calculator
total_new_video = number_new_video * new_video * \
                  night_new_video
total_old_video = number_old_video * old_video * \
                  night_old_video
total = total_new_video + total_old_video

# Output
print("Total cost: $" + str(total))