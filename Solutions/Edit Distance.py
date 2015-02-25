class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) > len(word2):
            return self.minDistance(word2,word1)
        if word1 == "":
            return len(word2)
        n1 = len(word1)
        n2 = len(word2)
        #only insert or replace
        #worst case : (n1) replace (n2-n1) insert
        #best  case : (n2-n1) insert
        
        dp = [i for i in range(n2+1)]
        for i in range(0,n1):
            newdp = [i+1] + [0 for t in range(n2)]
            for j in range(0,n2):
                if word1[i] == word2[j]:
                    cost = 0
                else:
                    cost = 1
                newdp[j+1] = min(dp[j+1]+1,newdp[j]+1,dp[j]+cost)
            dp = newdp


        return dp[-1]
                
        
s = Solution()
print s.minDistance("sea","eat")#2
print s.minDistance("park","spake")#3
print s.minDistance("food","money")#4
print s.minDistance("kitten","sitting")#3
print s.minDistance("a","a")#0

        
#Edit Distance
#https://oj.leetcode.com/problems/edit-distance/