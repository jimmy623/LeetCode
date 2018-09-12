class MyCalendar(object):

    def __init__(self):
        self.slots = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        head = 0
        tail = len(self.slots)-1
        index = len(self.slots)
        while head <= tail:
        	m = (head + tail)/2
        	if self.slots[m][0] < end:
        		head = m+1
        	else:
        		tail = m-1
        #if head >= len(self.slots):
        #print self.slots,head,start,end
        if head == 0 or self.slots[head-1][1] <= start:
       		self.slots.insert(head,[start,end])
       		return True
       	else:
       		return False
        

        #print head,tail,self.slots
        
        	

m = MyCalendar()
print m.book(47,50)
print m.book(33,41)
print m.book(39,45)

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#My Calendar I
#https://leetcode.com/problems/my-calendar-i/description/