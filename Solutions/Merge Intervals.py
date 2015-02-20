# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda x:x.start)
        result = [intervals[0]]
        pre = intervals[0]
        i = 1
        while i < n:
            time = intervals[i]
            if time.start <= pre.end:
                pre.end = max(time.end,pre.end)
            else:
                result.append(time)
                pre = time
            
            i += 1
            
            
        return result
            
            
#Merge Intervals
#https://oj.leetcode.com/problems/merge-intervals/