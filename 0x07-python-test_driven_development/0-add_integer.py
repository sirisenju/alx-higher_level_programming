#!/usr/bin/python3
"""This module is composed by a function that adds two numbers"""


def add_integer(a, b=98):
    """
        A function that adds 2 integeras.
        args:
            a: first int
            b: second int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
