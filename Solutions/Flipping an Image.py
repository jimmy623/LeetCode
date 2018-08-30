class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in A:
        	r.reverse()
        for r in A:
        	for i in xrange(len(r)):
        		r[i] = 1 - r[i]
        return A

#https://leetcode.com/problems/flipping-an-image/description/
#Flipping an Image