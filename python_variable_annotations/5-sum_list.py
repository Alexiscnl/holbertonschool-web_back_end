#!/usr/bin/env python3
"""
Module for list operations with type annotations.

This module provides functions for performing operations on lists
with proper type annotations for better code clarity and type checking.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating point numbers.

    Takes a list of floats and returns their sum as a float.

    Args:
        input_list: List of floating point numbers

    Returns:
        The sum of all numbers in the list

    Example:
        >>> sum_list([3.14, 1.11, 2.22])
        6.47
    """
    return sum(input_list)
