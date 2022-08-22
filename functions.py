#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Misc functions."""
import functools
import itertools
import math
from prime import yield_divisors


def ceil(n):
    """ Returns the ceiling of x as an int."""
    return int(math.ceil(n))


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


def xgcd(a,b):
    """Computes the extended gcd."""
    # http://anh.cs.luc.edu/331/notes/xgcd.pdf
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy


def modinv(a, m):
    """Computes the Modular multiplicative inverse."""
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


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
    # s is (m+n), mk is m*k, mks is m*k*s, etc
    mks = p // 2
    for m in yield_divisors(mks):
        ks = mks // m
        if ks >= m + 1:
            for k in yield_divisors(ks):
                s = ks // k
                n = s - m
                if 0 < n < m and s % 2 and gcd(m, n) == 1:
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


def polygonal(k, n):
    """ Polygonal numbers - https://en.wikipedia.org/wiki/Polygonal_number """
    return n + (k - 2) * n * (n - 1) // 2


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
    for n in range(1, 100):
        triplets = list(yield_pythagorean_triples_of_peri(n))
        for a, b, c in triplets:
            assert a + b + c == n
            assert a * a + b * b == c * c
            assert 0 < a < c
            assert 0 < b < c
        assert len(triplets) == len(set(triplets)), n
    for n in range(1, 100):
        assert Tn(n) == polygonal(3, n)
        assert Pn(n) == polygonal(5, n)
        assert Hn(n) == polygonal(6, n)


if __name__ == "__main__":
    main()
