class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.float(grid,i,j,m,n)
                    count += 1
        return count
    
    def float(self,grid,i,j,m,n):
        if i < 0 or i == m:
            return
        if j < 0 or j == n:
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.float(grid,i-1,j,m,n)
        self.float(grid,i+1,j,m,n)
        self.float(grid,i,j-1,m,n)
        self.float(grid,i,j+1,m,n)
        
        
s = Solution()
g = [["1","1"]]
print s.numIslands(g)
#Number of Islands
#https://leetcode.com/problems/number-of-islands/
