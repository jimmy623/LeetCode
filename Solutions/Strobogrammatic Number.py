class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        chars = "01689"
        buf = []
        def replace(c):
        	if c == "0":
        		return c
        	if c == "1":
        		return c
        	if c == "8":
        		return c
        	if c == "6":
        		return "9"
        	if c == "9":
        		return "6"

        for c in num:
        	buf.append(replace(c))
        	if c not in chars:
        		return False
        return num == "".join(buf[::-1])


#Strobogrammatic Number
#https://leetcode.com/problems/strobogrammatic-number/description/