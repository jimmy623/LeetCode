from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        a = defaultdict(int);
        b = defaultdict(int);
        for k in s:
        	a[k] += 1;
        for k in t:
        	b[k] += 1;
        return a == b;
        
#Valid Anagram
#https://leetcode.com/problems/valid-anagram/description/