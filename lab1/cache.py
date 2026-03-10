from collections import OrderedDict

class LRUCache:
    
    def __init__(self, capacity: int=10) -> None:
        """
        Initialize LRU cache with given capacity.
        """
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        
        self.capacity = capacity 
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        """
        Get value by key and mark as recently used.
        """
        if key not in self.cache:
            return ""
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: str, value: str) -> None:
        """
        Set key-value pair. If key exists, update value and mark as recent.
        If cache is full, remove least recently used item.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return
        
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

    def rem(self, key: str) -> None:
        """
        Remove key from cache if it exists.
        """
        if key in self.cache:
            del self.cache[key]
            
    def __len__(self) -> int:
        return len(self.cache)
    
    def clear(self) -> None:
        self.cache.clear()
    
    def __contains__(self, key) -> bool:
        return key in self.cache
    
    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={len(self.cache)})"