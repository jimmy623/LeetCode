class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    left = 99999
                else:
                    left = grid[i][j-1]
                
                if i == 0:
                    up = 99999
                else:
                    up = grid[i-1][j]
                
                grid[i][j] += min(left,up)
        return grid[m-1][n-1]
                  
#Minimum Path Sum
#https://oj.leetcode.com/problems/minimum-path-sum/