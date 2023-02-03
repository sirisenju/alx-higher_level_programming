#!/usr/bin/python3
"""This module is composed by a function that adds two numbers"""


def add_integer(a, b=98):
    """
        A function that adds 2 integeras.
        args:
            a: first int
            b: second int
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
