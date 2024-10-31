#!/usr/bin/env python3
"""LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU caching class"""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.lfu = dict()

    def evict(self):
        """Evict the least frequently used item in the cache (LFU)."""
        if self.lfu and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = sorted(self.lfu.items(), key=lambda x: x[1])[0][0]
            del self.cache_data[lfu_key]
            del self.lfu[lfu_key]
            print(f"DISCARD: {lfu_key}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lfu[key] += 1
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.lfu[key] = 1

    def get(self, key):
        """Get the associated value of key."""
        value = self.cache_data.get(key)
        if value:
            self.lfu[key] += 1
        return value
