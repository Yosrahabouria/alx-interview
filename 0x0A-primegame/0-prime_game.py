#!/usr/bin/python3
"""
defines the function isWinner.
"""


def primeNumbers(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes."""
    prime_numbers = []
    is_prime = [True] * (n + 1)
    current_prime = 2
    while (current_prime * current_prime <= n):
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, n + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1
    for number in range(2, n + 1):
        if is_prime[number]:
            prime_numbers.append(number)
    return prime_numbers

def isWinner(x, nums):
    
    """Determines the winner of x rounds of a prime number game."""
    if x != len(nums):
        return None

    Ben = 0
    Maria = 0

    for n in nums:
        primes = primeNumbers(n)
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    return "Ben" if Ben > Maria else "Maria"
