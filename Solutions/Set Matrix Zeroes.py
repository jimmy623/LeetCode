class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        mark = " "
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for t in range(m):
                        if matrix[t][j] != 0:
                            matrix[t][j] = mark
                    for t in range(n):
                        if matrix[i][t] != 0:
                            matrix[i][t] = mark
                            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == mark:
                    matrix[i][j] = 0
#Set Matrix Zeroes
#https://oj.leetcode.com/problems/set-matrix-zeroes/