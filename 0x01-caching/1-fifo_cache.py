#!/usr/bin/env python3
"""FIFO caching"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.queue = deque()

    def evict(self):
        """Evict the first item in the cache (FIFO)."""
        if self.queue and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_in = self.queue.popleft()
            print(f"DISCARD: {first_in}")
            del self.cache_data[first_in]

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            self.evict()
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get the associated value of key."""
        return self.cache_data.get(key)
