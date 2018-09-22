from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = defaultdict(list)
        for i in xrange(len(s)-1,-1,-1):
            d[s[i]].append(i)
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = []
        left = 0
        while d:
            right = len(s)
            candidates = []
            for c,pos in d.items():
                right = min(right,pos[0])
            for c,pos in d.items():
                if pos[-1] <=right:
                    candidates.append([c,pos[-1]])

            candidates.sort()
            char,i = candidates[0]
            result.append(char)
            left = i+1
            del d[char]
            for c,pos in d.items():
                while pos[-1] < left:
                    pos.pop()

        return "".join(result)
            

s = Solution()
print s.removeDuplicateLetters("bcabc")
print s.removeDuplicateLetters("cbacdcbc")

#Remove Duplicate Letters
#https://leetcode.com/problems/remove-duplicate-letters/description/