class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        # for s in xrange(n-1,-1,-1):
        #     dp[s][s] = nums[s]
        #     for e in xrange(s+1,n):
        #         a = nums[s] - dp[s+1][e]
        #         b = nums[e] - dp[s][e-1]
        #         dp[s][e] = max(a,b)

        # for row in dp:
        #     print row

        # return dp[0][n-1] >= 0

        
        n = len(nums)
        dp = [0 for _ in xrange(n)]
        for s in xrange(n-1,-1,-1):
            dp[s] = nums[s]
            for e in xrange(s+1,n):
                a = nums[s] - dp[e]
                b = nums[e] - dp[e-1]
                dp[e] = max(a,b)
        return dp[n-1] >= 0


    #     n = len(nums)
    #     memo = [[None for _ in xrange(n)] for _ in xrange(n)]
    #     return self.winner(nums,0,n-1,memo) >= 0

    # def winner(self,nums,s,e,memo):
    #     if s == e:
    #       return nums[s]
    #     if memo[s][e]:
    #       return memo[s][e] 
    #     a = nums[s] - self.winner(nums,s+1,e,memo)
    #     b = nums[e] - self.winner(nums,s,e-1,memo)
    #     r = max(a,b)
    #     memo[s][e] = r
    #     return r

s = Solution()
print s.PredictTheWinner([1, 5, 2])
#Predict the Winner
#https://leetcode.com/problems/predict-the-winner/description/