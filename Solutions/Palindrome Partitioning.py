class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.result = []
        self.dfs(s,[])
        return self.result
        
    def dfs(self,s,route):
        n = len(s)
        if n == 1:
            r = list(route)
            r.append(s)
            self.result.append(r)
            return

        for i in range(1,n+1):
            before = s[0:i]
            if self.isPalindrome(before):
                r = list(route)
                r.append(before)
                if i == n:
                    self.result.append(r)
                else:
                    after = s[i:n]
                    self.dfs(after,r)
            
    
    def isPalindrome(self,s):
        for i in range(len(s)/2):
            if s[i] != s[-i-1]:
                return False
        return True
            
s = Solution()
print s.partition("aab")

#Palindrome Partitioning
#https://oj.leetcode.com/problems/palindrome-partitioning/https://oj.leetcode.com/problems/palindrome-partitioning/