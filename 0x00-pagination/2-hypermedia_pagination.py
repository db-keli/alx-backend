#!/usr/bin/env python3
"""2. Hypermedia pagination"""


import csv
import math
from typing import List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary of:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page (equivalent to return from previous task)
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset as an
            integer
        """
        page_with_data = self.get_page(page, page_size)
        dataset_len = len(self.dataset())
        hyper_data_dict = {
            'page_size': len(page_with_data),
            'page': page,
            'data': page_with_data,
            'next_page': page + 1 if dataset_len > page * page_size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(dataset_len / page_size)
        }
        return hyper_data_dict
