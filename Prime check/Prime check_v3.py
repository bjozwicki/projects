""" Prime generator
Changes:
Incorporated checks if number is divisible by 2 or 5
AVG = 0,40s
"""

from math import sqrt
from time import time


def is_prime(x):

    if x < 2:
        return False

    if x % 2 == 0 and x > 2:
        return False

    if x % 5 == 0 and x > 5:
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
    print count


def time_check():
    average_time = 0
    for i in range(10):

        t0 = time()
        prime_generator()
        t1 = time()

        TE = t1 - t0
        print "TE  = ", TE
        average_time += TE
        
    print "ATE = ", average_time / 10


time_check()
