class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        
        if len(p) > 2:
            news = p[0:2]
            for i in range(2,len(p)):
                v = p[i]
                news += v
                if v == "*":
                    if news[-1] == news[-3] and news[-2] == news[-4]:
                        news = news[0:len(news)-2]
            p = news       
                
        pi = 0
        si = 0
        while si <= len(s) and pi < len(p):
            c = p[pi]
            star = False
            if pi + 1 < len(p):
                if p[pi+1] == "*":
                    star = True
            
            if c == ".":
                if star:
                    pi += 2
                    flag = False
                    for i in range(si,len(s)+1):
                        result = self.isMatch(s[i:len(s)],p[pi:len(p)])
                        if result:
                            return True
                    if flag:
                        return True
                    else:
                        return False
                else:
                    pi += 1
                    si += 1
                continue
                
            if si < len(s):
                v = s[si]
            else:
                v = None
            if c == v:
                si += 1
                if star:
                    pi += 2
                    flag = False
                    k = si 
                    while k < len(s) and s[k] == c:
                        k += 1
                    for i in range(si-1,k+1):
                        if self.isMatch(s[i:len(s)],p[pi:len(p)]):
                            return True
                    
                    return False
                else:
                    pi += 1
            else:
                if star:
                    pi += 2
                    continue
                else:
                    return False
                
            
        if si == len(s) and pi == len(p):
            return True
        else:
            return False
                
s = Solution()

str = "aaa"
p = "a*a"

str = "aa"
p = "a*"

str = "aab"
p = "c*a*b"

str = "a"
p = "ab*"

str = "bbbba"
p = ".*a*a"

str = "a"
p = "a*a"

str = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"


print s.isMatch(str,p)
            
            
#Regular Expression Matching
#https://oj.leetcode.com/problems/regular-expression-matching/