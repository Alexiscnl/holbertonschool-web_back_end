#!/usr/bin/env python3
"""
Module for basic arithmetic operations with type annotations.

This module provides functions for performing basic mathematical operations
with proper type annotations for better code clarity and type checking.
"""


def add(a: float, b: float) -> float:
    """
    Add two floating point numbers.

    Takes two float arguments and returns their sum as a float.

    Args:
        a: First floating point number
        b: Second floating point number

    Returns:
        The sum of a and b as a float

    Example:
        >>> add(1.11, 2.22)
        3.33
    """
    return a + b
