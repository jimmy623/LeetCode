class Solution:
    # @return an integer
    result = {}
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if (m,n) in self.result:
            return self.result[(m,n)]
        r = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        self.result[(m,n)] = r
        return r
        
        
s = Solution()
print s.uniquePaths(3,7)

#Unique Paths
#https://oj.leetcode.com/problems/unique-paths/