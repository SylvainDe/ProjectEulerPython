#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Functions related to prime numbers decomposition in prime factors."""
import math
import collections
import itertools
from functions import mult


def prime_factors(n):
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
    l = list(prime_factors(n))
    assert mult(l) == n
    return l


def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in range(2, int(math.sqrt(n)) + 1))


def yield_primes(beg=0):
    for i in itertools.count(beg):
        if is_prime(i):
            yield i


def sieve(lim):
    primes = [True] * (lim + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(lim)) + 1):
        if primes[i]:
            for j in range(i * i, lim + 1, i):
                primes[j] = False
    return primes


def primes_up_to(lim):
    return (i for i, p in enumerate(sieve(lim)) if p)


def yield_divisors(n):
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
    return mult(c + 1
                for c in collections.Counter(
                prime_factors(n)).values())


def nb_prime_divisors(n):
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
    assert all(nb_divisors(p) == 2 and nb_prime_divisors(p) == 1 and prime_factors_list(p) == [p] for p in primes)

if __name__ == "__main__":
    main()
