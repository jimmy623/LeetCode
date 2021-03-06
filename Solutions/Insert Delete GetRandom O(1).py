from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.d = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
        	return False
        else:
        	self.nums.append(val)
        	self.d[val] = len(self.nums)-1
        	return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
        	index = self.d[val]
        	last = self.nums.pop()
        	if index != len(self.nums):
        		self.nums[index] = last
        		self.d[last] = index
        	del self.d[val]
        	return True
        else:
        	return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = randint(0,len(self.nums)-1)
        return self.nums[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#nsert Delete GetRandom O(1)
#https://leetcode.com/problems/insert-delete-getrandom-o1/description/