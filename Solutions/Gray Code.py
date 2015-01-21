class Solution:
    # @return a list of integers
    def grayCode(self, n):
        self.result = [0]
        self.n = n
        current = []
        for i in range(n):
            current.append(0)
        
        flag = True
        count = 1
        max = 2**n
        while count != max:
            test = current
            for i in range(n):
                test[n-i-1] = 1 - test[n-i-1]
                candidate = self.bitsToInt(test)
                if candidate in self.result:
                    test[n-i-1] = 1 - test[n-i-1]
                else:
                    self.result.append(candidate)
                    count += 1
                    break
                
                
                
        return self.result
            
    def bitsToInt(self,bits):
        r = 0
        for i in range(self.n):
            b = self.n-i-1
            if bits[b] == 1:
                r += 1<<i
        return r
        
        
s = Solution()
r = s.grayCode(2)
print "result",r
#Gray Code
#https://oj.leetcode.com/problems/gray-code/