""" Twin Primes generator

Inputs list of positive integers
Outputs prime pairs with set gap in between them. 

ETA (print / don't print)
Twin  : 0,38/0,32
Cousin: 0,38/0,32
Sexy  : 0,45/0,32

TODO:
use wikipedia formulas for possible optimization
try listing and then selecting, so to not check second prime twice (as in 11,13 and 13,15)
note that second prime is not a first prime later
"""

from math import sqrt
from time import time

# Debugging settings
min_number = 1
max_number = 100000
""" Set gap size:
2 for twin primes
4 for cousin primes
6 for sexy primes """
gap = 2
print_primes = False



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



def prime_generator(min_number, max_number, gap, print_primes):
    t0 = time()
    count = 0
    number = min_number

    while number < max_number:

        if is_prime(number) == True:

            if is_prime(number + gap) == True:  # Twin check
                count += 1
                
                if print_primes == True:
                    print count, "|", number, number + gap

            if number != 2:
                number += 2  # Omit even number in between
            else:
                number += 1  #Single case, as 3 is also prime
                
        else:
            number += 1    

    print ""
    print "Final count : ", count

    t1 = time()
    print "Time elapsed: ", t1 - t0

prime_generator(min_number, max_number, gap, print_primes)