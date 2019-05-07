class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        result = None
        N = len(A)
        f = 0
        sumation = sum(A)
        for i,n in enumerate(A):
            f += i*n
        result = f
        for i in xrange(1,N):
            f = f + N * A[i-1] - sumation
            result = max(result,f)
        return result



#Rotate Function
#https://leetcode.com/problems/rotate-function/
