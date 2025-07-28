#!/usr/bin/env python3
"""
Module for mixed list operations with type annotations.

This module provides functions for performing operations on lists
containing mixed numeric types with proper type annotations.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Takes a list containing both integers and floats and returns
    their sum as a float.

    Args:
        mxd_lst: List containing integers and/or floating point numbers

    Returns:
        The sum of all numbers in the list as a float

    Example:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        679.13
    """
    return sum(mxd_lst)
