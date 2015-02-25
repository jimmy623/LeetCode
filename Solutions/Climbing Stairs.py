class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        one,two = 1,2
        for i in range(3,n+1):
            one,two = two,one+two
            
        return two
        

#Climbing Stairs
#https://oj.leetcode.com/problems/climbing-stairs/