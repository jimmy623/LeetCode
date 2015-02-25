class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = len(T)
        n = len(S)
        if m > n:
            return 0
        result = [0 for i in range(m+1)]
        result[0] = 1
        for j in range(1,n+1):
            for i in range(m,0,-1):
                result[i] += (T[i-1] == S[j-1])*result[i-1]
        return result[m]
        
s = Solution()
print s.numDistinct("rabbbit","rabbit")
print s.numDistinct("","a")
                
                
        
#Distinct Subsequences
#https://oj.leetcode.com/problems/distinct-subsequences/