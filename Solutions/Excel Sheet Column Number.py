class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        n = len(s)
        result = 0
        for i in range(n):
            c = s[n-1-i]
            d = ord(c) - 64
            result += d*(26**i)
        return result
#Excel Sheet Column Number
#https://oj.leetcode.com/problems/excel-sheet-column-number/