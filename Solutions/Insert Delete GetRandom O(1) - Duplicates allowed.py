from collections import defaultdict
from random import randint
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.d = defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.d[val].add(len(self.nums)-1)
        if len(self.d[val]) == 1:
            return True
        else:
            return False
        
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.d[val]:
            return False
        index = self.d[val].pop()
        last = self.nums.pop()
        if index != len(self.nums):
            self.d[last].remove(len(self.nums))
            self.d[last].add(index)
            self.nums[index] = last
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        i = randint(0,len(self.nums)-1)
        return self.nums[i]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
#Insert Delete GetRandom O(1) - Duplicates allowed
#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/