class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = ' '.join(s.split()).split()
        if len(words) == 0:
            return ""
        words.reverse()
        return " ".join(words)
#Reverse Words in a String
#https://oj.leetcode.com/problems/reverse-words-in-a-string/