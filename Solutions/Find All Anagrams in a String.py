class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s) or len(s) == 0:
        	return []

        cp = [0 for i in xrange(26)]
        aoffset = ord("a")
        for c in p:
        	cp[ord(c)-aoffset] += 1
        print cp
        sp = [0 for i in xrange(26)]
        for i in xrange(len(p)):
        	sp[ord(s[i])-aoffset] += 1
        result = []
        if sp == cp:
        	result.append(0)
        lenp = len(p)
        for i in xrange(1,len(s)-lenp+1):
        	sp[ord(s[i+lenp-1])-aoffset] += 1
        	sp[ord(s[i-1]) - aoffset] -= 1
        	if sp == cp:
        		result.append(i)
       	return result
        	

#s = 123456.  6
#p = 123 3


s = Solution()
print s.findAnagrams("cbaebabacd","abc")
#Find All Anagrams in a String
#https://leetcode.com/problems/find-all-anagrams-in-a-string/description/