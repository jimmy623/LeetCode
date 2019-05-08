class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.counter = 0
        result = 0
        def dfs(x,y):
        	if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
        		return
        	self.counter += 1
        	grid[x][y] = 0
        	dfs(x-1,y)
        	dfs(x+1,y)
        	dfs(x,y-1)
        	dfs(x,y+1)

        for i in xrange(m):
        	for j in xrange(n):
        		if grid[i][j] == 1:
        			self.counter = 0
        			dfs(i,j)
        			result = max(result,self.counter)
        return result


        
#Max Area of Island
#https://leetcode.com/problems/max-area-of-island/