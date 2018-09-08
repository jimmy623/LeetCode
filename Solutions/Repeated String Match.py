import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lA = len(A)
        lB = len(B)
        tMin = int(math.ceil(float(lB)/lA))
        string = A * tMin
        if string.find(B) >= 0:
        	return tMin
        string += A
        if string.find(B) >= 0:
        	return tMin+1
        return -1

#Repeated String Match
#https://leetcode.com/problems/repeated-string-match/description/