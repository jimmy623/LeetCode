class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(s):
        	count = 0
        	for i,c in enumerate(s):
        		if c == "(":
        			count += 1
        		elif c == ")":
        			if count > 0:
        				count -= 1
        			else:
        				return False
        	return count == 0
        bfs = {s}
        result = set()
        while bfs:
        	next = set()
        	for left in bfs:
        		if valid(left):
        			result.add(left)
        		else:
        			for i in xrange(len(left)):
        				next.add(left[:i]+left[i+1:])
        	if result:
        		return list(result)
        	else:
        		bfs = next


        

s = Solution()
# print s.removeInvalidParentheses(")((((((((")
# print s.removeInvalidParentheses("()())()")
print s.removeInvalidParentheses("((s(())()(()))((((((")


#Remove Invalid Parentheses
#https://leetcode.com/problems/remove-invalid-parentheses/description/