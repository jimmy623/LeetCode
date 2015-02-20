class Solution:
    # @return a string
    def convert(self, s, nRows):
        grid = ["" for i in range(nRows)]
        i = 0
        zigzag = False
        zigStart = max(nRows-2,0)
        for c in s:
            if zigzag:
                grid[i]+=c
                i -= 1
                if i <= 0:
                    zigzag = False
                    i = 0
            else:
                grid[i] += c
                i += 1
                if i == nRows:
                    i = zigStart
                    if i != 0:
                        zigzag = True
                    
        result = ""
        for r in grid:
            result += r
        return result
        
        
s = Solution()
#print s.convert("PAYPALISHIRING",3)
#print s.convert("ABC",2)
print s.convert("ABCD",2)

#ZigZag Conversion
#https://oj.leetcode.com/problems/zigzag-conversion/