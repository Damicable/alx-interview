#!/usr/bin/python3
"""Calculation operations"""


def minOperations(n):
    """
    minOperations - A function that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    @n: The number ofOerations needed.
    Returns: 0 if n is impossible
    """
    if n == 1:
        return 0

    # Initialize an array to store the minimum number of operations for each value of i
    val = [float('inf')] * (n + 1)
    val[1] = 0  # Base case

    # Iterate from 2 to n
    for i in range(2, n + 1):
        if n % i == 0:
            # If i is a divisor of n, calculate the minimum number of operations
            for j in range(2, i + 1):
                if i % j == 0:
                    val[i] = min(val[i], val[j] + (i // j))

    return val[n] if val[n] != float('inf') else 0
