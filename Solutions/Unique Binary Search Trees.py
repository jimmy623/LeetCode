class Solution:
    # @return an integer
    def numTrees(self, n):
        if n < 2:
            return 1
        if n == 2:
            return 2
    
        self.data = {}
        if n in self.data:
            return self.data[n]
        
        result = 0
        for i in range(n):
            result += (self.numTrees(i) * self.numTrees(n-i-1))
        self.data[n] = result    
        return result

#Unique Binary Search Trees
#https://oj.leetcode.com/problems/unique-binary-search-trees/