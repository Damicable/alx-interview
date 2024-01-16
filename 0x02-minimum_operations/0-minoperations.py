#!/usr/bin/python3
"""Minimum calculation operations module"""


def minOperations(n):
    """
    minOperations - A function that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    @n: The number of H characters
    Returns: 0, otherwise the fewest number of operations
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    min_ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            min_ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return min_ops
