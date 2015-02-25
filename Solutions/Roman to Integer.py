class Solution:
    # @return an integer
    def romanToInt(self, s):
        digits = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        result = 0
        while len(s):
            for i in range(13):
                t = digits[i]
                n = len(t)
                if n > len(s):
                    continue
                c = s[0:n]
                if c == t:
                    result += value[i]
                    s = s[n:len(s)]
                    break
        return result
#Roman to Integer
#https://oj.leetcode.com/problems/roman-to-integer/