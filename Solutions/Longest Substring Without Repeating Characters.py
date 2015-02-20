from sets import Set
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        start = 0
        length = 1
        digits = Set()
        digits.add(s[0])
        for i in range(1,len(s)):
            c = s[i]
            if c in digits:
                while True:
                    cs = s[start]
                    start += 1
                    if cs == c:
                        break
                    else:
                        digits.remove(cs)
            else:
                digits.add(c)
                ll = len(digits)
                length = max(length,ll)
        return length
                
#Longest Substring Without Repeating Characters
#https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/