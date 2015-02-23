# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        result = []
        for inter in intervals:
            if newInterval == None:
                result.append(inter)
                continue
            
            if newInterval.end < inter.start:
                result.append(newInterval)
                newInterval = None
                result.append(inter)
                continue
            
            if newInterval.start > inter.end:
                result.append(inter)
                continue
            
            newInterval.start = min(newInterval.start,inter.start)
            newInterval.end = max(newInterval.end,inter.end)
        if newInterval:
            result.append(newInterval)
        return result
        
s = Solution()
inters = [Interval(1,5)]
newInterval = Interval(2,3)
print s.insert(inters,newInterval)
                
#Insert Interval
#https://oj.leetcode.com/problems/insert-interval/