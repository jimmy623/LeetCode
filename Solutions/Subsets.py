class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if len(S) == 0:
            return [[]]
        S.sort()
        self.S = S
        self.result = []
        self.dfs(0,[])
        return self.result
        
    def dfs(self,n,route):
        if n == len(self.S):
            self.result.append(route)
            return
        nr1 = list(route)
        self.dfs(n+1,nr1)
        nr2 = list(route)
        nr2.append(self.S[n])
        self.dfs(n+1,nr2)
        
#Subsets
#https://oj.leetcode.com/problems/subsets/