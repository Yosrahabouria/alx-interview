#!/usr/bin/python3
"""Minimum operations algorithm"""


def minOperations(n):
    """
    Calculates min number
    """
    # check for invalid inputs
    if n is None or n < 1:
        return 0

    # initialize variables
    operations = 0
    factors = 2 # every number has a factor of 1 and itself

    # iterate through all factors of n and add them to the operations count
    while factors <= n:
        while n % factors == 0:
            operations += factors
            n //= factors
        # increment factors
        factors += 1

    # return the operations count
    return operations
