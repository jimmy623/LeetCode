class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        if not grid:
            return []

        m = len(grid)
        n = len(grid[0])

        for i,j in hits:
            if grid[i][j] == 0:
                grid[i][j] = -1
            else:
                grid[i][j] = 0

        for p in xrange(n):
            if grid[0][p] != 1:
                continue
            bfs = [[0,p]]
            while bfs:
                next = []
                for i,j in bfs:
                    grid[i][j] = 2
                    for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            next.append([x,y])
                bfs = next
        result = []
        for p in xrange(len(hits)-1,-1,-1):
            x,y = hits[p]
            if grid[x][y] == -1:
                result.append(0)
                continue

            grid[x][y] = 1
            connected = False
            for x1,y1 in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 2:
                    connected = True
                    break
            if x == 0:
                connected = True
            if not connected:
                result.append(0)
                continue

            visited = set()
            connected = False
            

            bfs = [[x,y]]
            while bfs:
                next = []
                for i,j in bfs:
                    if (i,j) in visited:
                        continue
                    visited.add((i,j))
                    for x1,y1 in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                        if 0 <= x1 < m and 0 <= y1 < n:
                            if grid[x1][y1] == 1:
                                next.append([x1,y1])
                bfs = next
            
            result.append(len(visited)-1)
            for i,j in visited:
                grid[i][j] = 2
            

        result.reverse()
        return result

s = Solution()
print s.hitBricks([[1,0,0,0],[1,1,1,0]],[[1,0]])
print s.hitBricks([[1],[1],[1],[1],[1]],[[3,0],[4,0],[1,0],[2,0],[0,0]])       
print s.hitBricks([[1,0,1],[0,0,1]],[[1,0],[0,0]])                 


#Bricks Falling When Hit
#https://leetcode.com/problems/bricks-falling-when-hit/description/