class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        M = (N << 1) - 1;
        dp = [[0 for _ in xrange(N)] for _ in xrange(N)];
        dp[0][0] = grid[0][0];
      
        for n in xrange(1,M):
            for i in xrange(N-1,-1,-1):
                for p in xrange(N-1,-1,-1):
                    j = n - i
                    q = n - p
                
                    if j < 0 or j >= N or q < 0 or q >= N or grid[i][j] < 0 or grid[p][q] < 0:
                        dp[i][p] = -1
                        continue
     
                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p - 1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
     
                    if dp[i][p] >= 0:
                        if i != p:
                            t = grid[p][q]
                        else:
                            t = 0
                        dp[i][p] += grid[i][j] + t
             
    
        return max(dp[N - 1][N - 1], 0)
s = Solution()    
data = [[0,1,-1],[1,0,-1],[1,1,1]]
data = [[1,1,1,1,-1,-1,-1,1,0,0],[1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,1,1,1,0,-1,1,1],[0,0,0,0,1,-1,0,0,1,-1],[1,0,1,1,1,0,0,-1,1,0],[1,1,0,1,0,0,1,0,1,-1],[1,-1,0,1,0,0,0,1,-1,1],[1,0,-1,0,-1,0,0,1,0,0],[0,0,-1,0,1,0,1,0,0,1]]
print s.cherryPickup(data)
#Cherry Pickup
#https://leetcode.com/problems/cherry-pickup/