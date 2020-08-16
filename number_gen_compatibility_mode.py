# Number Gen, Version 3
# Generator random(ish) strings of numbers for practicing memory techniques.
# 3-17-19 JB
# Version 3: ask users to give the reverse order of their digits after giving original order.

import random
import subprocess as sp  # (to be used for clearing the screen of previous text).

# Establish global variables.
total = 0
row = 0

# Clear screen of previous text.
print("\n" * 80)

# Welcome user.
input("\n\t\tWelcome to Number Generator")

# Ask the user how many digits long they would like their string.
length = int(input("how long many digits long would you like your strings?: "))

def main():
    global total, row

    # Make comp_num.
    comp_num = ""  # establish variable to be added to over for loop.
    for i in range(length):
        comp_num += str(random.randint(0, 9))

    # Display comp_num.
    print("\n" * 80)
    print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
    input(comp_num)

    # Ask user for user_num.
    print("\n" * 80)
    print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
    user_num = input("What was your number?\n")

    # Test user_num against comp_num. If correct, skip loop.
    while user_num != comp_num:
        row = 0
        print("\n" * 80)
        print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
        user_num = input('sorry that\'s not correct. type "show me" or try again:\n')
        if user_num == "show me":
            input(comp_num)  # show comp_num, and clear after 'enter'
            print("\n" * 80)
            print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
            user_num = input("enter your number (again):\n")

    # Award 1 in-a-row points, and 1 total-problems points for correct entry of comp_num.
    print("\n" * 80)
    total += 1
    row += 1
    print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
    input("success\n")

    # Ask user for reverse order of digits.
    print("\n" * 80)
    print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
    comp_num_rev = comp_num[::-1]
    user_num = input("What was the REVERSE-order of your number?\n")

    # Test user answer for reverse order of digits, if correct skip loop.
    while user_num != comp_num_rev:
        print("\n" * 80)
        row = 0  # reset the correct-answers-in-a-row score back to 0.
        print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))  # display current progress.
        user_num = input('sorry that\'s not correct. type "show me" or try again:\n')
        if user_num == "show me":
            input(comp_num_rev)  # show comp_num_rev, and clear after 'enter'
            print("\n" * 80)  # clear_comp_num_rev
            print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
            user_num = input("enter your REVERSE-number (again):\n")

    # Award 1 in-a-row points, and 1 total-problems points for correct entry of comp_num_rev.
    print("\n" * 80)
    total += 1
    row += 1
    print("Total: " + str(total) + "\t|\t" + "Row: " + str(row))
    input("success\n")

while True:
    main()