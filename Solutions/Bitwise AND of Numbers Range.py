class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        result = 0
        for i in range(31):
            if m & 1 << i:
                a = n>>i
                b = m>>i
                if a > 0:
                    if a - b == 0:                  
                        result |= 1<<i
        return result
            
s = Solution()
# print s.rangeBitwiseAnd(0,2147483647)
# 
print s.rangeBitwiseAnd(5,7)

print s.rangeBitwiseAnd(3,4)

#print s.rangeBitwiseAnd(600000000,2147483645)
        
        
        
            
#Bitwise AND of Numbers Range
#https://leetcode.com/problems/bitwise-and-of-numbers-range/