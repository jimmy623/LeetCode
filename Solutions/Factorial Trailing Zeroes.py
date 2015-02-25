class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n >= 5:
            n = n/5
            result += n

        return result
        
#Factorial Trailing Zeroes
#https://oj.leetcode.com/problems/factorial-trailing-zeroes/
