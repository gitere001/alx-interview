#!/usr/bin/python3
"""This module contains the function minOperations."""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to transform the input
    integer 'n'.
    Takes an integer 'n' as input and returns the total number of operations
    performed.
    """
    if n <= 1:
        return 0
    divisor = 2
    operations = 0
    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            operations = operations + divisor
        else:
            divisor += 1
    return operations
