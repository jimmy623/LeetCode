class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == "(" or c == "[" orc == "{":
                stack.append(c)
            elif c == ")":
                if len(stack) and stack[-1] == ")":
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if len(stack) and stack[-1] == ")":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if len(stack) and stack[-1] == ")":
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
#Valid Parentheses
#https://oj.leetcode.com/problems/valid-parentheses/