# Arithmetic Practice 2.1 James B 7-27-19.
# 2.0 Changes: Random operation, keeps track of score, and execution of operation choice moved from main() to compute_number().
# As a result compute_number() now tells display_number() what operation it used.
#
# 2.1:
# (1) make integer answers for division() acceptable for the answers that are integers e.g., 5/1 = 5, not necessarily 5.0
# (2) allow .5 as an acceptable answer (instead of only 0.5)
# (3) Display fractions as
#  A
# ---
#  B

# 2.2 Adding a multiples of Z mode, to practice times tables.
# 2.3 includes a successive powers of an integer mode. (Perhaps next can have a random exponent
# mode that keeps values below a user-set threshold. 8-3-19
# 2.3.1 Trim out 2 lines of code I realized didn't need to exist in the main() under choice 6.

import random

def choose_operation():
    """get user's choice of operation"""
    user_operation = input(
        """
        Please choose among:

        1 for +
        2 for -
        3 for *
        4 for /
        5 for Random Arithmetic Operations
        6 for Successive Multiples of an Integer
        7 for Successive Powers of an Integer

        Your choice: """)
    return int(user_operation)

def choose_length():
    """get user input for length of numbers."""
    length_a = input("In the expression A [operation] B, how many digits long would you like A to be? ")
    length_b = input("... and how long would you like B to be? ")
    print(" ")
    return length_a, length_b

def generate_numbers(length_a, length_b):
    a_leading = str(random.randint(1, 9))

    a_trailing = ""
    for i in range(int(length_a) - 1):
        a_trailing += str(random.randint(0, 9))

    a = a_leading + a_trailing

    # Make number b
    b_leading = str(random.randint(1, 9))

    b_trailing = ""
    for i in range(int(length_b) - 1):
        b_trailing += str(random.randint(0, 9))

    b = b_leading + b_trailing

    return a, b

def compute_answer(a, b, user_operation):
    """Compute the answer to the chosen problem, including in 'random operation mode' """
    if user_operation == 1:
        return int(a) + int(b), "+"
    elif user_operation == 2:
        return int(a) - int(b), "-"
    elif user_operation == 3:
        return int(a) * int(b), "*"
    elif user_operation == 4:
        quotient = str(int(a) / int(b))

        c = 0
        for i in quotient:
            if i == "." and quotient[c + 1] == "0":
                return quotient[:c], "/"  # only returns "5" in "5.0" for example.

            elif i == ".":
                return quotient[:c + 2], "/"  # returns "3.1" from "3.14" for example.

            else:
                c += 1

    elif user_operation == 5:
        random_operation = random.randint(1, 4)

        if random_operation == 1:
            return int(a) + int(b), "+"
        elif random_operation == 2:
            return int(a) - int(b), "-"
        elif random_operation == 3:
            return int(a) * int(b), "*"
        elif random_operation == 4:
            quotient = str(int(a) / int(b))

            c = 0
            for i in quotient:
                if i == "." and quotient[c + 1] == "0":
                    return quotient[:1], "/"  # only returns "5" in "5.0" for example.

                elif i == ".":
                    return quotient[:c + 2], "/"  # returns "3.1" from "3.14" for example.

                else:
                    c += 1

    elif user_operation == 7:
        return a**b, "^"

    else:
        print("JB_error: compute_answer()")

def display_problem(a, b, given_operation):
    if given_operation == "/":
        print("", a, "\n---\n", b)

    else:
        print(a, given_operation, b)

def generate_random_operation(user_operation):
    if user_operation == 5:
        return random.randint(1, 4)


def main():
    total_correct = 0
    in_a_row = 0
    while True:
        print("Total:", total_correct, "|", "In-a-Row:", in_a_row, " ")
        user_operation = choose_operation()

        if int(user_operation) <= 5:
            length_a, length_b = choose_length()
            while True:
                a, b = generate_numbers(length_a, length_b)
                computed_answer, given_operation = compute_answer(a, b, user_operation)
                display_problem(a, b, given_operation)
                # print(computed_answer)  # for debugging. This one is so useful, just leave it here.
                user_answer = input("Your answer: ")
                if user_answer == "exit":
                    break
                while str(computed_answer) != user_answer and user_answer != (str(computed_answer))[1:]:
                    # Makes sure that user answer is correct, allowing leading with zero or just "."
                    in_a_row = 0
                    user_answer = input("Sorry that's not correct, try again: ")
                    if user_answer == "exit":
                        break
                if user_answer == "exit":
                    break
                in_a_row += 1
                print("\nSuccess!")
                total_correct += 1
                print("Total:", total_correct, "|", "In-a-Row:", in_a_row, "\n")

        elif int(user_operation) == 6:
            a = int(input("What number would you like to practice the multiples of?: "))

            i = 1
            while True:
                print("Total:", total_correct, "|", "In-a-Row:", in_a_row, "\n")
                i += 1
                computed_answer = str(a * i)
                display_problem(a, i, "*")
                user_answer = input("Answer: ")

                if user_answer == "show me":
                    in_a_row = 0
                    print("Answer:", computed_answer)
                    input("\nPress enter to continue.\n")
                    continue

                while user_answer != computed_answer and user_answer != "show me" and user_answer != "exit":
                    in_a_row = 0
                    user_answer = input("sorry, that's not correct. Please try again, or type 'show me': ")
                    if user_answer == "show me":
                        print("Answer:", computed_answer)
                        input("\nPress enter to continue.")

                if user_answer == "exit":
                    break

                if user_answer == "show me":
                    continue

                in_a_row += 1
                print("\nSuccess!")
                total_correct += 1

        elif int(user_operation) == 7:
            a = int(input("What number would you like to practice the powers of?: "))

            i = 1
            while True:
                print("Total:", total_correct, "|", "In-a-Row:", in_a_row, "\n")
                i += 1
                computed_answer = str(a**i)
                display_problem(a, i, "^")
                user_answer = input("Your answer: ")

                if user_answer == "show me":
                    in_a_row = 0
                    print("Answer:", computed_answer)
                    input("\nPress enter to continue.\n")
                    continue

                while user_answer != computed_answer and user_answer != "exit" and user_answer != "show me":
                    in_a_row = 0
                    user_answer = input("sorry, that's not correct. Please try again, or type 'show me': ")
                    if user_answer == "show me":
                        print("Answer:", computed_answer)
                        input("\nPress enter to continue.")

                if user_answer == "exit":
                    break

                if user_answer == "show me":  # Skip over increasing in_a_row, because user must have used "show me."
                    continue

                in_a_row += 1
                print("\nSuccess!")
                total_correct += 1









main()