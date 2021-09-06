"""
Author: Nguyen Xuan Tung
Date: 20/07/2021
Program: project_03_page_99.py
Problem:
    Modify the guessing-game program of Section 3.5 so that the user thinks of a
    number that the computer must guess. The computer must make no more than
    the minimum number of guesses, and it must prevent the user from cheating by
    entering misleading hints. (Hint: Use the math.log function to compute the minimum
    number of guesses needed after the lower and upper bounds are entered.)
Solution:

"""
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

count = 0

print()
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print(smaller, larger)
    print('Your number is %d' % myNumber)
    choice = input('Enter =, <, or >: ')
    if choice == '=':
        print("Hooray, I've got it in %d tries" % count)
        break
    elif smaller == larger:
        print("I'm out of guesses, and you cheated")
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1
