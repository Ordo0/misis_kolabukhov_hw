class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self._cache = {}

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, new_elem):
        if len(self._cache) >= self.limit:
            self.remove_oldest_element()
        self._cache[new_elem] = True

    def remove_oldest_element(self):
        oldest_element = next(iter(self._cache))
        del self._cache[oldest_element]

    def get_cache(self):
        return list(self._cache.keys())


# example
cache = LRUCache(3)

cache.cache = "Element 1"
cache.cache = "Element 2"
cache.cache = "Element 3"

print(cache.get_cache())

cache.cache = "Element 4"

print(cache.get_cache())