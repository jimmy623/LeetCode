class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        dict = dict
        n = len(s)
        result = [[] for i in range(n)]
        
        for i in range(n-1,-1,-1):
        
            if s[i:n] in dict:
                result[i].append(s[i:n])
            for j in range(i+1,n):
                if len(result[j]) > 0:
                    if s[i:j] in dict:
                        for w in result[j]:
                            result[i].append(s[i:j]+" "+ w)
                        continue
        
        
        return result[0]
        
s = Solution()
t = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
print s.wordBreak(t,dict)
#Word Break II
#https://oj.leetcode.com/problems/word-break-ii/