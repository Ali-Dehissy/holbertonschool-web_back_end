#!/usr/bin/python3
"""LIFO CACHING"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A lifo cache class that inherits from base"""

    def __init__(self):
        """Inisitializing instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key/value pair to cache data"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return value stored in `key` key of cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
