class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # s = 0
        self.sums = [0 for i in xrange(len(self.nums)+1)]
        self.end = 0
        # for n in nums:
        # 	s += n
        # 	self.sums.append(s)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        # oVal = self.nums[i]
        # diff = val -oVal
        self.nums[i] = val
        self.end = min(self.end,i)
        # for k in xrange(i+1,len(self.sums)):
        # 	self.sums[k] += diff
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if j+1 > self.end:
        	s = self.sums[self.end]	
        	for k in xrange(self.end+1,j+2):
        		s += self.nums[k-1]
        		self.sums[k] = s
        	self.end = j+1
        return self.sums[j+1] - self.sums[i]
        # return sum(self.nums[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


#Range Sum Query - Mutable
#https://leetcode.com/problems/range-sum-query-mutable/description/