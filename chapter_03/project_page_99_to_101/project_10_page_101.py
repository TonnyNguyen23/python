"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_10_page_101.py
Problem:
    The credit plan at TidBit Computer Store specifies a 10% down payment and
    an annual interest rate of 12%. Monthly payments are 5% of the listed purchase
    price, minus the down payment. Write a program that takes the purchase price
    as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain
    the following items:
    • the month number (beginning with 1)
    • the current total balance owed
    • the interest owed for that month
    • the amount of principal owed for that month
    • the payment for that month
    • the balance remaining after payment
    The amount of interest for a month is equal to balance * rate / 12. The amount of
    principal for a month is equal to the monthly payment minus the interest owed.
Solution:

"""
inital_price = float(input("Enter the Price of the Computer: "))
month = 0
an_interest = (inital_price - inital_price * .10) * .01 / 12
monthly_payment = (inital_price - inital_price * .10) * 0.05
principal = monthly_payment - an_interest

print("%0s%20s%20s%20s%13s%23s" % ("Month", "Current Balance",
                                   "Interest Owed", "Principal Owed", "Payment", "Balance Remaining"))

while monthly_payment >= 0:
    month += 1
    inital_price = inital_price - inital_price * .10
    balance = inital_price + an_interest - monthly_payment

    print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" % (
        month, inital_price, an_interest, principal, monthly_payment, balance))

    if balance <= 0:
        break
