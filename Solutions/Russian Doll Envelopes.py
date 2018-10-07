from bisect import bisect_left
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        def f(x,y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1

        envelopes.sort(cmp = f)
        r = []
        for i in xrange(len(envelopes)):
            w,h = envelopes[i]
            index = bisect_left(r,h)
            if index < len(r):
                r[index] = h
            else:
                r.append(h)
        return len(r)

        
#Russian Doll Envelopes
#https://leetcode.com/problems/russian-doll-envelopes/description/