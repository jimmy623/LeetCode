class MyCalendarTwo(object):

    def __init__(self):
        self.slots = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i,j in self.overlaps:
            if start <j and end > i:
                return False
        for i,j in self.slots:
            if start < j and end > i:
                self.overlaps.append([max(start,i),min(end,j)])
        self.slots.append([start,end])
        return True
#My Calendar II
#https://leetcode.com/problems/my-calendar-ii/description/