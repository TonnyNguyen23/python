"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: project_06_page_165.py
Problem:
   Define a function decimalToRep that returns the representation of an integer in a
    given base. The two arguments should be the integer and the base. The function
    should return a string. It should use a lookup table that associates integers with
    digits. Include a main function that tests the conversion function with numbers
    in several bases.
Solution:

"""


def decimalToRep(num, base):
    result = ""
    while num > 0:
        rem = num % base
    if rem in range(10):
        result += str(rem)
    else:
        # If the base is 16 then only it comes to else statement
        result += chr(65 + (rem % 10))
        num = num // base
        result = result[::-1]
    if result == "":
        return '0'
    return result


def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))
    main()
