class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.candidates = candidates
        self.candidates.sort()
        self.target = target
        self.result = []
        self.dfs(0,[],0)
        return self.result
        
    def dfs(self,sum,route,index):
        if index >= len(self.candidates):
            return
        v = self.candidates[index]
        
        if sum + v > self.target:
            return
        
        self.dfs(sum,route,index+1)
        newRoute = list(route)
        newRoute.append(v)

        if sum+v == self.target:
            if not newRoute in self.result:
                self.result.append(newRoute)
        else:
            self.dfs(sum+v,newRoute,index+1)
        
s = Solution()
print s.combinationSum2([1,1],1)
        
#Combination Sum II
#https://oj.leetcode.com/problems/combination-sum-ii/