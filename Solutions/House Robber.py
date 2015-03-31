class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        dp = [0 for i in range(len(num) + 2)]
        dp[-1] = 0
        dp[-2] = 0
        
        for i in range(len(num)-1,-1,-1):
            v = num[i]
            r = max(dp[i+1],dp[i+2]+v)
            dp[i] = r
        return dp[0]
                
#House Robber
#https://leetcode.com/problems/house-robber/