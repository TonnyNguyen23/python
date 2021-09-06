"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: exercise_09_page_85.py
Problem:
    Does the Boolean expression count > 0 and total // count > 0 contain a
    potential error? If not, why not?
Solution:
    The Boolean condition does not contain any potential error. Because:
        - count > 0: not error
        - total // count > 0: // executes before >. So, I can write again it is (total // count) > 0.
        That is right.
"""