class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
        	return
        n = len(matrix[0])
        if n == 0:
        	return
        self.sums = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        for i in xrange(m):
        	s = 0
        	for j in xrange(n):
        		s += matrix[i][j]
        		self.sums[i+1][j+1] = self.sums[i][j+1] + s

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1] + self.sums[row1][col1] - self.sums[row1][col2+1] - self.sums[row2+1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
#Range Sum Query 2D - Immutable
#https://leetcode.com/problems/range-sum-query-2d-immutable/description/