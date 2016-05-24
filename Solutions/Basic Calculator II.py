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
            elif c == "*":
                stack.append(c)
            elif c == "/":
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
        b = list(add)
        i = 0
        while i < len(b):
            if b[i] == "*":
                b[i-1] = b[i-1] * b[i+1]
                b = b[:i] + b[i+2:]
            elif b[i] == "/":
                b[i-1] = b[i-1] / b[i+1]
                b = b[:i] + b[i+2:]
            else:
                i += 1
        number = b[0]
        for j in range(1,len(b)):
            if type(b[j]) is int:
                if b[j-1] == "+":
                    number += b[j]
                else:
                    number -= b[j]
        return number
s = Solution()
d = " 3+5 / 2 "
d = "3+2*2"
d = "2*3*4"
print s.calculate(d)
#Basic Calculator II
#https://leetcode.com/problems/basic-calculator-ii/
