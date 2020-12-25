class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        current = 0
        for i in range(len(nums)):
        	if nums[i] == 1:
        		current +=1
        		result = max(result, current)
        	else:
        		current = 0

        return result
#Max Consecutive Ones
#https://leetcode.com/problems/max-consecutive-ones/