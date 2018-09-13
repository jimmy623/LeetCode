class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in xrange(m):
        	number = matrix[i][0]
        	d = 1
        	while i + d < m and d < n:
        		if matrix[i+d][d] != number:
        			return False
        		d+=1

        for i in xrange(1,n):
        	number = matrix[0][i]
        	d = 1
        	while d < m and i + d < n:
        		if matrix[d][i+d] != number:
        			return False
        		d+=1
        return True
#Toeplitz Matrix
#https://leetcode.com/problems/toeplitz-matrix/description/