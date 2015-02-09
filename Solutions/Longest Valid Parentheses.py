class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        max = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    continue
                else:
                    v = stack.pop()
                    if v == "(":
                        if len(stack):
                            if stack[-1] == "(":
                                stack.append(2)
                                if max < 2:
                                    max = 2
                            else:
                                stack[-1] = stack[-1] + 2
                                if max < stack[-1]:
                                    max = stack[-1]
                        else:
                            stack.append(2)    
                            if max < 2:
                                max = 2
                    else:      
                        if len(stack) > 1:
                            stack[-1] = v+2
                            if stack[-2] != "(":
                                v = stack.pop()
                                stack[-1] = stack[-1] + v
                            if stack[-1] > max:
                                max = stack[-1]
                                
                        elif len(stack) == 1:
                            stack[-1] = v+2
                            if stack[-1] > max:
                                max = stack[-1]
        return max
                        
            
                
                
s = Solution()



p = "(()"
p = ")()())"

p = "()(()"
p = ")()())"
p = "(()(((()"
p = "()(())"
print s.longestValidParentheses(p)
#Longest Valid Parentheses
#https://oj.leetcode.com/problems/longest-valid-parentheses/