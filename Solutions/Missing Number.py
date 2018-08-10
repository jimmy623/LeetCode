class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = 0
        supposedSum = 0
        for i in range(n):
        	sum1 += nums[i]
        	supposedSum += i
        return supposedSum + n - sum1

        #supposedSum + n - missing =  sum1

#Missing Number
#https://leetcode.com/problems/missing-number/description/