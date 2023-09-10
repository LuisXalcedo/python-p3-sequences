#!/usr/bin/env python3

def print_fibonacci(length):
    cache = {0: 0, 1: 1}

    def fibonacci_of(n):
        if n in cache:  # Base case
            return cache[n]
        cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
        return cache[n]
    print([fibonacci_of(n) for n in range(length)])
