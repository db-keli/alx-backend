#!/usr/bin/env python3
""" Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic caching dictionary"""

    def put(self, key, item):
        """Inserts a new cached data into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns for cached value for key"""
        return self.cache_data.get(key)
