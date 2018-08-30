class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        indexes = []
        vowels = []
        for i in xrange(len(s)):
        	if s[i] in "aeiouAEIOU":
        		indexes.append(i)
        		vowels.append(s[i])
        l = [c for c in s]

        vowels.reverse()
        for p in xrange(len(indexes)):
        	i = indexes[p]
        	c = vowels[p]
        	l[i] = c
        return "".join(l)
	        	

#Reverse Vowels of a String
#https://leetcode.com/problems/reverse-vowels-of-a-string/description/