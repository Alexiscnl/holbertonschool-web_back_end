#!/usr/bin/env python3
"""
Module for function factory operations with type annotations.

This module provides functions that return other functions
with proper type annotations for better code clarity and type checking.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Takes a multiplier value and returns a function that multiplies
    its input by that multiplier.

    Args:
        multiplier: The value to multiply by

    Returns:
        A function that takes a float and returns the product

    Example:
        >>> multiply_by_2 = make_multiplier(2.22)
        >>> multiply_by_2(2.22)
        4.928400000000001
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
