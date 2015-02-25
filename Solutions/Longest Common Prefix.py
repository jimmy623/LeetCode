class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        start = strs[0]
        ls = len(start)
        length = 0
        while length < ls:
            c = start[length]
            for i in range(1,n):
                word = strs[i]
                if length >= len(word):
                    return start[0:length]
                if not word[length] == c:
                    return start[0:length]
            length += 1
            
        return start
#Longest Common Prefix
#https://oj.leetcode.com/problems/longest-common-prefix/