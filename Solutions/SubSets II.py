class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        values = {}
        result = []
        for i in S:
            if i in values:
                values[i] += 1
            else:
                values[i] = 1
        keys = sorted(values.keys())

        result = self.dfs(keys,values)
        return result


    def dfs(self,keys,values):
        this = []
        for i in range(values[keys[0]] + 1):
            one = []
            for i in range(i):
                one.append(keys[0])
            this.append(one)

        if len(keys) != 1:
            suffix = self.dfs(keys[1:],values)    
            this = self.combine(this,suffix)
        
        return this
                
    def combine(self,list1,list2):
        result = []
        for i in list1:
            for j in list2:
                result.append(i+j)
        return result


S = [1,2,2]

sol = Solution()
r = sol.subsetsWithDup(S)
print "Result:"
print r

"""
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

#Subsets II
#https://oj.leetcode.com/problems/subsets-ii/