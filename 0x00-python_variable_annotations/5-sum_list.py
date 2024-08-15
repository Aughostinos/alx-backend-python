#!/usr/bin/env python3
"""Task 5. Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a type-annotated function sum_list which takes a list input_list of floats as
    argument and returns their sum as a float."""
    sum: float = 0
    for element in input_list:
        sum += element
    return sum
