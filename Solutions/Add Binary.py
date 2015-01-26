class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        str = bin(int(a,2)+int(b,2))
        return str[2:len(str)]
#Add Binary
#https://oj.leetcode.com/problems/add-binary/