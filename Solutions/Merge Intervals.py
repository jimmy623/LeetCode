# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
    	return str(self.start)+"|"+str(self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
        	return []
        intervals.sort(key=lambda e: (e.start,e.end))
        # print intervals
        result = [intervals[0]]
        for intv in intervals:
        	# print intv.start,intv.end,result
        	if intv.start <= result[-1].end:
        		result[-1].end = max(intv.end,result[-1].end)
        	else:
        		result.append(intv)
        return result

s = Solution()
print s.merge([Interval(1,4),Interval(1,5)])
#Merge Intervals
#https://leetcode.com/problems/merge-intervals/description/