#!/usr/bin/env python3
"""1. Simple pagination"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate dataset correctly and
        return the appropriate page of the dataset (i.e. the correct
        list of rows).
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start_index, end_index = self.index_range(page, page_size)
        if start_index < 0 or end_index > len(self.dataset()):
            return []
        return self.dataset()[start_index:end_index]
