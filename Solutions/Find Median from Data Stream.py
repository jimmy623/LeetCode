from heapq import heappush,heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num):
        if not self.right:
            self.right.append(num)
            return
        if num >= self.right[0]:
            heappush(self.right,num)
            if len(self.right) > len(self.left)+1:
                heappush(self.left,-heappop(self.right))
        else:
            heappush(self.left,-num)
            if len(self.left) > len(self.right):
                heappush(self.right,-heappop(self.left))

    def findMedian(self):
        if len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2.0

    #     self.left = []
    #     self.right = []
    #     self.middle = []

    # def addNum(self, num):
    #     """
    #     :type num: int
    #     :rtype: void
    #     """
    #     if not self.middle:
    #       self.middle.append(num)
    #       return
    #     if len(self.middle) == 1:
    #       if num >= self.middle[0]:
    #           if not self.right or num <= self.right[0]:
    #               self.middle.append(num)
    #           else:
    #               self.middle.append(heappop(self.right))
    #               heappush(self.right,num)
    #       else:
    #           if not self.left or num >= -self.left[0]:
    #               self.middle = [num] + self.middle
    #           else:
    #               self.middle = [-heappop(self.left)]+self.middle
    #               heappush(self.left,-num)
    #     else:
    #       if self.middle[0] <= num <= self.middle[1]:
    #           heappush(self.left,-self.middle[0])
    #           heappush(self.right,self.middle[1])
    #           self.middle = [num]
    #       elif num < self.middle[0]:
    #           heappush(self.left,-num)
    #           heappush(self.right,self.middle[1])
    #           self.middle = [self.middle[0]]
    #       else:
    #           heappush(self.right,num)
    #           heappush(self.left,-self.middle[0])
    #           self.middle = [self.middle[1]]
        

    # def findMedian(self):
    #     """
    #     :rtype: float
    #     """
    #     if not self.middle:
    #       return 0
    #     return float(sum(self.middle))/len(self.middle)
        
s = MedianFinder()
data = [12,10,13,11,5,15,1,11,6,17,14,8,17,6,4,16,8,10,2,12,0]
data = [1,2,3]
for n in data:
    s.addNum(n)
    # print n,s.findMedian(),s.left,s.middle,s.right
    print n,s.findMedian(),s.left,s.right

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#Find Median from Data Stream
#https://leetcode.com/problems/find-median-from-data-stream/description/