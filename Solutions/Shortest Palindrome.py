class Solution:
# @param {string} s
# @return {string}
    def shortestPalindrome(self, s):
        A=s+"*"+s[::-1]
        print A
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            print i,index,cont
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
        return s[cont[-1]:][::-1]+s

s = Solution()
data = "abccbaeuf"
print s.shortestPalindrome(data)

#Shortest Palindrome
#https://leetcode.com/problems/shortest-palindrome/
