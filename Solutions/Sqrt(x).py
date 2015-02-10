class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 1:
            return 1
        min = 0
        max = x
        d = (min+max)/2
        v = d*d
        while v != x:
            if v > x:
                max = d
            elif (d+1)*(d+1)>x:
                return d
            else:
                min = d
            d = (min+max)/2
            v = d * d
        
        return d

        
s = Solution()
#Sqrt(x)
#https://oj.leetcode.com/problems/sqrtx/

print s.sqrt(2)
            
        