class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False
            
        while True:
            if n == 1:
                return True
                
            r = n%2
            if r == 1:
                return False
            n = n/2

            

        
        
#Power of Two
#https://leetcode.com/problems/power-of-two/