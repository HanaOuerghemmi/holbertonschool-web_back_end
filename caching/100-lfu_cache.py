#!/usr/bin/python3
''' LFU Caching: Create a class LFUCache that inherits from BaseCaching
                 and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' An LFU cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to add
        an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the least frequently used entry to
        accommodate for the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache '''

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """dictionary
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """
        Return the value linked
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value

    def findLFU(self):
        ''' Return key of least frequently used item in cache.
            If multiple items have the same amount of uses, return the least
            recently used one. '''
        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return 