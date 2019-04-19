class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        i = 2
        length = 2
        while i < len(A):
        	if A[i-1] - A[i-2] == A[i] - A[i-1]:
        		length+=1
        		result += length - 3 + 1
        	else:
        		length = 2
        	i+=1

        return result




#Arithmetic Slices
#https://leetcode.com/problems/arithmetic-slices/