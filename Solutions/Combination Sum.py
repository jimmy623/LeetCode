class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.candidats.sort()
        self.target = target
        self.result = []
        self.dfs(0,[],0)
        return self.result
        
    def dfs(self,sum,route,index):
        if index >= len(self.candidates):
            return
        v = self.candidates[index]
        
        possible = (self.target-sum)/v
        if possible == 0:
            return
        
        for i in range(possible+1):
            temp = sum + v*i
            newRoute = list(route)
            for t in range(i):
                newRoute.append(v)
            
            if temp == self.target:
                self.result.append(newRoute)
                return
            self.dfs(temp,newRoute,index+1)
        
s = Solution()
print s.combinationSum([2,3,6,7],7)  
#Combination Sum
#https://oj.leetcode.com/problems/combination-sum/