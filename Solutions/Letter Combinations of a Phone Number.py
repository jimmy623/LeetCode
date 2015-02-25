class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dict = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
        self.result = []
        self.dfs(digits,"")
        return self.result
    
    def dfs(self,remain,str):
        if len(remain) == 0:
            self.result.append(str)
            return
        options = self.dict[remain[0]]
        length = len(remain)
        for c in options:
            newStr = str + c
            self.dfs(remain[1:length],newStr)
        
        
        
        

#Letter Combinations of a Phone Number
#https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/