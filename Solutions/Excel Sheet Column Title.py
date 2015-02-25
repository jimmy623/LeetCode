import string
class Solution:
    # @return a string
    def convertToTitle(self, num):
        dict = string.ascii_uppercase
        result = ""
        while num:
            d = (num-1) % 26
            num = (num-1) / 26
            result = dict[d] + result
        return result
        

#Excel Sheet Column Title
#https://oj.leetcode.com/problems/excel-sheet-column-title/