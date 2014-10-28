class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split(" ")
        num = len(words)
        while num > 0:
            if len(words[num-1]) > 0:
                return len(words[num-1])
            num -=1
        return 0
        
        

#Length of Last Word
#https://oj.leetcode.com/problems/length-of-last-word/