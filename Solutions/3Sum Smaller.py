class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        l = len(nums)
        for i in xrange(l-2):
        	start,end = i+1,l-1
        	v = nums[i]
        	while start < end:
        		if v + nums[start] + nums[end] < target:
        			count += end-start
        			start += 1
        		else:
        			end -= 1
        return count
s = Solution()
print s.threeSumSmaller([1,1,-2],1)
#3Sum Smaller
#https://leetcode.com/problems/3sum-smaller/description/