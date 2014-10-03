#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Functions related to prime numbers decomposition in prime factors."""
import math
import collections
import itertools
import operator
import functools


def mult(iterable, start=1):
    """Returns the product of an iterable - like the sum builtin."""
    return functools.reduce(operator.mul, iterable, start)


def prime_factors(n):
    """Yields prime factors of a positive number."""
    assert n > 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            yield d
        d += 1
    if n > 1:  # to avoid 1 as a factor
        assert d <= n
        yield n


def prime_factors_list(n):
    """Returns the prime factors of a positive number as a list."""
    l = list(prime_factors(n))
    assert mult(l) == n
    return l


def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    return all(n % i for i in range(2, int(math.sqrt(n)) + 1))


def yield_primes(beg=0):
    """Yields prime number by checking them individually - not efficient."""
    for i in itertools.count(beg):
        if is_prime(i):
            yield i


def sieve(lim):
    """Computes the sieve of Eratosthenes for values up to lim included."""
    primes = [True] * (lim + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(lim)) + 1):
        if primes[i]:
            for j in range(i * i, lim + 1, i):
                primes[j] = False
    return primes


def totient(lim):
    """Computes Euler's totient for values up to lim included."""
    # http://en.wikipedia.org/wiki/Euler%27s_totient_function
    totient = list(range(lim + 1))
    totient[0] = -1
    for i in range(2, lim + 1):
        if totient[i] == i:
            for j in range(i, lim + 1, i):
                totient[j] = (totient[j] * (i - 1)) // i
    return totient


def primes_up_to(lim):
    """Uses a sieve to return primes up to lim included."""
    return (i for i, p in enumerate(sieve(lim)) if p)


def yield_divisors(n):
    """Yields distinct divisors of n."""
    # to be improved : use prime_factors
    assert n > 0
    yield 1
    if n > 1:
        yield n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                yield i
                yield n // i


def nb_divisors(n):
    """Returns the number of divisors of n."""
    return mult(c + 1
                for c in collections.Counter(
                    prime_factors(n)).values())


def nb_prime_divisors(n):
    """Returns the number of prime divisors of n."""
    return len(list(itertools.groupby(prime_factors(n))))


def main():
    limit = 1000
    primes = list(primes_up_to(limit))
    primes2 = []
    for p in yield_primes():
        if p > limit:
            break
        primes2.append(p)
    assert primes == primes2
    assert all(
        nb_divisors(p) == 2 and
        nb_prime_divisors(p) == 1 and
        prime_factors_list(p) == [p]
        for p in primes)

if __name__ == "__main__":
    main()
