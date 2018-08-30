class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		if grid[i][j]:
        			#up
        			if i == 0:
        				count +=1
        			else:
        				if grid[i-1][j] == 0:
        					count += 1
        			#down
        			if i == len(grid) -1:
        				count += 1
        			else:
        				if grid[i+1][j] == 0:
        					count += 1
        			#left
        			if j == 0:
        				count += 1
        			else:
        				if grid[i][j-1] == 0:
        					count += 1
        			#right
        			if j == len(grid[0])-1:
        				count += 1
        			else:
        				if grid[i][j+1] == 0:
        					count += 1
        return count

#Island Perimeter
#https://leetcode.com/problems/island-perimeter/description/