#James Brevoort 2-22-20 introduce functions instead of relying on break and continue
# 3-7-20 Fixed errors to get running.
# 3.0 Adding function to test efficiency of different algorithms.
# Middle efficient: diving all previously found primes into the test number (not square root of test number)

import math, time
start_time = time.perf_counter()
primes = [2, 3, 5, 7]

def test_if_prime():
    for i in primes:
        if test % i == 0:
            return "composite"
    return "prime"  # have not found any prime factors less than squrt(test), so must be prime.


test = 10
while test < 100_000:  # change to "while True" to run infinitely.
    test += 1  # test next integer.

    result = test_if_prime()

    if result == "prime":
        # print(test, primes, threshold, result)
        primes.append(test)
        print(test)

print("Total calculation time: ", time.perf_counter() - start_time)