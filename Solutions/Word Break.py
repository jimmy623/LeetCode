class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dict = dict
        n = len(s)
        result = [False for i in range(n)]

        for i in range(n-1,-1,-1):

            if s[i:n] in dict:
                result[i] = True
                continue	
            for j in range(i+1,n):
                if result[j] == True:

                    if s[i:j] in dict:
                        result[i] = True
                        continue

        return result[0]       

        
	
s = Solution()
dict = ["leet","code"]
t = "leetcode"
print s.wordBreak(t,dict)

    	
#Word Break
#https://oj.leetcode.com/problems/word-break/