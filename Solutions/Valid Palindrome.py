import re
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = re.sub(r"\W+",'',s)
        s = s.lower()
        n = len(s)
        for i in range(n/2):
            if s[i] != s[n-i-1]:
                return False
        return True
        
        
s = Solution()
print s.isPalindrome("aA")
#Valid Palindrome
#https://oj.leetcode.com/problems/valid-palindrome/