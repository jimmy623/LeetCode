class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        for i in xrange(2,length):
        	if A[i] == A[i-1] or A[i] == A[i-2]:
        		return A[i]
        return A[0]

#N-Repeated Element in Size 2N Array
#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/