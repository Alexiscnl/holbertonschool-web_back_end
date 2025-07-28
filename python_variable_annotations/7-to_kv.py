#!/usr/bin/env python3
"""
Module for key-value operations with type annotations.

This module provides functions for creating key-value pairs
with proper type annotations for better code clarity and type checking.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string key and the square of a numeric value.

    Takes a string and a numeric value, returns a tuple containing
    the string and the square of the numeric value.

    Args:
        k: String key
        v: Numeric value (int or float)

    Returns:
        Tuple containing the string key and the square of v as a float

    Example:
        >>> to_kv("eggs", 3)
        ("eggs", 9)
        >>> to_kv("school", 0.02)
        ("school", 0.0004)
    """
    return (k, v ** 2)
