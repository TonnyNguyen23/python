"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_08_page_85.py
Problem:
    The variables x and y refer to numbers. Write a code segment that prompts the user for
    an arithmetic operator and prints the value obtained by applying that operator to x and y.
Solution:

"""
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
op = input("Enter an arithmetic operator: ")

result = 0
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y
elif op == "%":
    result = x % y
else:
    print("Invalid!")

print(x, op, y, " = ", result)
