class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.dfs(0,n,k)



    def dfs(self,index,sum,count):
        #print index,sum,count
        result = []
        if index >= sum:
            return [[]]
        if count == 1:
            if sum < 10:
                return [[sum]]

        for i in range(index+1,10):
            arrays = self.dfs(i,sum-i,count-1)
            for d in arrays:
                if len(d):
                    result.append([i]+d)
        return result


s = Solution()
k = 3
n = 9
print s.combinationSum3(k,n)


#Combination Sum III
#https://leetcode.com/problems/combination-sum-iii/
