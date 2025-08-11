#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
