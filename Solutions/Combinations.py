class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.result = []
        self.generate(1,n,k,[])
        return self.result
        
    def generate(self,s,e,k,route):
        if k == 0:
            self.result.append(route)
            return
        for i in range(s,e-k+2):
            nr = list(route)
            nr.append(i)
            self.generate(i+1,e,k-1,nr)
            
s = Solution()
print s.combine(4,2)      
#Combinations
#https://oj.leetcode.com/problems/combinations/