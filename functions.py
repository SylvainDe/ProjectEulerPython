#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Misc functions."""
import functools


def fibo(f=1, g=1):
    while True:
        yield f
        f, g = g, f + g


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return functools.reduce(lcm, args)
