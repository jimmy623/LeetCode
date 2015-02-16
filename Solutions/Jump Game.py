class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        end = A[0]
        
        i = 0
        while i <= end:
            end = max(end,i+A[i])
            if end >= n-1:
                return True
            i+=1
        return False

s = Solution()
print s.canJump([1,2,3])
#Jump Game
#https://oj.leetcode.com/problems/jump-game/