class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.results = []
        self.generate("",n,n)
        
        return self.results
        
    def generate(self,s,left,right):
        if left == 0 and right == 0:
            self.results.append(s)
            return
            
        if left == right:
            r = s + "("
            self.generate(r,left-1,right)
        else:
            if left > 0:
                r1 = s+"("
                self.generate(r1,left-1,right)
                
            r2 = s+")"
            self.generate(r2,left,right-1)
            
s = Solution()
print s.generateParenthesis(3)
            
    
#Generate Parentheses
#https://oj.leetcode.com/problems/generate-parentheses/