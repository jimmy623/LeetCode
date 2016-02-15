class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        if len(nums) == 0:
            return 0
        
        sum = 0
        result = 0
        while end < len(nums):
            sum += nums[end]
            end += 1
            while sum < s and end < len(nums):
                    sum += nums[end]
                    end+=1

            while sum - nums[start] >= s:
                sum -= nums[start]
                start += 1
            
            if sum >= s:
                if result == 0:
                    result = end - start
                else:
                    if result > (end-start):
                        result = end - start             
        return result
                 
            
        
s = Solution()
data = [1,4,4]
n = 4
print s.minSubArrayLen(n,data)
#Minimum Size Subarray Sum
#https://leetcode.com/problems/minimum-size-subarray-sum/#