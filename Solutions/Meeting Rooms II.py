# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from Queue import deque;
from operator import itemgetter, attrgetter
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
        	return 0
        intervals.sort(key=attrgetter("start"))
        q = deque()
        q.append(intervals[0])
        rooms = 1
        p = 1

        while p < len(intervals):
        	intv = intervals[p]
        	count = 1
    		for x in q:
    			if x.end > intv.start:
    				count += 1
    		if count > 1:
    			q.append(intv)
    			p += 1
    			rooms = max(rooms,count)
    		else:
    			if len(q):
    				q.popleft()
    			else:
    				q.append(intv)
    				p += 1




        return rooms


#Meeting Rooms II
#https://leetcode.com/problems/meeting-rooms-ii/description/