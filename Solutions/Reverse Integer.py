class Solution:
    # @return an integer
    def reverse(self, x):
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        
        a = x
        count = 0
        while a != 0:
            a /= 10
            count += 1
        
        ns = []
        for i in range(count):
            ns.append(self.digit(x,i))
            
        n = 0
        for i in range(count):
            n += ns[i] * (10**(count - 1 - i))
            
        iMax = (1<<31)-1
        iMin = - (1<<31)
        n *= flag
        if n > iMax or n < iMin:
            return 0
        return n
        
        
            
    def digit(self,x,i):
        pre = x / (10 ** (i+1))
        remain = x - pre * (10**(i+1))
        d = remain / (10**i)
        return d

#Reverse Integer
#https://oj.leetcode.com/problems/reverse-integer/