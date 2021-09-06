"""
Author: Nguyen Xuan Tung
Date: 08/08/2021
Program: exercise_03_page_146.py
Problem:
    What is a mutator method? Explain why mutator methods usually return the
    value None.
Solution:
    - Mutator method is Mutable objects (such as lists) have some methods devoted
    entirely to modifying the internal state of the object.
    - Because a change of state is all that is desired, a mutator method usually returns no value of interest to the
     caller (but note that pop is an exception to this rule). Python nevertheless automatically returns the special
     value None even when a method does not explicitly return a value.
"""