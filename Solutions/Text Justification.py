class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        
        self.result = []
        line = []
        count = 0
        self.L = L
        for w in words:
            n = len(w)
            if count + n > L:
                self.process(line,count)
                line = [w]
                count = n
                if n < L:
                    line.append(" ")
                    count += 1
                
            else:
                line.append(w)
                count += n
                if n < L:
                    line.append(" ")
                    count += 1

        if len(line):
            str = ""
            for w in line:
                str += w
            str += " " * (L - len(str))
            self.result.append(str)
        
        return self.result
        
    def process(self,line,count):
        if len(line) > 2:
            if line[-1] == " ":
                line.pop()
                count -= 1
                
        spaces = len(line)/2
        if spaces > 0:
            remain = self.L - count
            count = remain / spaces
            remain = remain % spaces
            for i in range(spaces):
                index = i*2+1
                num = count
                if i < remain:
                    num += 1
                line[index] = " " * (1 + num)
        str = ""
        for w in line:
            str += w
        self.result.append(str)
            
            

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
words = [""]
L = 2
print s.fullJustify(words,L)
        
            
#Text Justification
#https://oj.leetcode.com/problems/text-justification/