from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # d = collections.defaultdict(int)
        
        string = str(N)
        c = Counter(string)

        p = 1
        pstring = str(p)
        while len(pstring) <= len(string):
        	if len(pstring) == len(string):
        		if Counter(pstring) == c:
        			return True
        	p = p<< 1
        	pstring = str(p)
        return False


#Reordered Power of 2
#https://leetcode.com/problems/reordered-power-of-2/