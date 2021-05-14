# to implement an algorithm to determine if the string has all the unique characters
import time
import unittest
from collections import defaultdict


def is_unique_characters_pythonic(string : str) -> bool:
    return len(list(set(string))) == len(string)

# assuming the given characters are ASCII character set
# Time Complexity : O(n) or o(c) where c is the character set length
# Space Complexity : o(1)
def is_unique_algorithmic(string: str) -> bool:
    if len(string) > 128 :
        return False
    
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # character is already there
            return False
        char_set[val] = True
    return True

# we can reduce the space usage by the factor of 8 by using bit vector
def is_unique_bit_vector(string: str) -> bool:
    if len(string) > 128:
        return False
    
    checker = 0
    for char in string:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True

# using hash table or dictionary in python
def is_unique_using_dict(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True

# using time complexity O(n log n)
def is_unique_sorting(string: str):
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True



class Test(unittest.TestCase):
    test_cases = [
        ("a3evw",True),
        ("",True),
        ("23ds2",False),
        ("hb ()ce)",False),
        ("".join([chr(val) for val in range(128)]),True),
        ("".join([chr(val // 2) for val in range(129)]),True)
    ]

    test_functions = [
        is_unique_characters_pythonic,
        is_unique_algorithmic,
        is_unique_bit_vector,
        is_unique_using_dict,
        is_unique_sorting
    ]

    def test_is_unique_chars(self):
        num_runs = 100
        func_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique in self.test_functions:
                    start = time.perf_counter()

                    assert(is_unique(text) == expected),f"{is_unique.__name__} failed for value: {text}."
                    func_runtimes[is_unique.__name__] += (time.perf_counter() - start) * 1000
        
        print(f"\n{num_runs} runs...")
        for function_name, runtimes in func_runtimes.items():
            print(f"{function_name} : {runtimes:1.f} ms")