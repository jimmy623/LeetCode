class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # Just return True, first player always wins
        # return True
        n = len(piles)
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
        for s in xrange(n,-1,-1):
            for e in xrange(s+1,n):
                a = piles[s] - dp[s+1][e]
                b = piles[e] - dp[s][e-1]
                dp[s][e] = max(a,b)
        return dp[0][n-1] >= 0
#Stone Game
#https://leetcode.com/problems/stone-game/description/