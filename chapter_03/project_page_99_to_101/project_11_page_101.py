"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_11_page_101.py
Problem:
    In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
    the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible,
    a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
    on. A little mathematical analysis reveals that there are not enough ways to win
    to make the game worthwhile; however, because many people’s eyes glaze over
    at the first mention of mathematics, your challenge is to write a program that
    demonstrates the futility of playing the game. Your program should take as input
    the amount of money that the player wants to put into the pot, and play the game
    until the pot is empty. At that point, the program should print the number of
    rolls it took to break the player, as well as maximum amount of money in the pot.
Solution:

"""
import random


def sumDots():
    first = random.randint(1, 6)  # Produces a random number for first dice
    second = random.randint(1, 6)  # Produces a random number for second dice
    return first + second  # Returns the total roll


def get_input(valueError=None):  # Getting the input from the user
    while True:
        amount = input("How much money would you like to put in?:")  # Taking input
        try:
            amm = int(amount)  # Converts it to a integer
            if amm <= 0:
                print("Invalid number, greater than zero please")  # Letting user know that they cannot use any
                # negative number or 0
                continue
            return amm
        except valueError:  # if not given an integer as input, repeat something
            print("Invalid number, greater than zero please")
            continue


initial = get_input()  # Gets input
total = initial  # The initial pot value to a total value
rolls = 0
maxi = initial
print("Number of Rolls\t\t Win or Loss \t\t Current Value of the Pot")  # This is the model

while total > 0:
    dices = sumDots()  # roll the two dices
    rolls += 1  # Counts the number of rolls
    result = ""  # Win or Loss
    if dices == 7:  # Winning will add $4
        total = total + 4
        result = "Win"
    else:  # If loss we will reduce $1
        total = total - 1
        result = "Loss"
    if maxi < total:
        maxi = total
    print(rolls, "\t\t\t\t\t", result, "\t\t\t\t\t", total)  # Print results

print("\n\nThe maximum amount in pot was $", maxi)
