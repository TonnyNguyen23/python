"""
Author: Nguyen Xuan Tung
Date: 02/09/2021
Program: project_09_page_204.py
Problem:
    Write a program that computes and prints the average of the numbers in a text
    file. You should make use of two higher-order functions to simplify the design.
Solution:

"""


def main():
    fileName = input("Enter the file name: ")
    total = 0
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            for num in line.strip().split():
                total += float(num)
                count += 1
        print("\nThe average is " + str(total / count))


if __name__ == '__main__':
    main()
