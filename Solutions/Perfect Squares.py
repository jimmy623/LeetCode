# from math import *
from sets import Set;
class Solution(object):
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # toCheck = Set()
        # toCheck.add(n)
        # s = Set()
        # i = 1
        # while i * i <= n:
        #     s.add( i * i )
        #     i += 1
        # count = 1
        # while toCheck:
        #     temp = Set()
        #     for i in toCheck:
        #         if i in s:
        #             return count
        #         for k in s:
        #             if k < i:
        #                 temp.add(i-k)
        #     count += 1
        #     toCheck = temp


    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt

s = Solution()
print s.numSquares(12)
#Perfect Squares
#https://leetcode.com/problems/perfect-squares/description/