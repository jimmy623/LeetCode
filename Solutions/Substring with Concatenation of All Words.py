class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        length = len(L[0])
        num = len(L)
        slen = len(S)
        index = 0
        result = []
        while index + length*num <= slen:
            sub = S[index:index+length]
            remain = list(L)
            count = 0
            while len(remain):
                if sub in remain:
                    remain.remove(sub)
                    count += 1
                    sub = S[index+length*count:index+length*(count+1)]
                else:
                    break
                
            if count == num:
                result.append(index)
                
            index += 1
            
        return result

S = "barfoothefoobarman"
L = ["foo","bar"]
s = Solution()
result = s.findSubstring(S,L)
print result

#https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/
#Substring with Concatenation of All Words