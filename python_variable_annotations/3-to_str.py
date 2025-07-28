#!/usr/bin/env python3
"""
Module for type conversion operations with type annotations.

This module provides functions for converting between different types
with proper type annotations for better code clarity and type checking.
"""


def to_str(n: float) -> str:
    """
    Convert a floating point number to its string representation.

    Takes a float argument and returns its string representation.

    Args:
        n: Floating point number to convert

    Returns:
        String representation of the float

    Example:
        >>> to_str(3.14)
        "3.14"
    """
    return str(n)
