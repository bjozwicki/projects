""" Prime generator
Changes:
Basic prime check
AVG = 128,0s
"""


from math import sqrt
from time import time


def is_prime(x):

    if x < 2:
        return False

    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def prime_generator():
    count = 0
    for number in range(1, 100001):
        if is_prime(number) == True:
            count += 1


def time_check():
    average_time = 0
    for i in range(1):

        t0 = time()
        prime_generator()
        t1 = time()

        TE = t1 - t0
        print "TE  = ", TE
        average_time += TE
        
    print "ATE = ", average_time / 1

time_check()
