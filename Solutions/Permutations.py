from sets import Set
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.result = []
        remain = Set(num)
        self.dfs([],remain)
        return self.result
    
    def dfs(self,route,remain):
        if len(remain) == 1:
            route.append(remain.pop())
            self.result.append(route)
            return
        for i in remain:
            newRoute = list(route)
            newRemain = Set(remain)
            newRoute.append(i)
            newRemain.remove(i)
            self.dfs(newRoute,newRemain)
            
s = Solution()
print s.permute([1,2,3])
        
#Permutations
#https://oj.leetcode.com/problems/permutations/