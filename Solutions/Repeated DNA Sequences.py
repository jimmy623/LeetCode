class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        dict = {}
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in dict:
                dict[seq] += 1
            else:
                dict[seq] = 1
        result = []
        for seq, count in dict.iteritems():
            if count > 1:
                result.append(seq)
        return result
            
#Repeated DNA Sequences
#https://oj.leetcode.com/problems/repeated-dna-sequences/