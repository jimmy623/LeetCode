class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        nh = len(haystack)
        nn = len(needle)

        for i in range(nh-nn+1):
            flag = True
            for j in range(nn):
                if needle[j] != haystack[i+j]:
                    flag = False
                    break
            if flag:
                return i
        return -1
        
        
        
sol = Solution()
print sol.strStr("","")
#Implement strStr()
#https://oj.leetcode.com/problems/implement-strstr/