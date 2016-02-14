class Solution(object):
    def countDigitOne(self, n):
        d = 1
        count = 0
        range_total = 0   # number of 1's in [0, d / 10]
        while d <= n:
            r = n % d
            c = (n % (10 * d)) / d

            if c > 0:
                count = c * range_total + count + (d if c > 1 else (r + 1))

            range_total = 10 * range_total + d
            d *= 10

        return count
        
s = Solution()
input = 11
print s.countDigitOne(input)     
#Number of Digit One
#https://leetcode.com/problems/number-of-digit-one/
