""" Prime generator
Changes:
Tested not in ["1", "3", "7", "9"]
AVG = 0,45s
"""

from math import sqrt
from time import time


def is_prime(x):

    if x < 2:
        return False

    if x > 5 and str(x)[-1] not in ["1", "3", "7", "9"]:
            return False

    # Maximum possible integer divisor is square root of a number
    highest_divisor = sqrt(x)

    for n in range(2, int(highest_divisor) + 1):
        if x % n == 0:
            return False
    return True


def prime_generator():
    count = 0
    for number in range(1, 100001):
        if is_prime(number) == True:
            #print number
            count += 1
    print "COUNT", count


def time_check():
    average_time = 0
    for i in range(10):

        t0 = time()
        prime_generator()
        t1 = time()

        TE = t1 - t0
        print "TE  = ", TE
        average_time += TE

    print ""
    print "ATE = ", average_time / 10


time_check()
