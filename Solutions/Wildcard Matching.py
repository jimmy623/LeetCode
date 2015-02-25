class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    
    def isMatch(self, s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True]  + [False] * l
        for letter in p:
            print dp,letter
            new_dp = [dp[0] and letter == '*']
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        print dp
        return dp[-1]
            
sol = Solution()
s = "aa"
p = "a*"

s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"



s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p = "a*******b"

s = "aa"
p = "*"

s = "bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa"
p = "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****"

s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

s = "ababab"
p = "ab*b"
print sol.isMatch(s,p)
#Wildcard Matching
#https://oj.leetcode.com/problems/wildcard-matching/