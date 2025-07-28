#!/usr/bin/env python3
"""
Module for string operations with type annotations.

This module provides functions for performing string operations
with proper type annotations for better code clarity and type checking.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Takes two string arguments and returns their concatenation.

    Args:
        str1: First string to concatenate
        str2: Second string to concatenate

    Returns:
        The concatenated string

    Example:
        >>> concat("egg", "shell")
        "eggshell"
    """
    return str1 + str2
