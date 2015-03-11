class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            bit = 1 << i
            if n & bit:
                result |= 1 << (31-i)
        return result
#Reverse Bits
#https://leetcode.com/problems/reverse-bits/