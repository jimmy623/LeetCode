class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            #print c,stack
            if c in "+-*/":
                v2 = stack.pop()
                v1 = stack.pop()
                
                if c == "+":
                    r = v1 + v2
                elif c == "-":
                    r = v1 - v2
                elif c == "*":
                    r = v1 * v2
                else:
                    if v1 * v2 >= 0:
                        flag = 1
                    else:
                        flag = -1
                    r = abs(v1) / abs(v2) * flag
                    
                stack.append(r)
            else:
                stack.append(int(c))
        return stack[0]
        
s = Solution()
A = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(A)
#Evaluate Reverse Polish Notation
#https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/