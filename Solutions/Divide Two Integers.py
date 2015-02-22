class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return (1<<31) -1
        if dividend < 0 and divisor < 0:
            r = self.div(-dividend,-divisor)
        elif dividend < 0 or divisor < 0:
            r = - self.div(abs(dividend),abs(divisor))
        else:
            r = self.div(dividend,divisor)
        if r > (1<<31) -1:
            return (1<<31) -1
        return r
        
                
    def div(self,dividend,divisor):
        if divisor > dividend:
            return 0

        for i in range(1,32):
            multiplier = divisor << i
            if multiplier == dividend:
                return 1<<i
            if multiplier > dividend:
                d = 1 << (i-1)
                remain = dividend - (divisor<<(i-1))
                return d + self.div(remain,divisor)
                
s = Solution()
print s.divide(-2147483648,-1)
                
                
                    
        
#Divide Two Integers
#https://oj.leetcode.com/problems/divide-two-integers/