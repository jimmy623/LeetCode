class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inblock = False
        result = []

        remain = []        	
        for line in source:
        	blockStart = -2
        	blockEnd = -2
        	for i,c in enumerate(line):
        		if not inblock:
        			remain.append(c)
        			if i > 0 and i-2 != blockEnd and line[i-1] == "/" and c == "/":  # //
        				remain.pop()
        				remain.pop()
        				break

        			if i > 0 and i-2 != blockEnd and line[i-1] == "/" and c == "*":   # /*
        				inblock = True
        				remain.pop()
        				remain.pop()
        				blockStart = i-1

        		elif i > 0 and i-2 != blockStart and line[i-1] == "*" and c == "/":  # */
        			inblock = False
        			blockEnd = i -1

        	if not inblock:
        		if len(remain):
        			result.append("".join(remain))
        			remain = []
        return result




#Remove Comments
#https://leetcode.com/problems/remove-comments/description/