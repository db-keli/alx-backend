#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching class"""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.mru = []

    def evict(self):
        """Evict the most recently used item in the cache (MRU)."""
        if self.mru and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.mru.pop()
            del self.cache_data[mru]
            print(f"DISCARD: {mru}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key in self.mru:
                self.mru.remove(key)
            if key not in self.cache_data:
                self.evict()
            self.cache_data[key] = item
            self.mru.append(key)

    def get(self, key):
        """Get the associated value of key."""
        value = self.cache_data.get(key)
        if value:
            if key in self.mru:
                self.mru.remove(key)
            self.mru.append(key)
        return value
