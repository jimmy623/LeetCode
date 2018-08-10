class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        result = []
        for n in nums:
        	result.append(p)
        	p = p*n
        p = 1
        for i in range(len(nums)-1,-1,-1):
        	result[i] = result[i] * p
        	p = p* nums[i]
        return result

#Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/description/