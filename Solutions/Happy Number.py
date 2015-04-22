class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        been = []
        i = n
        while not i in been:
            been.append(i)
            s = str(i)
            sum = 0
            for c in s:
                digit = int(c)
                sum += digit * digit
            if sum == 1:
                return True
            else:
                i = sum
        return False
        
#Happy Number
#https://leetcode.com/problems/happy-number/