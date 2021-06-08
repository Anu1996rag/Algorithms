""" Given 2 strings , write a method to decide if one string is permutation of the other. """

import unittest
from collections import Counter


def check_permutation_pythonic(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) != sorted(s2):
        return False
    return True

