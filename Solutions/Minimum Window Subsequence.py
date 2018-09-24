import bisect
from collections import defaultdict
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = defaultdict(list)
        for i,c in enumerate(S):
        	d[c].append(i)
        if len(T) == 1:
        	if T in d:
        		return T
        	else:
        		return ""

        result = []
        first = T[0]
        possible = True
        for i in d[first]:
        	p = i+1
        	for j in xrange(1,len(T)):
        		c = T[j]
        		candidate = bisect.bisect_left(d[c],p)
        		if candidate == len(d[c]):
        			possible = False
        			break
        		p = d[c][candidate]+1
        	if not possible:
        		break
        	length = p-i
        	if not result or length < result[1]-result[0]+1:
        		result = [i,p-1]

        if not result:
        	return ""
        else:
        	return S[result[0]:result[1]+1]
s = Solution()
print s.minWindow("abcdebdde","bde")
print s.minWindow("cnhczmccqouqadqtmjjzl","mm")

#Minimum Window Subsequence
#https://leetcode.com/problems/minimum-window-subsequence/description/