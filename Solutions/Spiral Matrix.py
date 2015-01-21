class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        self.grid = matrix
        self.m = len(matrix)
        if self.m == 0:
            return result
        self.n = len(matrix[0])
        result.append(matrix[0][0])
        matrix[0][0] = None
        
        point = (0,0)
        direction = (1,0)

        flag = 4
        
        while flag > 0:
            flag -= 1
            
            read = False
            while self.valid((point[0]+direction[0],point[1]+direction[1])):
                read = True
                point = (point[0]+direction[0],point[1]+direction[1])
                result.append(self.point(point))
                self.setPoint(point)
                
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

                
        
        return result
        
    def point(self,(x,y)):
        return self.grid[y][x]
        
    def setPoint(self,(x,y)):
        self.grid[y][x] = None
        
    def valid(self,(x,y)):
        if x < 0 or x>= self.n:
            return False
        if y < 0 or y>= self.m:
            return False
        if self.point((x,y)) == None:
            return False
        return True
            
       
       
       
        
        
# m = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]


# m = [
#         [2,5,8],
#         [4,0,-1]
#     ]

m = [
    [3],
    [2]
]

s = Solution()
r = s.spiralOrder(m)
print r

#Spiral Matrix
#https://oj.leetcode.com/problems/spiral-matrix/