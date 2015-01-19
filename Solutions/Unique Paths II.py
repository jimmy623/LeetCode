class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = {}
        return self.route(obstacleGrid,0,0,m,n,result)
        
    def route(self,g,x,y,m,n,result):
        if (x,y) in result:
            return result[(x,y)]
        
        if x == m -1 and y == n - 1:
            if g[x][y] == 1:
                return 0
            return 1
            
        if x == m or y == n:
            return 0
        
        if g[x][y] == 1:
            result[(x,y)] = 0
            return 0
        
        right = self.route(g,x+1,y,m,n,result)
        down = self.route(g,x,y+1,m,n,result)
        result[(x,y)] = right + down
        print right,down
        return right + down
        
        
g = [[1],[0]]
s = Solution()
print s.uniquePathsWithObstacles(g)


#Unique Paths II 
#https://oj.leetcode.com/problems/unique-paths-ii/