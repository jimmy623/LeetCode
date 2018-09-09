class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m = len(self.matrix)
        if self.m == 0:
            return

        self.n = len(self.matrix[0])
        self.sums = [[0 for _ in xrange(self.n+1)] for _ in xrange(self.m+1)]
        for i in xrange(self.m):
            s = 0
            for j in xrange(self.n):
                self.sums[i+1][j+1] = self.sums[i][j+1] + self.matrix[i][j] + s
                s += self.matrix[i][j]
        #print self.sums

    # def cornerSum:(self,row,col):
    #   if row == 0 or col == 0:
    #       return 0


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        oldVal = self.matrix[row][col]
        diff = val - oldVal
        self.matrix[row][col] = val
        for i in xrange(row,self.m):
            for j in xrange(col,self.n):
                self.sums[i+1][j+1] += diff


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1] + self.sums[row1][col1] - self.sums[row1][col2+1] - self.sums[row2+1][col1]


# class NumMatrix(object):

#     def __init__(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         """
#         self.matrix = matrix
#         self.result = {}

#     def update(self, row, col, val):
#         """
#         :type row: int
#         :type col: int
#         :type val: int
#         :rtype: void
#         """
#         oldVal = self.matrix[row][col]
#         diff = val -oldVal
#         self.matrix[row][col] = val
#         for key in self.result:
#           if key[0] <= row <= key[2] and key[1] <= col <= key[3]:
#               self.result[key] += diff

#     def sumRegion(self, row1, col1, row2, col2):
#         """
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
#         if (row1,col1,row2,col2) in self.result:
#           return self.result[(row1,col1,row2,col2)]

#         count = 0
#         for i in xrange(row1,row2+1):
#           for j in xrange(col1,col2+1):
#               count += self.matrix[i][j]
#         self.result[(row1,col1,row2,col2)] = count
#         return count


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
#Range Sum Query 2D - Mutable
#https://leetcode.com/problems/range-sum-query-2d-mutable/description/