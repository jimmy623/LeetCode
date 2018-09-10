class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        dp = []
        wlen = len(sentence[0])
        p = 0
        wsum = 0
        for i,w in enumerate(sentence):
            while wsum + wlen <= cols:
                wsum  = wsum + wlen
                p += 1
                wlen = len(sentence[p%len(sentence)])+1
            dp.append(p-i)
            wsum -= (len(w) + 1)

        w_count = 0
        for _ in xrange(rows):
            w_count += dp[w_count % len(sentence)]
        return w_count/len(sentence)
                


s = Solution()
print s.wordsTyping(["f", "p", "a"],8,7)
#Sentence Screen Fitting
#https://leetcode.com/problems/sentence-screen-fitting/description/