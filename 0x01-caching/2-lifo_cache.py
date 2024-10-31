#!/usr/bin/env python3
"""LIFO caching"""
from collections import deque
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching class"""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.queue = deque()

    def evict(self):
        """Evict the last item in the cache (LIFO)."""
        if self.queue and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_in = self.queue.pop()
            del self.cache_data[first_in]
            print(f"DISCARD: {first_in}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            self.evict()
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get the associated value of key."""
        return self.cache_data.get(key)
