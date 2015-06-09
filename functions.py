#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Misc functions."""
import functools
import itertools
import math
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
    where m, n, and k are positive integers with m > n, m - n odd, and with m and n coprime.
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


def isPn(x):
    " Test if pentagonal."""
    if x == 0:
        return True
    cand = int((1 + math.sqrt(1 + 24 * x)) / 6)
    return Pn(cand) == x


def champernowne_digit(n):
    """Get Champernowne constant's n-th digit (starting from 0)."""
    # Implementation determines 3 pieces of info in that order:
    #  - the length of the number the digit belongs to : len_num
    #  - the index of the digit in the number : digit_index
    #  - the number the digit belongs to : num
    base = 10
    prev_pow = 1
    for len_num in itertools.count(1):
        nb_dig_block = len_num * (base - 1) * prev_pow
        if nb_dig_block < n:
            n -= nb_dig_block
            prev_pow *= base
        else:
            num_index, digit_index = divmod(n, len_num)
            num = prev_pow + num_index
            return int(str(num)[digit_index])


def main():
    # TODO : add more tests
    champernowne_string = ''.join(str(i) for i in range(1, 10005))
    for i, d in enumerate(champernowne_string):
        assert champernowne_digit(i) == int(d)


if __name__ == "__main__":
    main()
