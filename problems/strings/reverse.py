from functools import reduce

"""
Range of implementations of the reverse a string problem
"""


def reverse1(text: str) -> str:
    """
    Reverse example 1. Using a form of list comprehension and the [::-1] shorthand to
    reverse a given array/list
    :param text:
    :return:
    """
    return ''.join(c for c in text[::-1])


def reverse2(text: str) -> str:
    """
    Using a functional paradigm to reverse a list, namely the reducer approach, where we are effectively append
    to an initial string in reverse order as we iterate over the string. In the lambda x represents
    the growing newly appended to string, and y represents the next value in the iterator.
    summary:
        x - accumulator
        y - next value in iterator
        iterator - list
        initializer - starting point of reducer to build on. Will default to none
    :param text:
    :return:
    """
    return reduce(lambda x, y: y + x, list(text), "")


def reverse3(text):
    """
    a more rudimentary approach
    :param text:
    :return:
    """
    result = ''
    for i in range(len(text), 0, -1):
        result += text[i - 1]
    return result

def reverse4(text):
    """
    a more rudimentary approach, however somewhat slower as we reverse the initially generated range
    :param text:
    :return:
    """
    result = ''
    for i in reversed(range(0, len(text))):
        result += text[i]
    return result
