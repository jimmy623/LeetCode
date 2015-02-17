class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
            
        previous = [1]
        i = 1
        while True:
            level = []
            for j in range(i+1):
                if j == i or j == 0:
                    level.append(1)
                else:
                    level.append(previous[j-1]+previous[j])
            if i == rowIndex:
                return level
            previous = level
            i+=1
#Pascal's Triangle II
#https://oj.leetcode.com/problems/pascals-triangle-ii/