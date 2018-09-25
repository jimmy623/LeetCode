from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        start = 0
        end = 0
        result = 0
        while end < len(s):
        	d[s[end]] += 1
        	while len(d) > k:
        		c = s[start]
        		if d[c] == 1:
        			del d[c]
        		else:
        			d[c] -= 1
        		start += 1
        	result = max(result,end-start+1)
        	end += 1
        return result

#Longest Substring with At Most K Distinct Characters
#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/