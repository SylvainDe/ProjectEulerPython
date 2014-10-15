#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Misc functions."""
import functools
from prime import yield_divisors


def fibo(f=1, g=1):
    """Yields Fibonacci numbers."""
    while True:
        yield f
        f, g = g, f + g


def gcd(a, b):
    """Computes gcd for 2 numbers."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes lcm for 2 numbers."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Computes lcm for numbers."""
    return functools.reduce(lcm, args)


def yield_pythagorean_triples_of_peri(p):
    """ http://en.wikipedia.org/wiki/Pythagorean_triple
    a = k . (m^2 - n^2), b = k . (2mn), c = k . (m^2 + n^2)
    where m, n, and k are positive integers with m > n, m − n odd, and with m and n coprime.
    p = 2mk . (m + n)."""
    if p % 2:
        return
    prod = p // 2
    for k in yield_divisors(prod):
        prod1 = prod // k
        for m in yield_divisors(prod1):
            prod2 = prod1 // m
            n = prod2 - m
            if 0 < n < m and prod2 % 2 and gcd(m, n) == 1:
                m2, n2 = m * m, n * n
                a, b, c = k * (m2 - n2), 2 * k * m * n, k * (m2 + n2)
                yield a, b, c


def Tn(n):
    """ Triangular numbers."""
    return n * (n + 1) // 2


def Pn(n):
    """ Pentagonal numbers."""
    return n * (3 * n - 1) // 2


def Hn(n):
    """ Hexagonal numbers."""
    return n * (2 * n - 1)


def main():
    pass  # TODO : add tests

if __name__ == "__main__":
    main()
