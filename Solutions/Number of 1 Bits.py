class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        for i in range(32):
            bit = 1<<i
            if n & bit:
                count += 1
        return count
#Number of 1 Bits
#https://leetcode.com/problems/number-of-1-bits/