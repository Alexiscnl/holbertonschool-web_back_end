#!/usr/bin/env python3
"""
Module for mathematical floor operations with type annotations.

This module provides functions for performing floor operations
with proper type annotations for better code clarity and type checking.
"""


def floor(n: float) -> int:
    """
    Return the floor of a floating point number.

    Takes a float argument and returns the largest integer less than
    or equal to the input.

    Args:
        n: Floating point number to floor

    Returns:
        The floor of n as an integer

    Example:
        >>> floor(3.14)
        3
    """
    return int(n)
