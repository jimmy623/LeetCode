class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        s = 0
        self.sums = [0]
        for n in nums:
        	s += n
        	self.sums.append(s)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
#Range Sum Query - Immutable
#https://leetcode.com/problems/range-sum-query-immutable/description/