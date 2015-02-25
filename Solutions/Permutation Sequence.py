import math
f = math.factorial
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        digits = range(1,n+1)
        i = n
        result = ""
        k -= 1
        while i:
            pers = f(i-1)
            index = k/pers
            result += str(digits.pop(index))
            k = k % pers
            i-= 1
        
    
s = Solution()
print s.getPermutation(3,6)
        
        
#Permutation Sequence
#https://oj.leetcode.com/problems/permutation-sequence/