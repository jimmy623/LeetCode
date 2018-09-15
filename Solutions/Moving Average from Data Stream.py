from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.sum = 0.0
        self.size = 0.0
        self.window = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size >= self.window:
        	self.sum -= self.q.popleft()
        else:
        	self.size += 1
        self.sum += val
        self.q.append(val)
        return self.sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
#Moving Average from Data Stream
#https://leetcode.com/problems/moving-average-from-data-stream/description/