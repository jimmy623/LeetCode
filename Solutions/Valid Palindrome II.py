class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        changeUsed = False
        valid = True
        while start < end:
        	if s[start] == s[end]:
        		start += 1
        		end -= 1
        	else:
        		nstart = start + 1
        		nend = end
        		while nstart < nend:
        			if s[nstart] == s[nend]:
        				nstart += 1
        				nend -= 1
        			else:
        				valid = False
        				break
        		if valid:
        			return True
        		valid = True
        		nstart = start
        		nend = end -1
        		while nstart < nend:
        			if s[nstart] == s[nend]:
        				nstart += 1
        				nend -= 1
        			else:
        				valid = False
        				break
        		if valid:
        			return True
        		else:
        			return False
        return True
#Valid Palindrome II
#https://leetcode.com/problems/valid-palindrome-ii/description/