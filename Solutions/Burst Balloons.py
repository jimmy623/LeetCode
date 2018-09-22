class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = [1] + [i for i in nums if i > 0] + [1]
    	n = len(self.nums)
    	self.dp = [[0]*n for _ in xrange(n)]

    	return self.burst(0,n-1)

    def burst(self,left,right):
    	if left+1 == right:
    		return 0
    	if self.dp[left][right] > 0:
    		return self.dp[left][right]
    	answer = 0
    	for i in xrange(left+1,right):
    		answer = max(answer,self.nums[i]*self.nums[left]*self.nums[right]+self.burst(left,i)+self.burst(i,right))
    	self.dp[left][right] = answer
    	return answer

#Burst Balloons
#https://leetcode.com/problems/burst-balloons/description/