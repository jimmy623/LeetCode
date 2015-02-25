class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            if s == "0":
                return 0
            else:
                return 1
        dp = [1 for i in (range(len(s)+1))]
        
        if s[-1] == "0":
            dp[n-1] = 0
            
        for i in range(n-2,-1,-1):
            c = s[i]
            cn = s[i+1]
            if c == "0":
                if i == 0:
                    return 0
                if cn == "0":
                    return 0
                dp[i] = 0
            elif c == "1":
                if cn == "0":
                    dp[i] = dp[i+2]
                else:
                    dp[i] = dp[i+1] + dp[i+2]
            elif c == "2":
                if cn in "123456":
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+2]
            else:
                dp[i] = dp[i+1]
            
         
        return dp[0]

s = Solution()
print s.numDecodings("110")
                    
#Decode Ways
#https://oj.leetcode.com/problems/decode-ways/