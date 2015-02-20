class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
            
        a = x
        count = 0
        while a != 0:
            a /= 10
            count += 1
        
        for i in range(count/2):
            if self.digit(x,i) != self.digit(x,count-i-1):
                return False
        return True
            
    def digit(self,x,i):
        pre = x / (10 ** (i+1))
        remain = x - pre * (10**(i+1))
        d = remain / (10**i)
        return d
        
        
s = Solution()
print s.isPalindrome(-2147483648)
#Palindrome Number
#https://oj.leetcode.com/problems/palindrome-number/