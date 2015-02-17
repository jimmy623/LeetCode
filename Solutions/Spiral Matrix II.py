class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        self.n = n
        if self.n == 0:
            return []
            
        self.grid = []
        for i in range(n):
            self.grid.append([None for x in range(n)])
        
        print self.grid
            
        
        self.grid[0][0] = 1
        value = 1
        
        point = (0,0)
        direction = (1,0)

        flag = 4
        
        while flag > 0:
            flag -= 1
            
            read = False
            while self.valid((point[0]+direction[0],point[1]+direction[1])):
                read = True
                point = (point[0]+direction[0],point[1]+direction[1])
                value += 1
                self.setPoint(point,value)
                
            if read:
                flag += 1
             
            if direction == (1,0):
                direction = (0,1)
            elif direction == (0,1):
                direction = (-1,0)
            elif direction == (-1,0):
                direction = (0,-1)
            elif direction == (0,-1):
                direction = (1,0)

                
        
        return self.grid
        
    def point(self,(x,y)):
        return self.grid[y][x]
        
    def setPoint(self,(x,y),value):
        self.grid[y][x] = value
        
    def valid(self,(x,y)):
        if x < 0 or x >= self.n:
            return False
        if y < 0 or y>= self.n:
            return False
        if self.point((x,y)) != None:
            return False
        return True

s = Solution()
print s.generateMatrix(3)     
    
#Spiral Matrix II
#https://oj.leetcode.com/problems/spiral-matrix-ii/