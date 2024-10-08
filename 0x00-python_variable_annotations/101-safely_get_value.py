#!/usr/bin/env python3
"""Task 10. Duck typing - first element of a sequence"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return values,
    addtype annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
