"""
Author: Nguyen Xuan Tung
Date: 01/08/2021
Program: exercise_03_page_109.py
Problem:
    You are given a string that was encoded by a Caesar cipher with an unknown distance value.
    The text can contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.
Solution:
    Printable ASCII characters range from 32 (decimal value) to 126 (if we consider spaces, otherwise from 33 to 126)
    The main shortcoming of this encryption strategy is that the plaintext is encrypted one character at
    a time, and each encrypted character depends on that single character and a fixed distance
    value.
"""