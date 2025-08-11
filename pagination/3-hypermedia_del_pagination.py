#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0

        Returns:
            Dict[int, List]: A dictionary with index as key and data row
                           as value, limited to first 1000 entries
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve hypermedia pagination information with deletion resilience.

        Args:
            index (int): The start index of the current page. Default is None.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            dict: A dictionary containing:
                - index (int): The current start index of the return page
                - data (List[List]): The actual page of the dataset
                - page_size (int): The current page size (length of data)
                - next_index (int): The next index to query with

        Raises:
            AssertionError: If index is not a valid integer or out of range
        """
        assert isinstance(index, int) and index is not None
        assert 0 <= index < len(self.dataset())

        data = []
        current_index = index
        collected = 0
        indexed_data = self.indexed_dataset()

        while collected < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current_index
        }
