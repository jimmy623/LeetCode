from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct = Counter(s)
        for i in xrange(len(s)):
        	if ct[s[i]] == 1:
        		return i
        return -1
#First Unique Character in a String
#https://leetcode.com/problems/first-unique-character-in-a-string/description/