class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        n = len(s1)
        if n <= 1:
            return s1 == s2
        flag = False
        for m in range(1,n):
            p1 = s1[0:m]
            p2 = s1[m:n]
            sp1 = sorted(p1)
            sp2 = sorted(p2)        
            if sorted(s2[0:m]) == sp1 and sorted(s2[m:n]) == sp2:
                if self.isScramble(s2[0:m],p1) and self.isScramble(s2[m:n],p2):
                    return True
            elif sorted(s2[0:n-m]) == sp2 and sorted(s2[n-m:n]) == sp1:
                if self.isScramble(s2[0:n-m],p2) and self.isScramble(s2[n-m:n],p1):
                    return True
            
        return False
        
        
s = Solution()
s1 = "great"
s2 = "rgtae"
s1 = "abb"
s2 = "bab"
print s.isScramble(s1,s2)      
#Scramble String
#https://oj.leetcode.com/problems/scramble-string/