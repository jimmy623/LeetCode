class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end and nums[start] <= nums[start+1]:
            start += 1
        if start >= end:
            return 0
        while nums[end] >= nums[end-1]:
            end-=1
            
        minimum = min(nums[start:end+1])
        maximum = max(nums[start:end+1])
        
        while start >= 0 and nums[start] > minimum:
        	start -= 1
        while end < len(nums) and nums[end] < maximum:
        	end += 1
            
        return end- start -1


#Shortest Unsorted Continuous Subarray
#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/