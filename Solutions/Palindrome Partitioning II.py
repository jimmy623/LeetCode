class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        matrix = [[False for x in range(n)] for j in range(n)]

        cuts = []
        for i in range(n+1):
            cuts.append(n-i)
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if (s[i] == s[j] and j-i<2) or (s[i] == s[j] and matrix[i+1][j-1]):
                    matrix[i][j] = True
                    cuts[i] = min(cuts[i],cuts[j+1]+1)
        result = cuts[0]
        return result -1
        


s = Solution()
#print s.minCut("aabbccddeeffgghhiijjkk")
print s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")
#print s.minCut("aab")
    
#Palindrome Partitioning II
#https://oj.leetcode.com/problems/palindrome-partitioning-ii/