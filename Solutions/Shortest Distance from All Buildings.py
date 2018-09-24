class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = -1
        building = 0
        buildings = []
        for i in xrange(m):
        	for j in xrange(n):
        		if grid[i][j] == 1:
        			building += 1
        			buildings.append([i,j])
        def isValid(i,j):
        	if i < 0 or i >= m:
        		return False
        	if j < 0 or j >= n:
        		return False
        	if grid[i][j] == 0:
        		return True
        	return False

        def surrounding(i,j,visited):
        	result = []
        	for i1,j1 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        		if isValid(i1,j1) and (i1,j1) not in visited:
        			result.append((i1,j1))
        	return result

        board = [[[0,0] for _ in xrange(n)] for _ in xrange(m)]
        for k,[h,v] in enumerate(buildings):
        	visited = set([(h,v)])
        	pos = surrounding(h,v,visited)
        	dis = 1
        	while pos:
        		newPos = set()
        		for i,j in pos:
        			if (i,j) in visited:
        				continue
        			visited.add((i,j))
        			if board[i][j][0] == k:
        				board[i][j][0] += 1
        				board[i][j][1] += dis
        				newPos.update(surrounding(i,j,visited))
        		pos = newPos
        		dis += 1
        result = -1
        for i in xrange(m):
        	for j in xrange(n):
        		if board[i][j][0] == len(buildings):
        			if result < 0 or board[i][j][1] < result:
        				result = board[i][j][1]
        return result


s = Solution()
# print s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
print s.shortestDistance([[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]])

#Shortest Distance from All Buildings
#https://leetcode.com/problems/shortest-distance-from-all-buildings/description/