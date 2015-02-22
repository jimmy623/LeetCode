class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        f = [False for x in range(n+1)]
        
        for i in A:
            if i > 0 and i < n+1:
                f[i-1] = True
        for i in range(n+1):
            if f[i] == False:
                return i+1
        return 1

s = Solution()
print s.firstMissingPositive([1])
#First Missing Positive
#https://oj.leetcode.com/problems/first-missing-positive/