class Solution:
    # @return a string
    def intToRoman(self, num):
        result = ""
                
        s1000 = ["","M","MM","MMM"]
        s100 = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        s10 = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        s1 = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        print num  
        i = num/1000
        result += s1000[i]
        num -= i * 1000
        
        print i
        i = num/100
        result += s100[i]
        num -= i*100
        print i
        
        i = num/10
        result += s10[i]
        num -= i*10
        
        i = num
        result += s1[i] 
        
        
        return result
        
s = Solution()
print s.intToRoman(1)
#Integer to Roman
#https://oj.leetcode.com/problems/integer-to-roman/