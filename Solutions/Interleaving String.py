class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m+n != l:
            return False
            
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(n+1):        
                if i > 0:
                    if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                        dp[i][j] = True
                        continue
                if j > 0:
                    if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                        dp[i][j] = True
        return dp[m][n]
                        
                
        
        
        
        
        
        
s = Solution()

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#s3 = "aadbbbaccc"


s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
print s.isInterleave(s1,s2,s3)
#Interleaving String
#https://oj.leetcode.com/problems/interleaving-string/