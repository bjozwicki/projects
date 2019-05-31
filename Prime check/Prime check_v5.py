""" Prime generator
Changes:
Continuation of v3, added steps in range(), added debugging settings
AVG = 0,28s
"""

from math import sqrt
from time import time

# Debugging settings
set_number  = 100000
set_tries   = 10


def is_prime(x):

    if x < 2:
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


def prime_generator(max_number):
    count = 0

    for number in range(1, max_number + 1):
        if is_prime(number) == True:
            count += 1



    print "CNT = ", count


def time_check(tries):
    average_time = 0
    for i in range(tries):

        t0 = time()
        prime_generator(set_number)
        t1 = time()

        TE = t1 - t0
        print "TE  = ", TE
        average_time += TE

    print ""
    print "ATE = ", average_time / tries


time_check(set_tries)
