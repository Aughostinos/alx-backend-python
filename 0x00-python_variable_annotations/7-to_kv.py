#!/usr/bin/env python3
"""Task 7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a type-annotated function to_kv that returns a tuple."""
    return k, float(v ** 2)
