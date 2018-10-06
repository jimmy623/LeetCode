from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        # dp = [1 for _ in xrange(len(nums))]
        # for i,n in enumerate(nums):
        # 	for j in xrange(i):
        # 		if nums[j] < n:
        # 			dp[i] = max(dp[i],1+dp[j])
        # return max(dp)
        
        r = [nums[0]]
        for i in xrange(1,len(nums)):
        	n = nums[i]
        	index = bisect_left(r,n)
        	if index == len(r):
        		r.append(n)
        		continue
        	if r[index] != n:
        		r[index] = n
        
        return len(r)

        #https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

s = Solution()
print s.lengthOfLIS([4,10,4,3,8,9])
#Longest Increasing Subsequence
#https://leetcode.com/problems/longest-increasing-subsequence/description/