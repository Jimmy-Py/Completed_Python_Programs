#James Brevoort 2-22-20 introduce functions instead of relying on break and continue
# 3-7-20 Fixed errors to get running.

import math
primes = [2, 3, 5, 7]

def test_if_prime():
    for i in primes:
        if i <= threshold:
            if test % i == 0:
                return "composite"
    return "prime"  # have not found any prime factors less than squrt(test), so must be prime.


test = 10
j = 0
while True:  # change to "while True" to run infinitely or while "j > 50" for testing.
    # j += 1  # counter for test purposes.
    test += 1  # test next integer.

    threshold = int(math.trunc(test**(1 / 2)))
    result = test_if_prime()

    if result == "prime":
        # print(test, primes, threshold, result)
        primes.append(test)
        print(test)