class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s = s.replace(" ","")
        i = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == "(":
                        add = stack[i+1:]
                        n = self.consume(add)

                        stack = stack[:i] + [n]
                        break

            elif c == "+":
                stack.append(c)
            elif c == "-":
                stack.append(c)
            else:
                number = 0
                if (len(stack)):
                    if type(stack[-1]) is int:
                        stack[-1] = int(str(stack[-1]) + c)
                    else:
                        stack.append(int(c))
                else:
                    stack.append(int(c))

        return self.consume(stack)

    def consume(self,add):
        number = add[0]
        for j in range(1,len(add)):
            if type(add[j]) is int:
                if add[j-1] == "+":
                    number += add[j]
                else:
                    number -= add[j]
        return number
        
s = Solution()
d = "1 + 1"
d = "(1+(4+5+2)-3)+(6+8)"
print s.calculate(d)



#Basic Calculator
#https://leetcode.com/problems/basic-calculator/
