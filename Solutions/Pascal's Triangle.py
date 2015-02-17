class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
            
        result = [[1]]
        for i in range(1,numRows):
            level = []
            for j in range(i+1):
                if j == i or j == 0:
                    level.append(1)
                else:
                    level.append(result[-1][j-1]+result[-1][j])
            result.append(level)
        return result
            
#Pascal's Triangle
#https://oj.leetcode.com/problems/pascals-triangle/