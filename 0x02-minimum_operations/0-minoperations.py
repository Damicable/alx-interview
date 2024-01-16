#!/usr/bin/python3
"""Minimum calculation operations module"""


def minOperations(n):
    """
    minOperations - A function that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    @n: The number of H characters
    Returns: 0, otherwise int the fewest number of operations
    """
    if n <= 1:
        return 0

    # Initialize factors list
    factors = []

    # Find prime factors of n
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Calculate minimum operations
    min_operations = sum(factors)

    return min_operations


if __name__ == "__main__":
