class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if not len(code) or code[0] != "<":
        	return False
        
        inCDATA = False
        stack = []
        inOpenTag = False
        inCloseTag = False
        def isCdataStart(index):
        	if index >= 8:
        		if code[index-8:index+1] == "<![CDATA[":
        			return True
        	return False

        def isCdataEnd(index):
        	if inCDATA and index >= 2:
        		if code[index-2:index+1] == "]]>":
        			return True
        	return False

        def isTagStart(index):
        	if inCDATA or inOpenTag or inCloseTag:
        		return False
        	return True

        def isCloseTagStart(index):
        	if inCDATA:
        		return False
        	if index >= 1:
        		if code[index-1:index+1] == "</":
        			return True
        	return False

        def isTagEnd(index):
        	if inCDATA:
        		return False
        	if inOpenTag or inCloseTag :
        		return True
        	return False

        def validTagName(tag):
        	if len(tag) == 0 or len(tag) > 9:
        		return False
        	for c in tag:
        		if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        			return False
        	return True

        tsi = 0

        for i,c in enumerate(code):
        	if c == "<":
        		if isTagStart(i):
        			tsi = i
        			inOpenTag = True
        		elif inCDATA:
        			continue
        		else:
        			return False

        	elif c == "/":
        		if isCloseTagStart(i):
        			tsi = i
        			inOpenTag = False
        			inCloseTag = True

        	elif c == ">":
        		if isCdataEnd(i):
        			inCDATA = False
        			if not len(stack):
        				return False
        		elif isTagEnd(i):
        			tag = code[tsi+1:i]
        			if not validTagName(tag):
        				return False
        			if inOpenTag:
        				stack.append((tag,i))
        				inOpenTag = False
        				continue
        			if inCloseTag:
        				if len(stack) and stack[-1][0] == tag:
							stack.pop()
                            inCloseTag = False
        					if len(stack) == 0 and i != len(code)-1:
        						return False
        				else:
        					return False
        				
        	elif c == "[":
        		if isCdataStart(i):
        			inCDATA = True
        			inOpenTag = False
        			inCloseTag = False
        			CDATA_start = i+1

        if inCDATA or inOpenTag or inCloseTag or len(stack):
        	return False
        return True


s = Solution()
data = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
data = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"
data = "<A></A><B></B>"
# data = "<A><A></A></A>"
print s.isValid(data)


#Tag Validator
#https://leetcode.com/problems/tag-validator/description/