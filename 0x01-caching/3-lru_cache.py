#!/usr/bin/env python3
"""LRU caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching class"""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.lru = []

    def evict(self):
        """Evict the least recently used item in the cache (LRU)."""
        if self.lru and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.lru.pop(0)
            del self.cache_data[lru]
            print(f"DISCARD: {lru}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            self.evict()
            self.cache_data[key] = item

    def get(self, key):
        """Get the associated value of key."""
        value = self.cache_data.get(key)
        if value:
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
        return value
