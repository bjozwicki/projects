""" Prime generator
Changes:
Rewrote prime_generator function

"""

from math import sqrt
from time import time

# Debugging settings
min_number = 1
max_number = 100

print_primes = True
print_pairs  = False
print_count  = True

set_tries = 1


def is_prime(x):
    if x == 1:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    # Maximum possible integer divisor is square root of a number
    highest_divisor = sqrt(x)

    for n in range(3, int(highest_divisor) + 1, 2):
        if x % n == 0:
            return False
    return True


def prime_generator(min_number, max_number, print_count, print_primes, print_pairs):
    count = 0

    for number in range(min_number, max_number + 1):
        if is_prime(number) == True:
            count += 1
            if print_primes == True:
                print number

        if print_pairs == True:
            print number, is_prime(number)

    if print_count == True:
        print "COUNT =", count


def time_check(tries):
    average_time = 0
    for i in range(tries):
        t0 = time()
        prime_generator(min_number, max_number, print_count, print_primes, print_pairs)
        t1 = time()

        TE = t1 - t0
        print "TE  = ", TE
        average_time += TE

    print ""
    print "ATE = ", average_time / tries

# print is_prime(7)
# prime_generator(min_number, max_number, print_count, print_primes, print_pairs)
time_check(set_tries)
