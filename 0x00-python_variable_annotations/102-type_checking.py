#!/usr/bin/env python3
"""Task 12. Type Checking"""
from typing import Tuple, List

 
def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """fix error: Incompatible types in assignment
    (expression has type "List[Any]", variable has type "Tuple[Any, ...]")"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)