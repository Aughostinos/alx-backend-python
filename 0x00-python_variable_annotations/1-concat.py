#!/usr/bin/env python3
"""Task 1. Basic annotations - concat"""


def concat(str1: str, str2: str) -> str:
    """ a type-annotated function concat that takes a string str1 and a
    string str2 as arguments and returns a concatenated string"""
    return "{} {}".format(str1, str2)