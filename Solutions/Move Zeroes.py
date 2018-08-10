class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        i = 0
        n = len(nums)
        while i < n:
        	if nums[i] != 0:
        		nums[p] = nums[i]
        		p += 1
        	i += 1
        while p < n:
        	nums[p] = 0
        	p += 1

#Move Zeroes
#https://leetcode.com/problems/move-zeroes/description/