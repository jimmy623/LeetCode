class Solution:
    # @return an integer
    def atoi(self, str):
        n = len(str)
        i = 0
        while i < n and str[i] == " ":
            i += 1

        if i >= n:
            return 0
            
        minus = 1
        
        if str[i] == "-":
            i+= 1
            minus = -1
        elif str[i] == "+":
            i+= 1
        
        if i>= n:
            return 0
            
        if not str[i] in "01234567890":
            return 0
        
        num = ""
        iMax= 2147483647
        iMin = -2147483648
        while i < n:
            if str[i] in "01234567890":
                num += str[i]
            else:
                break
            i+= 1
        result = int(num) * minus
        if result > iMax:
            return iMax
        if result < iMin:
            return iMin
        return result
            
s = Solution()
print s.atoi("1")
            
#String to Integer (atoi)
#https://oj.leetcode.com/problems/string-to-integer-atoi/