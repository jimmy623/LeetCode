class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #self.count = 0;
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        return self.dfs(matrix,target,0,0)
        
    def dfs(self,matrix,target,i,j):
    	if matrix[i][j] == None:
    		return False
    	#self.count += 1;
    	#print i,j,self.count
    	if matrix[i][j] == target:
    		return True
    	if matrix[i][j] > target:
    		return False
    	if i+1 < len(matrix):
    		if self.dfs(matrix,target,i+1,j):
    			return True
    	if j+1 < len(matrix[0]):
    		if self.dfs(matrix,target,i,j+1):
    			return True
    	matrix[i][j] = None
    	return False


#Search a 2D Matrix II
#https://leetcode.com/problems/search-a-2d-matrix-ii/description/