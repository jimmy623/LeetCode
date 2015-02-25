import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.usage = collections.deque()
        self.dict = {}

    # @return an integer
    def get(self, key):
        if key in self.dict:
            self.usage.remove(key)
            self.usage.append(key)
            return self.dict[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            self.dict[key] = value
            self.usage.remove(key)
            self.usage.append(key)
        else:
            if len(self.dict) == self.capacity:
                x = self.usage.popleft()
                del self.dict[x]
            self.dict[key] = value
            self.usage.append(key)
                
        
        
        
        
        
#LRU Cache
#https://oj.leetcode.com/problems/lru-cache/