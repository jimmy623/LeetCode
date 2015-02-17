class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        t = 0
        for i in A:
            t = t^i
        return t
#Single Number
#https://oj.leetcode.com/problems/single-number/