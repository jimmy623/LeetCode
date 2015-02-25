class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        n = len(s)
        if n == 0:
            return False
            
        if s[0] == "+" or s[0] == "-":
            s = s[1:]

        n = len(s)
        if n == 0:
            return False
        
        if n > 1:
            if s[0] == 0 and s[1] != ".":
                return False
        
        
        numercis = "0123456789"
        dot = False
        e = False
        
        for i in range(n):
            c = s[i]
            if c in numercis:
                continue
            elif c == ".":
                if dot:
                    return False
                else:
                    if n == 1:
                        return False
                    if e:
                        return False
                    dot = True
            elif c == "e":
                if e:
                    return False
                else:
                    if i == 0 or i == n-1:
                        return False
                    if dot:
                        if i == 1:
                            return False
                    e = True
            elif c == "+" or c == "-":
                if s[i-1] == "e" and i != n-1:
                    continue
                else:
                    return False
            else:
                return False
        
        
        return True

s = Solution()
print s.isNumber("-1.")
#Valid Number
#https://oj.leetcode.com/problems/valid-number/