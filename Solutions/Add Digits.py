class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return (num-10)%9+1
        
#Add Digits
#https://leetcode.com/problems/add-digits/description/