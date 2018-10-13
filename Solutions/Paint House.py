class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
        	return 0
        dp = [[0,0,0] for _ in xrange(len(costs))]

        dp[0] = costs[0]
        for i in xrange(1,len(costs)):
        	dp[i][0] = costs[i][0] + min(dp[i-1][1],dp[i-1][2])
        	dp[i][1] = costs[i][1] + min(dp[i-1][2],dp[i-1][0])
        	dp[i][2] = costs[i][2] + min(dp[i-1][1],dp[i-1][0])
        return min(dp[-1])
#Paint House
#https://leetcode.com/problems/paint-house/description/