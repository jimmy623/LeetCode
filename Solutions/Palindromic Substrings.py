class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0;
        length = len(s)
        for i in range(length):
        	result += 1
        	#center
        	maxExpand = min(i,length-i-1)
        	width = 1
        	while width <= maxExpand:
        		#print "single" + str(i) + " "+ str(width);
        		if s[i-width] == s[i+width]:
        			result += 1
        			width += 1
        		else:
        			break
        	#+1 center
        	maxExpand = min(i,length-i-2)
        	width = 1
        	if i < length - 1 and s[i] == s[i+1]:
        		result += 1
        		#print "double" + str(i) + " "+ str(width);
        		while width <= maxExpand:
        			if s[i-width] == s[i+width+1]:
        				result += 1
        				width += 1
        			else:
        				break

        return result
s = Solution()
print s.countSubstrings("aaa")   
#Palindromic Substrings
#https://leetcode.com/problems/palindromic-substrings/description/