# from heapq import heappush,heappop
# class RecentCounter(object):

#     def __init__(self):
#         self.pings = []

#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """
#         while self.pings:
#             if t - self.pings[0] > 3000:
#                 heappop(self.pings)
#             else:
#                 break
#         heappush(self.pings,t)
#         return len(self.pings)
        
from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.pings = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.pings:
            if t - self.pings[0] > 3000:
                self.pings.popleft()
            else:
                break
        self.pings.append(t)
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#Number of Recent Calls
#https://leetcode.com/problems/number-of-recent-calls/