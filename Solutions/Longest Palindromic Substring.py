class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        longest = 1
        result = (0,1)
        n = len(s)
        
        for i in range(0,n-1):
            if longest > min((i+1)*2,(n-i)*2):
                break
            j = 1
            length = 1
            while i - j >= 0 and i+j <= n-1:
                if s[i-j] == s[i+j]:
                    length += 2
                    if length > longest:
                        longest = length
                        result = (i-j,i+j+1)
                    j += 1
                else:
                    break
            if s[i] == s[i+1]:
                if longest == 1:
                    longest = 2
                    result = (i,i+2)
                j = 1
                length = 2
                while i-j >= 0 and i+j+1 <= n-1:
                    if s[i-j] == s[i+j+1]:
                        length += 2
                        if length > longest:
                            longest = length
                            result = (i-j,i+j+2)
                        j += 1
                    else:
                        break
        return s[result[0]:result[1]]

s = Solution()
print s.longestPalindrome("dddddddd")
                
                
            
#Longest Palindromic Substring
#https://oj.leetcode.com/problems/longest-palindromic-substring/
