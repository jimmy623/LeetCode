class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
        	return 0
        n = len(costs)
        m = len(costs[0])
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]

        dp[0] = costs[0]
        for i in xrange(1,n):
        	for j in xrange(m):
        		dp[i][j] = costs[i][j] + min(dp[i-1][:j]+dp[i-1][j+1])
        return min(dp[-1])
#Paint House II
#https://leetcode.com/problems/paint-house-ii/description/