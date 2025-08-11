#!/usr/bin/env python3
"""
Simple pagination implementation for paginating a database of popular baby names.
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: The cached dataset without header row
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of rows for the requested page, or empty list
                       if page is out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(data):
            return []

        return data[start:end]


def index_range(page, page_size):
    """
    Calculate start and end indices for pagination.

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing (start_index, end_index) corresponding to
               the range of indexes to return in a list for the given pagination
               parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
