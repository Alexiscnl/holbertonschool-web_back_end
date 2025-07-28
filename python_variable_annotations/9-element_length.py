#!/usr/bin/env python3
"""
Module that provides functionality to calculate element lengths.

This module contains functions for working with iterables and calculating
the length of each element within them.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable.

    Takes an iterable containing sequences and returns a list of tuples
    where each tuple contains the original element and its length.

    Args:
        lst: An iterable containing sequences (strings, lists, tuples, etc.)

    Returns:
        A list of tuples where each tuple contains (element, length_of_element)

    Example:
        >>> element_length(["hello", "world"])
        [("hello", 5), ("world", 5)]
    """
    return [(i, len(i)) for i in lst]
