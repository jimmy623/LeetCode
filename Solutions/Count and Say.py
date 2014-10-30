class Solution:
    # @return a string
    def countAndSay(self, n):
        string = str(n)
        result = self.generate("1",n)
        
        return result

    def generate(self,string,n):
        index = 0
        length = len(string)
        result = ""

        while index < length:
            digit = string[index]
            offset = 1
            while index + offset < length and string[index + offset] == digit:
                offset += 1
            result += str(offset)
            result += digit
            
            index += offset

        if n == 1:
            return "1"
        elif n == 2:
            return result
        else:
            return self.generate(result,(n-1))
        

n = 5
s = Solution()
result = s.countAndSay(n)
print result

#https://oj.leetcode.com/problems/count-and-say/
#Count and Say
