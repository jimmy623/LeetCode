class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        maxArea = 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j],cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            
            for j in range(n-1,-1,-1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            print left
            print right
            print height
            for j in range(n):
                maxArea = max(maxArea,(right[j]-left[j])*height[j])
        return maxArea     
        
s = Solution()
matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
matrix = [["0","0","0"],["0","0","0"],["1","1","1"]]
print s.maximalRectangle(matrix)
                
#Maximal Rectangle
#https://oj.leetcode.com/problems/maximal-rectangle/