"""
LRU Cache Implementation
A Least Recently Used (LRU) cache implementation using OrderedDict.
Demonstrates efficient cache management for performance optimization.
"""

from collections import OrderedDict

class LRUCache:
    """
    LRU Cache with O(1) get and put operations.
    
    Time Complexity:
        - get: O(1)
        - put: O(1)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items in cache
        """
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        """
        Get value from cache. Returns -1 if not found.
        Moves the accessed item to the end (most recently used).
        """
        if key not in self.cache:
            return -1
        
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair in cache.
        If cache is full, removes least recently used item.
        """
        if key in self.cache:
            # Update existing key - set value before moving for atomic operation
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
        
        # Remove least recently used item if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
    def __repr__(self):
        return f"LRUCache({dict(self.cache)})"

# Example usage
if __name__ == "__main__":
    cache = LRUCache(3)
    
    cache.put(1, "one")
    cache.put(2, "two")
    cache.put(3, "three")
    print(f"Cache after adding 1, 2, 3: {cache}")
    
    print(f"Get key 1: {cache.get(1)}")
    
    cache.put(4, "four")  # This will evict key 2
    print(f"Cache after adding 4: {cache}")
    
    print(f"Get key 2: {cache.get(2)}")  # Should return -1
