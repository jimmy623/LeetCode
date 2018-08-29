# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import sys
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = -sys.maxint - 1
        high = sys.maxint
        while True:
        	mid = (low+high)/2
        	print low,high,mid
        	r = guess(mid)
        	if r == 0:
        		return mid
        	if r == 1:
        		low = mid +1
        	else:
        		high = mid-1
        	# if high - low == 1:
        	# 	if guess(high) == 0:
        	# 		return high
        	# 	else:
        	# 		return low
#Guess Number Higher or Lower
#https://leetcode.com/problems/guess-number-higher-or-lower/description/