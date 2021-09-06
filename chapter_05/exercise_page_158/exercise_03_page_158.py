"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: exercise_03_page_158.py
Problem:
    Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
    expressions that perform the following tasks:
    a. Replace the value at the key 'b' in data with that value’s negation.
    b. Add the key/value pair 'c':40 to data.
    c. Remove the value at key 'b' in data, safely.
    d. Print the keys in data in alphabetical order.
Solution:

"""
data = {'b': 20, 'a': 35}
# a...
value = data.get("b")
data["b"] = -value
print(data)

# b...
data.update({'c': 40})
print(data)

# c..
# data.pop('b')
print(data)

# d...
theKeys = list(data.keys())
theKeys.sort()
for key in theKeys:
    print(key, data[key])



