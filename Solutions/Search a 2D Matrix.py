class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        e = m-1
        while s <= e:
            middle = (s+e)/2
            v = matrix[middle][0]
            if v == target:
                return True
            if v > target:
                e = middle - 1
            else:
                s = middle + 1
        
        if target > matrix[e][n-1]:
            return False
        
        row = e
        s = 1
        e = n-1
        while s <= e:
            middle = (s+e)/2
            v = matrix[row][middle]
            if v == target:
                return True
            if v > target:
                e = middle - 1
            else:
                s = middle + 1
        return False
        
s = Solution()
m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
#m = [[1]]
m = [[1,3]]
print s.searchMatrix(m,3)
            
#Search a 2D Matrix
#https://oj.leetcode.com/problems/search-a-2d-matrix/